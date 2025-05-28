from flask import jsonify, request, Blueprint
from Models.InformativoLixeiraModel import InformativoLixeira
from Routes.Socketio import socketio
from Routes.SocketioEnviarObservacao import enviar_observacao_lixeira
from datetime import datetime

informativo_lixeira = Blueprint('informativo_lixeira',__name__)

@informativo_lixeira.route('/get_informativo_lixeira',methods=['POST'])
def select_informativo_lixeira():

    resultado = []
    where = []

    data = request.get_json()

    if data.get('id_informativo'):

        where.append({'id_informativo':data['id_informativo']})

    if data.get('ponto_lixo_id'):

        where.append({'ponto_lixo_id':data['ponto_lixo_id']})

    if data.get('informado_por_id'):

        where.append({'informado_por_id':data['informado_por_id']})
    
    if data.get('nivel_lixeira'):

        where.append({'nivel_lixeira':data['nivel_lixeira']})

    if data.get('observacao'):

        where.append({'observacao':data['observacao']})

    if data.get('criado_em'):

        where.append({'criado_em':data['criado_em']})


    for informativo in InformativoLixeira.select(where):

        dados = {

            "id_informativo" : informativo.InformativoLixeira.id_informativo,
            "ponto_lixo_id": informativo.InformativoLixeira.ponto_lixo_id,
            "informado_por_id":informativo.InformativoLixeira.informado_por_id,
            "nivel_lixeira": informativo.InformativoLixeira.nivel_lixeira,
            "observacao": informativo.InformativoLixeira.observacao,
            "criado_em": informativo.InformativoLixeira.criado_em

        }

        resultado.append(dados)

    if(len(resultado) > 0):

        return jsonify(resultado),200
    
    else:

        return jsonify({'message':"Nenhum dado encontrado !"}),404

@informativo_lixeira.route('/cadastrar_informativo_lixeira',methods=['POST'])
def insert():

    try:

        data = request.get_json()

        if not data.get("ponto_lixo_id"):

            return jsonify({'message', 'Nenhum ponto de lixo foi informado !'}),400
        
        if data.get('nivel_lixeira') != 0:

            if(not data.get('nivel_lixeira')):

                return jsonify({'message':'O nivel da lixeira não foi informado !'}),400
            
            if(int(data.get('nivel_lixeira')) < 0):

                return jsonify({'message':'O nivel da lixeira não pode menor que 0 !'}),400
        
        if not data.get('informado_por_id'):

            return jsonify({"message": "O id do solicitante da requisição enviada não foi informado !"})
        
        informativo_lixeira = InformativoLixeira(

            ponto_lixo_id = data['ponto_lixo_id'],
            informado_por_id = data['informado_por_id'],
            nivel_lixeira = data['nivel_lixeira'],
            observacao = data['observacao'],
        )

        dados_inseridos = InformativoLixeira.insert(informativo_lixeira)

        if not dados_inseridos:

            return jsonify({"message":"Erro ao inserir informativo lixeira !"}),500
        
        retorno_dados_inseridos = {

            "id_informativo":dados_inseridos.id_informativo,
            "ponto_lixo_id": dados_inseridos.ponto_lixo_id,
            "informado_por_id": dados_inseridos.informado_por_id,
            "nivel_lixeira": dados_inseridos.nivel_lixeira,
            "observacao": dados_inseridos.observacao,
            "criado_em": str(dados_inseridos.criado_em)

        }
        
        enviar_observacao_lixeira(socketio,retorno_dados_inseridos)
                
        return jsonify({"message":"Informativo realizado com sucesso!","dados":retorno_dados_inseridos}),201


    except EOFError as e:

        return jsonify({'message':str(e)}),500