# Gerenciador de Lixeira Reciclável

Este projeto está sendo desenvovido para o trabalho da Fatec São Roque para disciplina de IOT e tem objetivo de ser capaz gerenciar os níveis das lixeiras em tempo real em diversos pontos da cidade, seja por meio da sinalização por um morador ou ainda por meio de sensores que ESP32 que são integrados ao sistema.

A empresa pode gerenciar a coleta de lixos recicláveis de uma maneira mais eficiente, se programando antecipadamente, realizando a coleta em pontos 
estratégicos. Também pode reduzir os custos traçando a melhor rota antecipadamente, coletando lixos recicláveis em pontos mais críticos. Pois o sistema será capaz de apresentar diversos dados que ajudam na tomada de decisão como, regiões com mais ou menos lixo.

Também tem objetivo de aprender e explorar um pouco mais a questão de projetar sistemas seguindo as melhores práticas no desenvolvimento de software, como a criação de componentes, serviços, gerenciamentos de estados dos componentes, aplicação de diretivas personalizadas, criação de APis, uso de websockets para informação em tempo real, trabalhar com microcontrolador ESP32 utilizando micropython e outros tópicos que poderão ser explorados ao longo do projeto.

## Funcionalidades já desenvolvidas

- Criação de grupos de lixeiras recicláveis
- Criação de lixeiras para coletas de papel, metal, vidro, orgânico.....
- Usuário pode informar niveis das lixeiras manualmente
- Usuário consegue acessar link através de QRCode gerado na tela para cada lixeira para informar status da lixeira.
- Empresa consegue visualizar grupos de lixeiras criados.
- Empresa consegue visualizar as lixeiras cadastradas por grupo
- Empresa consegue visualizar observações deixadas por cada usuário que informa o nivel da lixeiras, como também informação sobre coletas já realizadas.
- Empresa consegue visualizar se as sinalizações das lixeiras estão sendo informadas por uma pessoa, ou ainda por um dispositivo instalado nas lixeiras.
- Empresa consegue filtrar e visualizar grupos de lixeira por id_grupo, endereço(rua, bairro, cidade, estado ou cep), capacidades de cada lixeiras em litros ou ainda niveis de lixo que cada uma se encontra.
- Integração do sistema com microcontroladores ESP32 que envia dados para o sistema informando o nivel das lixeiras.
- Gráfico de acompanhamento dos niveis de lixo reciclável ao longo do tempo nas lixeiras.

## Futuras
- Ajustes


## Principais Tecnologias
- Vue.js
- Vuetify
- Python
- Micropython
- Microcontrolador ESP32


# Telas do projeto
- [![Tela acompanhamento dos niveis de lixeira reciclavel](https://github.com/joseguilherme96/sistema_gerenciador_lixeira_reciclavel/blob/f8fddfa8650bf7573296a4d1f46f303a74648278/src/assets/tela_acompanhamento_lixeiras_reciclaveis.png "Tela acompanhamento dos niveis de lixeira reciclavel")](https://github.com/joseguilherme96/sistema_gerenciador_lixeira_reciclavel/blob/f8fddfa8650bf7573296a4d1f46f303a74648278/src/assets/tela_acompanhamento_lixeiras_reciclaveis.png)

- [![Tela que mostra as atualizações dos niveis da lixeira sinalizadas pelos os usuários ou por microcontrolador](https://github.com/joseguilherme96/sistema_gerenciador_lixeira_reciclavel/blob/25f74f8c33a1e9f190f744726051cedc35b58d23/src/assets/atualizacao_lixeira.png "Tela que mostra as atualizações dos niveis da lixeira sinalizadas pelos os usuários ou por microcontrolador")](https://github.com/joseguilherme96/sistema_gerenciador_lixeira_reciclavel/blob/25f74f8c33a1e9f190f744726051cedc35b58d23/src/assets/atualizacao_lixeira.png)

- [![Tela utilizada pelo usuário para informar o nivel da lixeira](https://github.com/joseguilherme96/sistema_gerenciador_lixeira_reciclavel/blob/4757e4a78eb1e3e1431d8539587ac248c5fdc1c8/src/assets/tela_de_atualizacao_nivel_lixeira.png "Tela utilizada pelo usuário para informar o nivel da lixeira")](https://github.com/joseguilherme96/sistema_gerenciador_lixeira_reciclavel/blob/4757e4a78eb1e3e1431d8539587ac248c5fdc1c8/src/assets/tela_de_atualizacao_nivel_lixeira.png)



- [![Tela de apresentação dos niveis de lixo reciclável de forma gráfica nas lixeiras ao longo do tempo](https://github.com/joseguilherme96/sistema_gerenciador_lixeira_reciclavel/blob/main/src/assets/grafico_de_acompanhamento_do_nivel_da_lixeira_reciclavel.png "Tela de apresentação dos niveis de lixo reciclável de forma gráfica nas lixeiras ao longo do tempo")](https://github.com/joseguilherme96/sistema_gerenciador_lixeira_reciclavel/blob/main/src/assets/grafico_de_acompanhamento_do_nivel_da_lixeira_reciclavel.png)

## Configuração do projeto  

## Intalação das depêndencias

```sh
npm install
```

### Execução

```sh
npm run dev
```

## Instalação

Instale as dependencias com o seguinte comando :

```sh
    pip install -r requirements.txt

```

### Ative o ambiente virtual

Ativar ambiente virtual na pasta src/backend/.venv/scripts/activate

### Execute o banco de dados

Dentro da pasta app. Execute :

```sh
    flask db init

```

### Execute o servidor Flask

Ainda dentro da pasta app. Execute :

```sh
    flask --app app run

```

### Incie o servidor json-server

Incie o servidor json-server para carregar os estados automaticamente dentro dos forms de pesquisa e cadastro de grupo lixeira. Está é a ultima api que ainda está mockada, mas em breve será criada definitivamente com python. Assim com já foram feitas as outras APIs que já foram migradas.

```sh

    npx json-server src/backend/db.json

```

