## Backend Servidor Flask APIs

Foi desenvolvido API em Flask para recebimento de dados do usuário que usa o sistema, quanto dados enviados automaticamente por Microcontroladores ESP32.

### Principais Recursos que API oferece

- Validação dos dados
- APis Modulares com Blueprints
- Persistência no banco de dados com Flask-SQLAchemy
- Controle de Transações com os principais comandos BEGIN, COMMIT e ROLLBACK.
- Acompanhamento de atividade dos Microcontroladores ESP32
- Gravação de logs gerados pelos Microcontroladores ESP32 em arquivo.
- Retorno direcionado com principais Códigos de status de Respostas HTTP 400, 404, 405, 415 e 500.
- Controle de versão do Banco de Dados com Flask-Migrate
- API WEBSOCKET para comunicação em tempo real com Flask-SocketIO
- Proteção de rotas com Flask-JWT-Extended’s, criação e validação de tokens JWT.

## Rotas das APIs

O arquivo de importação das APIs se encontra-se na pasta [insomnia](insomnia/Insomnia_2025-07-27.yaml).
E abaixo rotas detalhadas com dados que são enviados, estão organizadas por grupos de APIs.

### Login

| Método |        URL       |
| ------ | ---------------- |
| POST   | `/login`         |
| POST   | `/validar_token` |

POST /login
```json
{
  "email": "default",
  "senha": "default"
}

```

POST /validar_token
```json
{
	
"usuario":"default",
"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc1MDU0NzM0OSwianRpIjoiMmQwZTNmYzQtODJhMy00MjliLWI2MzYtNzBmYTllNDRmMjc5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImRlZmF1bHQiLCJuYmYiOjE3NTA1NDczNDksImNzcmYiOiIwZDJmNzI3Zi1jMWQ3LTQ5MTUtOGE4Yi0zMDkxYTE5MTg0NGEiLCJleHAiOjE3NTA1NDc0MDl9.q5b3356kz2zyGBcvM3sut--u_M9onURH4hBfWdPTCLw"
	
}

```

### GrupoLixeira

| Método | URL                        |
| ------ | -------------------------- |
| POST   | `/grupo_lixeira`           |
| POST   | `/cadastrar_grupo_lixeira` |

POST /cadastrar_grupo_lixeira
```json
{
  "nome": "Grupo Y",
  "descricao": "Lixeiras para coleta de metais",
  "cep": "18909999",
  "endereco": "Avenida de Minas",
  "cidade": "Sorocaba",
  "bairro": "Jardim",
  "estado": "Minas Gerais"
}
```
### Lixeira

| Método | URL                        |
| ------ | -------------------------- |
| PUT    | `/atualizar_nivel_lixeira` |
| POST   | `/cadastrar_lixeira`       |
| POST   | `/get_lixeira`             |
| POST   | `/lixeira_grupo_lixeira`   |

PUT /atualizar_nivel_lixeira
```json
{
  "lixeira_id": 1,
  "nivel_lixeira": 20,
  "esta_aberta": true
}
```

POST /cadastrar_lixeira

```json
[
  {
    "tets": "ss",
    "mat_colet_id": 1,
    "grupo_lixeira_id": 1,
    "ponto_lixo_id": "5",
    "cor_id": 1,
    "descricao": "Lixeira 1",
    "capacidade": "100",
    "nivel_lixeira": "10",
    "observacao": ""
  }
]

```

### InformativoPontoLixo

| Método | URL                              |
| ------ | -------------------------------- |
| POST   | `/cadastrar_informativo_lixeira` |
| POST   | `/get_informativo_lixeira`       |

POST /cadastrar_informativo_lixeira
```json
{
  "ponto_lixo_id": "6",
  "informado_por_id": "1",
  "nivel_lixeira": 1,
  "observacao": "Lixeira começou a encher"
}

```

### PontoLixo

| Método | URL                     |
| ------ | ----------------------- |
| POST   | `/cadastrar_ponto_lixo` |
| POST   | `/ponto_lixo`           |

POST /cadastrar_ponto_lixo
```json
{
  
}
```
POST /ponto_lixo
```json
{
  "ponto_lixo_id": "",
  "data": "",
  "hora": ""
}
```


