# Gerenciador de Lixeira Reciclável

Este projeto está sendo desenvolvido e tem objetivo de ser capaz gerenciar os niveis das lixeiras em tempo real em diversos pontos da cidade, seja por meio da sinalização por um morador ou ainda por meio de sensores que serão integrados ao sistema.

Também tem objetivo de aprender e explorar um pouco mais a questão de projetar sistemas seguindo as melhores práticas no desenvolvimento de software, como a criação de componentes, serviços, gerenciamentos de estados dos componentes, aplicação de diretivas personalizadas, uso de websockets para informação em tempo real e outros tópicos que poderão ser explorados ao longo do projeto.

Os dados ainda apresentados estão mockados e apenas servirão como base para construção da API definitiva que será desenvolvido em python posteriormente.

# Telas do projeto
- [![Tela acompanhamento dos niveis de lixeira reciclavel](https://github.com/joseguilherme96/sistema_gerenciador_lixeira_reciclavel/blob/f8fddfa8650bf7573296a4d1f46f303a74648278/src/assets/tela_acompanhamento_lixeiras_reciclaveis.png "Tela acompanhamento dos niveis de lixeira reciclavel")](https://github.com/joseguilherme96/sistema_gerenciador_lixeira_reciclavel/blob/f8fddfa8650bf7573296a4d1f46f303a74648278/src/assets/tela_acompanhamento_lixeiras_reciclaveis.png)

- [![Tela que mostra as atualizações dos niveis da lixeira sinalizadas pelos os usuários ou por microcontrolador](https://github.com/joseguilherme96/sistema_gerenciador_lixeira_reciclavel/blob/25f74f8c33a1e9f190f744726051cedc35b58d23/src/assets/atualizacao_lixeira.png "Tela que mostra as atualizações dos niveis da lixeira sinalizadas pelos os usuários ou por microcontrolador")](https://github.com/joseguilherme96/sistema_gerenciador_lixeira_reciclavel/blob/25f74f8c33a1e9f190f744726051cedc35b58d23/src/assets/atualizacao_lixeira.png)

## Configuração do projeto  

## Intalação das depêndencias

```sh
npm install
```

### Execução

```sh
npm run dev
```

### Iniciar servidor json-server

Como os dados ainda estão mockados, é necessário a execução do servidor json com o seguinte comando abaixo.

```sh

npx json-server src/backend/db.json

```