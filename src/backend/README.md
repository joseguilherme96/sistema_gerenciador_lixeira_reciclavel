## Backend Servidor Flask APIs

Foi desenvolvido API em Flask para recebimento de dados do usuário que usa o sistema, quanto dados enviados automaticamente por Microcontroladores ESP32.

### Principais Recursos que API oferece

- Validação dos dados
- Persistência no banco de dados com Flask-SQLAchemy
- Controle de Transações com os principais comandos BEGIN, COMMIT e ROLLBACK.
- Acompanhamento de atividade dos Microcontroladores ESP32
- Gravação de logs gerados pelos Microcontroladores ESP32 em arquivo.
- Retorno direcionado com principais Códigos de status de Respostas HTTP 400, 404, 405, 415 e 500.
- Controle de versão do Banco de Dados com Flask-Migrate
- API WEBSOCKET para comunicação em tempo real com Flask-SocketIO


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


