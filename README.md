# VERACODE_API_Sample

# Veracode Python HMAC Example

Exemplos simples de como obter resultados das APIs Rest da VERACODE.

## Setup

Clono o repositório:

    git clone https://github.com/afernandooliveira/VERACODE_API_Sample.git

Instale as dependências:

    cd VERACODE_API_Sample
    pip install -r requirements.txt

Salve as suas credencias de API Veracode em `~/.veracode/credentials`

    [default]
    veracode_api_key_id = <YOUR_API_KEY_ID>
    veracode_api_key_secret = <YOUR_API_KEY_SECRET>

## Run

Se você salvou ou exportou as suas credenciais então pode executar:

    python3 Identity_API/user/self/api_self.py
    
Também pode-se exportar em variáveis de ambiente as suas API Credentials:

    export VERACODE_API_KEY_ID=<YOUR_API_KEY_ID>
    export VERACODE_API_KEY_SECRET=<YOUR_API_KEY_SECRET>
    python3 Identity_API/user/self/api_self.py