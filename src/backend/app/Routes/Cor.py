from flask import request, jsonify, Blueprint
from Models.CorModel import Cor


cor = Blueprint('cor',__name__)


@cor.route('/cadastrar_cor',methods=['POST'])
def insert():

    try:


        data = request.get_json()

        if not data.get('nome'):

            return jsonify({'message':'Por favor informe o nome de uma cor !'})
        
        cor = Cor(

            nome= data['nome']


        ) 

        dados_inseridos = Cor.insert(cor)

        return jsonify({'message':'A cor foi inserida com sucesso !','dados':dados_inseridos})
    
    except Exception as e:

        return jsonify({'message':f'${str(e)}','status':'error'})

@cor.route('/cor',methods=['POST'])
def select_cor():

    try:
        data = request.get_json()

        where = []
        cores = []

        if data.get('cor_id'):

            where.append({"cor_id":data['cor_id']})

        if data.get('nome'):

            where.append({"nome":data['nome']})

        dados_encontrados = Cor.select(where)

        if(len(dados_encontrados) == 0):

            return jsonify({'message':'Nenhuma cor encontrada !'}),404

        for cor in Cor.select(where):

            encontrado = {

                "cor_id" : cor.Cor.id_cor,
                "nome": cor.Cor.nome,
                
            }

            cores.append(encontrado)

        
        
        return jsonify(cores)

    except Exception as e:

        return jsonify({'message':f'${str(e)}'}),500



    