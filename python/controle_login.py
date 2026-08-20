import tkinter as tk
from tkinter import messagebox
import requests

# =========================================================
# SISTEMA LOCAL DE USUARIOS
# =========================================================
# Sem arquivo JSON e sem importar pedro.py.
# Os usuarios ficam salvos apenas enquanto o programa estiver aberto.
# Se quiser deixar usuarios fixos, coloque aqui, por exemplo:
# USUARIOS = [("admin", "1234")]
USUARIOS = []


def cadastrar_usuario(nome, senha):
    nome = nome.strip()
    senha = senha.strip()

    if not nome or not senha:
        return False, "Nome e senha sao obrigatorios."

    for usuario_cadastrado, _ in USUARIOS:
        if usuario_cadastrado == nome:
            return False, "Esse usuario ja esta cadastrado."

    USUARIOS.append((nome, senha))
    return True, "Usuario cadastrado com sucesso!"


def validar_usuario(nome, senha):
    nome = nome.strip()
    senha = senha.strip()

    for usuario_cadastrado, senha_cadastrada in USUARIOS:
        if usuario_cadastrado == nome and senha_cadastrada == senha:
            return True

    return False


def listar_usuarios():
    return [nome for nome, _ in USUARIOS]


# =========================================================
# CONFIGURACAO DO CONTROLE DO ROBO
# =========================================================
IP_ESP32 = "http://10.10.0.2"


def enviar(comando):
    try:
        requests.get(f"{IP_ESP32}/{comando}", timeout=1)
        print("Comando:", comando)
    except requests.RequestException:
        print("Erro ao conectar ao ESP32")


# =========================================================
# INTERFACE TKINTER
# =========================================================
root = tk.Tk()
root.title("Sistema do Robo")
root.geometry("500x420")
root.configure(bg="#18669A")

frame_atual = None


def limpar_tela():
    global frame_atual

    if frame_atual is not None:
        frame_atual.destroy()

    frame_atual = tk.Frame(root, bg="#18669A")
    frame_atual.pack(fill="both", expand=True)
    return frame_atual


def criar_titulo(frame, texto):
    titulo = tk.Label(
        frame,
        text=texto,
        font=("Arial", 22, "bold"),
        bg="#18669A",
        fg="white"
    )
    titulo.pack(pady=25)
    return titulo


def criar_label(frame, texto, tamanho=14):
    label = tk.Label(
        frame,
        text=texto,
        font=("Arial", tamanho),
        bg="#18669A",
        fg="white"
    )
    label.pack()
    return label


def tela_menu():
    frame = limpar_tela()
    criar_titulo(frame, "ACESSO AO CONTROLE")

    aviso = tk.Label(
        frame,
        text="Cadastre um usuario ou faca login para abrir o controle do robo.",
        font=("Arial", 12),
        bg="#18669A",
        fg="white",
        wraplength=420
    )
    aviso.pack(pady=10)

    tk.Button(
        frame,
        text="1 - CADASTRAR USUARIO",
        font=("Arial", 13, "bold"),
        width=25,
        command=tela_cadastro
    ).pack(pady=12)

    tk.Button(
        frame,
        text="2 - LOGAR NO SISTEMA",
        font=("Arial", 13, "bold"),
        width=25,
        command=tela_login
    ).pack(pady=12)

    tk.Button(
        frame,
        text="3 - LISTAR USUARIOS",
        font=("Arial", 13, "bold"),
        width=25,
        command=mostrar_usuarios
    ).pack(pady=12)

    tk.Button(
        frame,
        text="4 - SAIR",
        font=("Arial", 13, "bold"),
        width=25,
        command=root.destroy
    ).pack(pady=12)


