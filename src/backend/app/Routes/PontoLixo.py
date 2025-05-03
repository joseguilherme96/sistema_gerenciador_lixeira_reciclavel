from flask import request, jsonify, Blueprint
from Models.PontoLixoModel import PontoLixo
from Models.ExtensionsModel import db

ponto_lixo = Blueprint('ponto_lixo',__name__)

@ponto_lixo.route('/cadastrar_ponto_lixo',methods=['POST'])
def insert(data = [],chamada_interna_api = False):

    try:

        realizar_commit = False

        # A responsabilidade da transação fica com a função que chamou a api caso seja uma chamada interna
        if not chamada_interna_api:

            db.session.begin()
            realizar_commit = True
            data = request.get_json()

        dados_inseridos = PontoLixo.insert(PontoLixo())
        
        db.session.commit() if realizar_commit else ''

        return jsonify({'message':'O ponto de lixo foi inserido com sucesso !',"dados":dados_inseridos}),201

    except Exception as e:

        return jsonify({'message':f'${str(e)}'})
    
@ponto_lixo.route('/ponto_lixo',methods=['POST'])
def select():

    try:

        data = request.get_json()

        where = []
        dados_encontrados = []

        if data.get('ponto_lixo_id'):

            where.append({'ponto_lixo_id':data['ponto_lixo_id']})
        
        if data.get('data'):

            where.append({'data':data['data']})

        if data.get('hora'):

            where.append({'hora':data['hora']})

        for ponto_lixo in PontoLixo.select(where):

            encontrado = {

                "ponto_lixo_id" : ponto_lixo.PontoLixo.id_ponto_lixo,
                "data": str(ponto_lixo.PontoLixo.data),
                "hora": str(ponto_lixo.PontoLixo.time)
                
            }

            dados_encontrados.append(encontrado)

        if(len(dados_encontrados) == 0):

            return jsonify({'message':'Nenhum ponto lixo encontrado !'}),404
        
        return jsonify(dados_encontrados)


    except Exception as e:

        return jsonify({'message':f'${str(e)}'})