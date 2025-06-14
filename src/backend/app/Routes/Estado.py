

from flask import Blueprint, jsonify, request
estado = Blueprint('estados',__name__)

@estado.route('/estados',methods=['GET'])
def estados():

    estados = [
    {
      "id": "1",
      "estado": "Acre",
      "sigla": "AC"
    },
    {
      "id": "2",
      "estado": "Alagoas",
      "sigla": "AL"
    },
    {
      "id": "3",
      "estado": "Amapá",
      "sigla": "AP"
    },
    {
      "id": "4",
      "estado": "Amazonas",
      "sigla": "AM"
    },
    {
      "id": "5",
      "estado": "Bahia",
      "sigla": "BA"
    },
    {
      "id": "6",
      "estado": "Ceará",
      "sigla": "CE"
    },
    {
      "id": "7",
      "estado": "Distrito Federal",
      "sigla": "DF"
    },
    {
      "id": "8",
      "estado": "Espírito Santo",
      "sigla": "ES"
    },
    {
      "id": "9",
      "estado": "Goiás",
      "sigla": "GO"
    },
    {
      "id": "10",
      "estado": "Maranhão",
      "sigla": "MA"
    },
    {
      "id": "11",
      "estado": "Mato Grosso",
      "sigla": "MT"
    },
    {
      "id": "12",
      "estado": "Mato Grosso do Sul",
      "sigla": "MS"
    },
    {
      "id": "13",
      "estado": "Minas Gerais",
      "sigla": "MG"
    },
    {
      "id": "14",
      "estado": "Pará",
      "sigla": "PA"
    },
    {
      "id": "15",
      "estado": "Paraíba",
      "sigla": "PB"
    },
    {
      "id": "16",
      "estado": "Paraná",
      "sigla": "PR"
    },
    {
      "id": "17",
      "estado": "Pernambuco",
      "sigla": "PE"
    },
    {
      "id": "18",
      "estado": "Piauí",
      "sigla": "PI"
    },
    {
      "id": "19",
      "estado": "Rio de Janeiro",
      "sigla": "RJ"
    },
    {
      "id": "20",
      "estado": "Rio Grande do Norte",
      "sigla": "RN"
    },
    {
      "id": "21",
      "estado": "Rio Grande do Sul",
      "sigla": "RS"
    },
    {
      "id": "22",
      "estado": "Rondônia",
      "sigla": "RO"
    },
    {
      "id": "23",
      "estado": "Roraima",
      "sigla": "RR"
    },
    {
      "id": "24",
      "estado": "Santa Catarina",
      "sigla": "SC"
    },
    {
      "id": "25",
      "estado": "São Paulo",
      "sigla": "SP"
    },
    {
      "id": "26",
      "estado": "Sergipe",
      "sigla": "SE"
    },
    {
      "id": "27",
      "estado": "Tocantins",
      "sigla": "TO"
    }
  ]

    return jsonify(estados),200
    

