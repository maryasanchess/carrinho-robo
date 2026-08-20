# 🤖 Carrinho Robô

Projeto de carrinho robô controlado remotamente: um **ESP32** recebe
comandos de movimento (frente, ré, esquerda, direita, parar), e uma
interface em Python (com login) envia esses comandos a partir do teclado
do computador.

Desenvolvido no 1º semestre da faculdade de Análise e Desenvolvimento de
Sistemas.

Testamos a comunicação entre o computador e o ESP32 tanto por **Wi-Fi**
quanto por **Bluetooth** ao longo do desenvolvimento.

## 🗣️ Linguagens utilizadas

| Linguagem | Onde |
|---|---|
| **C++** | Firmware do ESP32 (`arduino/`), usando a API `WiFi.h` |
| **Python** | Todas as interfaces de controle (`python/`) — Tkinter, Streamlit e Pygame+sockets |

## 🔧 Como funciona

```
Teclado (W A S D) → Interface Python (Tkinter/Streamlit/Pygame) → Wi-Fi/Bluetooth → ESP32 → Motores
```

- O **ESP32** (`arduino/`) sobe um servidor e escuta comandos de um
  caractere (`w`, `s`, `a`, `d`, `p`).
- As **interfaces em Python** (`python/`) capturam as teclas pressionadas
  (ou cliques de botão) e mandam o comando correspondente pro ESP32.

## 📁 Estrutura

- `arduino/carrinho-robo.ino` — firmware principal do ESP32 (servidor que recebe os comandos e "aciona" os motores)
- `arduino/codigo-lan.ino` — versão anterior do firmware, mesma lógica, testada em outra rede
- `arduino/verifica-ip.ino` — sketch de diagnóstico, só pra checar se o ESP32 conectou e qual IP recebeu
- `python/main.py` — primeira versão da interface (Tkinter)
- `python/teste3.py` — segunda versão/teste da interface (Tkinter)
- `python/controle_login.py` — versão com cadastro de usuário (Tkinter)
- `python/app.py` — versão em Streamlit, com botões na tela em vez de só teclado
- `python/code_drive/` — versão alternativa usando Pygame (captura de tecla) + socket TCP direto, com painel Streamlit pra abrir o controle (baseado em [lfusca/code_drive](https://github.com/lfusca/code_drive))

> São várias versões da mesma ideia, feitas durante o desenvolvimento —
> mantidas aqui como registro da evolução do projeto.

## ⚙️ Configuração

Nos arquivos `.ino` em `arduino/`, preencha `ssid` e `password` com os
dados da sua própria rede antes de gravar no ESP32 (nunca suba
credenciais reais pro repositório).

O login usado nas interfaces Python é fixo (`admin` / `1234`) — é só uma
tela de demonstração do projeto, não um sistema de autenticação real.

## 🛠️ Tecnologias

![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![ESP32](https://img.shields.io/badge/ESP32-E7352C?style=for-the-badge&logo=espressif&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Bluetooth](https://img.shields.io/badge/Bluetooth-0082FC?style=for-the-badge&logo=bluetooth&logoColor=white)
