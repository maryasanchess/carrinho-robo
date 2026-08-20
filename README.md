# 🤖 Carrinho Robô

Projeto de carrinho robô controlado remotamente: um **ESP32** recebe
comandos de movimento (frente, ré, esquerda, direita, parar) via Wi-Fi, e
uma interface em Python (com login) envia esses comandos a partir do
teclado do computador.

Desenvolvido no 1º semestre da faculdade de Análise e Desenvolvimento de
Sistemas.

## 🔧 Como funciona

```
Teclado (W A S D) → Interface Python (Tkinter/Streamlit) → HTTP → ESP32 → Motores
```

- O **ESP32** (`arduino/carrinho-robo.ino`) sobe um servidor Wi-Fi com IP
  fixo e escuta comandos de um caractere (`w`, `s`, `a`, `d`, `p`).
- As **interfaces em Python** (`python/`) mostram uma tela de login e,
  depois de autenticado, capturam as teclas pressionadas e mandam o
  comando correspondente pro ESP32.

## 📁 Estrutura

- `arduino/carrinho-robo.ino` — firmware do ESP32 (servidor Wi-Fi que recebe os comandos)
- `python/main.py` — primeira versão da interface (Tkinter)
- `python/teste3.py` — segunda versão/teste da interface (Tkinter)
- `python/controle_login.py` — versão com cadastro de usuário (Tkinter)
- `python/app.py` — versão em Streamlit, com botões na tela em vez de só teclado

> São várias versões da mesma ideia, feitas durante o desenvolvimento —
> mantidas aqui como registro da evolução do projeto.

## ⚙️ Configuração

No `arduino/carrinho-robo.ino`, preencha `ssid` e `password` com os dados
da sua própria rede Wi-Fi antes de gravar no ESP32 (nunca suba
credenciais reais pro repositório).

O login usado nas interfaces Python é fixo (`admin` / `1234`) — é só uma
tela de demonstração do projeto, não um sistema de autenticação real.

## 🛠️ Tecnologias

![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![ESP32](https://img.shields.io/badge/ESP32-E7352C?style=for-the-badge&logo=espressif&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
