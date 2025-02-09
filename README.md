# Gerenciador de Lixeira Reciclável

Este projeto está sendo desenvovido e tem objetivo de ser capaz gerenciar os niveis das lixeiras em tempo real em diversos pontos da cidade, seja por meio da sinalização por um morador ou ainda por meio de sensores que serão integrados ao sistema.

Os dados ainda estão mockados e servirão como base para construção da API definitiva que será desenvolvido em python posteriormente.

# Foto da primeira tela inicial do projeto
- [![Tela acompanhamento dos niveis de lixeira reciclavel](src/assets/public/imagens/tela_acompanhamento_lixeiras_reciclaveis.png "Logo, framework vue.js")](src/assets/public/imagens/tela_acompanhamento_lixeiras_reciclaveis.png)

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Configuração do projeto

## Intalação das depêndencias

```sh
npm install
```

### Execução

```sh
npm run dev
```

### Iniciar servivor json-server

Como os dados ainda estão mockados, é necessário a execução do servidor json com o seguinte comando abaixo.

```sh

npx json-server src/backend/db.json5

```