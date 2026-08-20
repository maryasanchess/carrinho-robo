# app.py
import streamlit as st
import requests


ESP32_IP = "http://10.10.0.2"  


USUARIO = "admin"
SENHA = "1234"


if "logado" not in st.session_state:
    st.session_state.logado = False


def enviar_comando(comando):
    try:
        requests.get(f"{ESP32_IP}/{comando}")
    except:
        st.error("Erro ao conectar no ESP32")



if not st.session_state.logado:

    st.set_page_config(page_title="Login Robô", layout="centered")

    st.markdown(
        """
        <h1 style='text-align:center;color:#7B2CBF;'>
        🤖 LOGIN DO ROBÔ
        </h1>
        """,
        unsafe_allow_html=True
    )

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):

        if usuario == USUARIO and senha == SENHA:
            st.session_state.logado = True
            st.rerun()

        else:
            st.error("Usuário ou senha incorretos")


else:

    st.set_page_config(page_title="Controle do Robô", layout="centered")

    st.markdown(
        """
        <h1 style='text-align:center;color:#7B2CBF;'>
        🎮 CONTROLE DO CARRINHO ROBÔ
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.write("Use os botões para controlar o robô")

    col1, col2, col3 = st.columns(3)

    with col2:
        if st.button("W ⬆ Frente"):
            enviar_comando("frente")

    col4, col5, col6 = st.columns(3)

    with col4:
        if st.button("A ⬅ Esquerda"):
            enviar_comando("esquerda")

    with col5:
        if st.button("PARAR 🛑"):
            enviar_comando("parar")

    with col6:
        if st.button("D ➡ Direita"):
            enviar_comando("direita")

    col7, col8, col9 = st.columns(3)

    with col8:
        if st.button("S ⬇ Ré"):
            enviar_comando("tras")

    st.divider()

    if st.button("Sair"):
        st.session_state.logado = False
        st.rerun()

  

    st.markdown(
        """
        <script>
        document.addEventListener('keydown', function(event) {

            fetch('/?key=' + event.key);

        });

        document.addEventListener('keyup', function(event) {

            fetch('/?key=parar');

        });
        </script>
        """,
        unsafe_allow_html=True
    )

    query = st.query_params

    if "key" in query:

        tecla = query["key"]

        if tecla == "w":
            enviar_comando("frente")

        elif tecla == "s":
            enviar_comando("tras")

        elif tecla == "a":
            enviar_comando("esquerda")

        elif tecla == "d":
            enviar_comando("direita")

        elif tecla == "parar":
            enviar_comando("parar")