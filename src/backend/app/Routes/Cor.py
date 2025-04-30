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

        return jsonify({'message':f'${str(e)}'})

@cor.route('/cor',methods=['POST'])
def select_cor():

    try:
        data = request.get_json()

        where = []
        cor = []

        if data.get('cor_id'):

            where.append({"cor_id":data['cor_id']})

        if data.get('nome'):

            where.append({"nome":data['nome']})

        for cor in Cor.select(where):

            encontrado = {

                "cor_id" : cor.Cor.cor_id,
                "nome": cor.Cor.nome,
                
            }

            cor.append(encontrado)

        if(len(cor) == 0):

            return jsonify({'message':'Nenhuma cor encontrada !'}),404
        
        return jsonify(cor)

    except Exception as e:

        return jsonify({'message':f'${str(e)}'}),400



    