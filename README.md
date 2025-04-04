"""
# 🏥 Automação de Login e Busca de Paciente - SulAmérica

Este script Python automatiza o login no portal da SulAmérica para prestadores de serviço e realiza uma busca de paciente a partir do número da carteira de saúde, utilizando apenas a biblioteca `requests`.

## 📌 Objetivo

Automatizar o processo de:

1. Realizar login no portal SulAmérica.
2. Navegar até a área de consulta.
3. Buscar um paciente pelo número da carteira.

## ⚙️ Tecnologias Utilizadas

- Python 3.x
- requests
- BeautifulSoup (bs4)

## 🚀 Como Executar

1. Instale as dependências:
   pip install requests beautifulsoup4

2. Execute o script:
   python login_sulamerica.py

## 🔑 Credenciais de Teste

| Campo              | Valor                |
|-------------------|----------------------|
| Código Referenciado | 100000009361        |
| Usuário            | master               |
| Senha              | 837543               |


## 🔍 Busca de Paciente

Número da Carteira: 55788888485177660015