def tela_cadastro():
    frame = limpar_tela()
    criar_titulo(frame, "CADASTRO")

    criar_label(frame, "Usuario")
    entrada_usuario = tk.Entry(frame, font=("Arial", 14))
    entrada_usuario.pack(pady=8)

    criar_label(frame, "Senha")
    entrada_senha = tk.Entry(frame, show="*", font=("Arial", 14))
    entrada_senha.pack(pady=8)

    def confirmar_cadastro():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()

        sucesso, mensagem = cadastrar_usuario(usuario, senha)

        if sucesso:
            messagebox.showinfo("Cadastro", mensagem)
            tela_login()
        else:
            messagebox.showerror("Erro", mensagem)

    tk.Button(
        frame,
        text="CADASTRAR",
        font=("Arial", 13, "bold"),
        width=15,
        command=confirmar_cadastro
    ).pack(pady=20)

    tk.Button(
        frame,
        text="VOLTAR",
        font=("Arial", 12),
        width=15,
        command=tela_menu
    ).pack()

    entrada_usuario.focus_set()


def tela_login():
    frame = limpar_tela()
    criar_titulo(frame, "LOGIN DO ROBO")

    criar_label(frame, "Usuario")
    entrada_usuario = tk.Entry(frame, font=("Arial", 14))
    entrada_usuario.pack(pady=8)

    criar_label(frame, "Senha")
    entrada_senha = tk.Entry(frame, show="*", font=("Arial", 14))
    entrada_senha.pack(pady=8)

    def confirmar_login(event=None):
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()

        if validar_usuario(usuario, senha):
            messagebox.showinfo("Login", "Login realizado com sucesso!")
            abrir_controle(usuario)
        else:
            messagebox.showerror("Erro", "Nome de usuario ou senha incorretos!")

    tk.Button(
        frame,
        text="ENTRAR",
        font=("Arial", 13, "bold"),
        width=15,
        command=confirmar_login
    ).pack(pady=20)

    tk.Button(
        frame,
        text="VOLTAR",
        font=("Arial", 12),
        width=15,
        command=tela_menu
    ).pack()

    entrada_senha.bind("<Return>", confirmar_login)
    entrada_usuario.focus_set()


def mostrar_usuarios():
    usuarios = listar_usuarios()

    if not usuarios:
        messagebox.showinfo("Usuarios", "Nenhum usuario cadastrado ainda.")
        return

    texto = "Usuarios cadastrados:\n\n" + "\n".join(f"- {usuario}" for usuario in usuarios)
    messagebox.showinfo("Usuarios", texto)


def abrir_controle(usuario_logado):
    frame = limpar_tela()
    criar_titulo(frame, "CONTROLE DO ROBO")

    criar_label(frame, f"Usuario logado: {usuario_logado}", 12)

    texto = tk.Label(
        frame,
        text="Use W A S D",
        font=("Arial", 18),
        bg="#18669A",
        fg="white"
    )
    texto.pack(pady=20)

    comandos = tk.Label(
        frame,
        text="W = Frente\nS = Re\nA = Esquerda\nD = Direita",
        font=("Arial", 18),
        bg="#18669A",
        fg="white"
    )
    comandos.pack(pady=25)

    aviso = tk.Label(
        frame,
        text="Ao soltar a tecla o robo para",
        font=("Arial", 12),
        bg="#18669A",
        fg="white"
    )
    aviso.pack(pady=15)

    tk.Button(
        frame,
        text="SAIR DO CONTROLE",
        font=("Arial", 12, "bold"),
        width=18,
        command=tela_menu
    ).pack(pady=10)

    root.bind("<KeyPress>", apertou)
    root.bind("<KeyRelease>", soltou)
    root.focus_set()


def apertou(event):
    tecla = event.keysym.lower()

    if tecla == "w":
        enviar("frente")
    elif tecla == "s":
        enviar("tras")
    elif tecla == "a":
        enviar("esquerda")
    elif tecla == "d":
        enviar("direita")


def soltou(event):
    tecla = event.keysym.lower()

    if tecla in ["w", "a", "s", "d"]:
        enviar("parar")


if __name__ == "__main__":
    tela_menu()
    root.mainloop()
