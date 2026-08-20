import tkinter as tk
from tkinter import messagebox
import requests


ESP32_IP = "http://10.10.0.2"


USUARIO = "admin"
SENHA = "1234"


def enviar_comando(comando):

    try:
        requests.get(f"{ESP32_IP}/{comando}")
        print(f"Comando enviado: {comando}")

    except:
        print("Erro ao conectar no ESP32")



def tecla_pressionada(event):

    tecla = event.keysym.lower()

    if tecla == "w":
        enviar_comando("frente")

    elif tecla == "s":
        enviar_comando("tras")

    elif tecla == "a":
        enviar_comando("esquerda")

    elif tecla == "d":
        enviar_comando("direita")



def tecla_solta(event):

    enviar_comando("parar")


# =========================
# ABRIR TELA DE CONTROLE
# =========================
def abrir_controle():

    janela_login.destroy()

    global janela

    janela = tk.Tk()

    janela.title("Controle do Carrinho Robô")
    janela.geometry("500x400")
    janela.configure(bg="#18669A")

    titulo = tk.Label(
        janela,
        text="CONTROLE DO ROBÔ",
        font=("Arial", 24, "bold"),
        bg="#18669A",
        fg="white"
    )

    titulo.pack(pady=30)

    instrucoes = tk.Label(
        janela,
        text="Use as teclas W A S D",
        font=("Arial", 16),
        bg="#18669A",
        fg="white"
    )

    instrucoes.pack(pady=10)

    comandos = tk.Label(
        janela,
        text="W = Frente\nS = Ré\nA = Esquerda\nD = Direita",
        font=("Arial", 18, "bold"),
        bg="#18669A",
        fg="white"
    )

    comandos.pack(pady=40)

    aviso = tk.Label(
        janela,
        text="Ao soltar a tecla o carrinho para",
        font=("Arial", 12),
        bg="#18669A",
        fg="white"
    )

    aviso.pack(pady=10)

    # EVENTOS DAS TECLAS
    janela.bind("<KeyPress>", tecla_pressionada)
    janela.bind("<KeyRelease>", tecla_solta)

    janela.mainloop()



def validar_login():

    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario == USUARIO and senha == SENHA:

        abrir_controle()

    else:

        messagebox.showerror(
            "Erro",
            "Usuário ou senha incorretos"
        )



janela_login = tk.Tk()

janela_login.title("Login")
janela_login.geometry("400x350")
janela_login.configure(bg="#18669A")

# TÍTULO
titulo_login = tk.Label(
    janela_login,
    text="LOGIN DO ROBÔ",
    font=("Arial", 24, "bold"),
    bg="#18669A",
    fg="white"
)

titulo_login.pack(pady=30)

# USUÁRIO
label_usuario = tk.Label(
    janela_login,
    text="Usuário",
    font=("Arial", 14),
    bg="#18669A",
    fg="white"
)

label_usuario.pack()

entrada_usuario = tk.Entry(
    janela_login,
    font=("Arial", 14)
)

entrada_usuario.pack(pady=10)

# SENHA
label_senha = tk.Label(
    janela_login,
    text="Senha",
    font=("Arial", 14),
    bg="#18669A",
    fg="white"
)

label_senha.pack()

entrada_senha = tk.Entry(
    janela_login,
    show="*",
    font=("Arial", 14)
)

entrada_senha.pack(pady=10)

# BOTÃO LOGIN
botao_login = tk.Button(
    janela_login,
    text="ENTRAR",
    font=("Arial", 14, "bold"),
    bg="white",
    fg="#77C4F7",
    width=15,
    command=validar_login
)

botao_login.pack(pady=30)

janela_login.mainloop()