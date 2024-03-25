# Coleta de dados INFO B2B Remanejamento + token de autorização

## Sobre o projeto

- Coleta de dados para INFO B2B para remanejamento de equipamentos

### Pré-Requisitos

É necessário ter instalado corretamente em seu computador:

- Python 3.8+
- Instalar o certificado ca.crt no Chrome para o seleniumwire

### Instalação

Siga o passo a passo para instalar a aplicação:

1. Clone o repositório abrindo o Git Bash:
```bash
git clone https://github.com/Btime/collect_data_infob2b.git
```

2. Crie um Ambiente Virtual (venv) e ative:
```bash
Windows: python -m venv venv
         venv/scripts/activate
```

3. Instale as dependências necessárias após ativar a venv:
```bash
pip install -r requirements.txt
```

4. Inicie o arquivo run.py (esteja com a pasta raiz do projeto aberto)
```bash
python run.py
```

### Dependências

Lista de dependências do projeto:
```bash
attrs==23.2.0
blinker==1.7.0
Brotli==1.1.0
certifi==2024.2.2
cffi==1.16.0
charset-normalizer==3.3.2
cryptography==42.0.5
h11==0.14.0
h2==4.1.0
hpack==4.0.0
hyperframe==6.0.1
idna==3.6
kaitaistruct==0.10
outcome==1.3.0.post0
pyasn1==0.5.1
pycparser==2.21
pydivert==2.1.0
pyOpenSSL==24.1.0
pyparsing==3.1.2
PySocks==1.7.1
python-dotenv==1.0.1
requests==2.31.0
selenium==4.18.1
selenium-wire==5.1.0
setuptools==69.2.0
sniffio==1.3.1
sortedcontainers==2.4.0
trio==0.25.0
trio-websocket==0.11.1
typing_extensions==4.10.0
urllib3==2.2.1
wsproto==1.2.0
zstandard==0.22.0
```

## Instalando certificado ca.crt

1. Abra o Google Chrome
2. Definições
3. Privacidade e segurança
4. Gerir certificados
5. Importar...
6. Avançar e selecione o ca.crt
7. Selecione a opção "Colocar todos os certificados no repositório a seguir
8. Clique em procurar e selecione "Autoridade de Certificação Raiz Confiável"
9. Conclua a instalação

## Uso

Lembre-se de estar com o acesso correto no ".env"
Se não houver o arquivo .json com o token necessário para acessar as requisições o bot coletará automaticamente com Selenium.
Se o token de autorização estiver expirado e retornar unauthorized ou authorization expired no terminal o bot coletará o novo token automaticamente.

OBS: Em fase de testes. Ainda contém captcha no login, necessitando de interação no terminal e preenchimento manual do mesmo.