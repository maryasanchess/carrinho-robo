# ============================================================
# menu.py — Painel web de controle do Rover
# Interface criada com Streamlit que permite abrir o controle
# gráfico (controle.py) com um clique de botão
# ============================================================

import streamlit as st   # Biblioteca para criar interfaces web simples
import subprocess        # Módulo para abrir processos externos do sistema

# Define o título exibido no topo da página web
st.title("🚗 Rover")

# Exibe um botão na interface; quando clicado, retorna True
if st.button("Abrir Controle"):

    # Abre o arquivo controle.py em um processo separado,
    # sem bloquear o painel web (Popen = execução em paralelo)
    subprocess.Popen(["python", "controle.py"])