### MaterialColetado

| Método | URL                            |
| ------ | ------------------------------ |
| POST   | `/cadastrar_material_coletado` |
| POST   | `/material_coletado`           |

POST /cadastrar_material_coletado
```json
{
  "nome": "Metal"
}

```
### Cor

| Método | URL              |
| ------ | ---------------- |
| POST   | `/cor`           |
| POST   | `/cadastrar_cor` |

POST /cor
```json
{
	
	"cor_id":"",
	"nome":""
	
}

```
POST /cadastrar_cor
```json
{
  "nome": ""
}

```

### GrupoLixeiraPontoLixoLixeira

| Método | URL                                           |
| ------ | --------------------------------------------- |
| POST   | `/cadastrar_grupo_lixeira_ponto_lixo_lixeira` |

POST /cadastrar_grupo_lixeira_ponto_lixo_lixeira
```json
{
    "cep": "181200000",
    "endereco": "Rua Figueiredo Nº 25",
    "cidade": "Mairinque",
    "estado": "SP",
    "descricao": "",
    "nome": "ddddddddddd",
    "bairro": "sss",
    "lixeiras": [
        {
        "material": "Plástico",
        "descricao": "",
        "capacidade": "10",
        "cor": "Verde",
        "observacao": "",
        "nivel_lixeira": "1",
        "cor_id": 1,
        "mat_colet_id": 2
        },
        {
        "material": "Metal",
        "descricao": "",
        "capacidade": "10",
        "cor": "Verde",
        "observacao": "",
        "nivel_lixeira": "25",
        "cor_id": 1,
        "mat_colet_id": 1
        }
    ],
}
````


### Logs

| Método | URL                    |
| ------ | ---------------------- |
| POST   | `/cadastrar_log_esp32` |

POST /cadastrar_log_esp32
```json
[
  {
    "message": "-----------------",
    "label": "SUCCESS",
    "time_execucao": "12"
  },
  {
    "message": "Iniciando loop !",
    "label": "SUCCESS",
    "time_execucao": "12"
  },
  {
    "message": "Aguardando conexão...",
    "label": "",
    "time_execucao": "1"
  }
]

```

### Estado

| Método | URL        |
| ------ | ---------- |
| GET    | `/estados` |


## Instalação

### Versão Python utilizada

- Python >= 3.10.11 

### Configure o arquivo .env na pasta backend

Na pasta src/backend abra o arquivo .env, você verá as configurações abaixo.

```sh

# BASES URL QUE O FRONT PODE ESTAR SENDO EXECUTADO
    
VITE_APP_BASE_URL_LOCAL = 'http://localhost:5173'
VITE_APP_BASE_URL_NETWORK1 = 'http://192.168.1.13:5173'
VITE_APP_BASE_URL_NETWORK2 = 'http://192.168.43.243:5173'


ORIGENS_PERMITIDAS = ${VITE_APP_BASE_URL_LOCAL},${VITE_APP_BASE_URL_NETWORK1},${VITE_APP_BASE_URL_NETWORK2}

```

Elas mudam de acordo com a base url que o app(frontend) está sendo ou será executado. Reatribua os valores baseados nas possiveis bases url que seu front possa estar sendo executado. Assim você estará autorizando que as origens onde o app está sendo executado sejam permitidas a consumir as APIs criadas em Flask.

### Instalação de dependências :

Dentro da pasta backend. Instale as dependências usando o comando abaixo, para que o servidor flask possa ser executado corretamente.

```sh

    pip install -r requirements.txt

```

### Ative o ambiente virtual

Ative o ambiente virtual na pasta src/backend/.venv/scripts/activate usando o seguinte comando dentro da pasta backend

```sh

    .venv\scripts\activate

```

### Inicie o banco de dados

Partindo da raiz do projeto, abra a pasta src/backend/app e inicie o banco de dados.

```sh

    cd src/backend/app

    flask db init

```

### Inicie o servidor Flask

Ainda dentro da pasta app. Execute o comando abaixo para iniciar o servidor flask.

```sh

    python app.py

```


