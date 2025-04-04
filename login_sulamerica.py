import requests
from bs4 import BeautifulSoup

# Criar uma sessão persistente
session = requests.Session()

# URLS DO SISTEMA
URL_LOGIN = "https://saude.sulamericaseguros.com.br/prestador/login/"
URL_BUSCA_PACIENTE = "https://saude.sulamericaseguros.com.br/prestador/servicos-medicos/contas-medicas/faturamento-tiss-3/faturamento/guia-de-consulta/"

#CREDENCIAIS
payload = {
    "code": "100000009361",
    "user": "master",
    "senha": "837543"
}

# HTML DA PÁGINA DE LOGIN PARA COLETAR TOKENS
response = session.get(URL_LOGIN)
soup = BeautifulSoup(response.text, "html.parser")


#CAMPOS OCULTOS NECESSÁRIOS PARA O LOGIN
for hidden_input in soup.find_all("input", type="hidden"):
    name = hidden_input.get("name")
    value = hidden_input.get("value", "")
    if name:
        payload[name] = value

#CABEÇALHOS PARA EVITAR DETECÇÃO
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": URL_LOGIN
}

#LOGIN
login_response = session.post(URL_LOGIN, data=payload, headers=headers)

#VERIFICAR SE O LOGIN FOI BEM-SUCEDIDO
if "Bem-vindo" in login_response.text or login_response.status_code == 200:
    print("Login realizado com sucesso!")
else:
    print("Falha no login. Verifique as credenciais ou proteções do site.")
    print("Resposta do site:", login_response.text[:500])
    exit()

#BUSCAR PACIENTE
params = {
    "numero_carteira": "55788888485177660015"
}

#REQUISIÇÃO DE CONSULTA
response = session.get(URL_BUSCA_PACIENTE, params=params, headers=headers)

if "Paciente encontrado" in response.text:
    print("Paciente localizado!")
    print(response.text[:500])  
else:
    print("Paciente não encontrado ou erro na consulta.")
    print(response.text[:1000])  