import tkinter as tk
from tkinter import messagebox
import requests

# IP do ESP32
ip_esp32 = "http://10.10.0.2"

# Login
usuario_correto = "admin"
senha_correta = "1234"


# Função para enviar comando
def enviar(comando):

    try:
        requests.get(ip_esp32 + "/" + comando)
        print("Comando:", comando)

    except:
        print("Erro ao conectar")


# Quando apertar tecla
def apertou(acoes):

    tecla = acoes.keysym

    if tecla == "w":
        enviar("frente")

    if tecla == "s":
        enviar("tras")

    if tecla == "a":
        enviar("esquerda")

    if tecla == "d":
        enviar("direita")


# Quando soltar tecla
def soltou(acoes):

    enviar("parar")


# Abrir tela do controle
def abrir_controle():

    tela_login.destroy()

    tela = tk.Tk()

    tela.title("Controle")
    tela.geometry("500x400")
    tela.configure(bg="#185B9A")

    titulo = tk.Label(
        tela,
        text="CONTROLE DO ROBÔ",
        font=("Arial", 22, "bold"),
        bg="#185B9A",
        fg="white"
    )

    titulo.pack(pady=30)

    texto = tk.Label(
        tela,
        text="Use W A S D",
        font=("Arial", 18),
        bg="#185B9A",
        fg="white"
    )

    texto.pack(pady=20)

    comandos = tk.Label(
        tela,
        text="W = Frente\nS = Ré\nA = Esquerda\nD = Direita",
        font=("Arial", 18),
        bg="#185B9A",
        fg="white"
    )

    comandos.pack(pady=30)

    aviso = tk.Label(
        tela,
        text="Ao soltar a tecla o robô para",
        font=("Arial", 12),
        bg="#185B9A",
        fg="white"
    )

    aviso.pack(pady=20)

    # Detectar teclado
    tela.bind("<KeyPress>", apertou)
    tela.bind("<KeyRelease>", soltou)

    tela.mainloop()


# Validar login
def login():

    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario == usuario_correto and senha == senha_correta:

        abrir_controle()

    else:

        messagebox.showerror(
            "Erro",
            "Login incorreto"
        )


# Tela de login
tela_login = tk.Tk()

tela_login.title("Login")
tela_login.geometry("400x350")
tela_login.configure(bg="#185B9A")

# Título
titulo = tk.Label(
    tela_login,
    text="LOGIN DO ROBÔ",
    font=("Arial", 22, "bold"),
    bg="#185B9A",
    fg="white"
)

titulo.pack(pady=30)

# Usuário
texto_usuario = tk.Label(
    tela_login,
    text="Usuário",
    font=("Arial", 14),
    bg="#185B9A",
    fg="white"
)

texto_usuario.pack()

entrada_usuario = tk.Entry(
    tela_login,
    font=("Arial", 14)
)

entrada_usuario.pack(pady=10)

# Senha
texto_senha = tk.Label(
    tela_login,
    text="Senha",
    font=("Arial", 14),
    bg="#185B9A",
    fg="white"
)

texto_senha.pack()

entrada_senha = tk.Entry(
    tela_login,
    show="*",
    font=("Arial", 14)
)

entrada_senha.pack(pady=10)

# Botão
botao = tk.Button(
    tela_login,
    text="ENTRAR",
    font=("Arial", 14, "bold"),
    width=15,
    command=login
)

botao.pack(pady=30)

tela_login.mainloop()