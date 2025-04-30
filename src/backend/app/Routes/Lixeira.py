from Models.LixeiraModel import Lixeira
from Models.MaterialColetadoModel import MaterialColetado
from Models.GrupoLixeiraModel import GrupoLixeira
from Models.CorModel import Cor
from Models.PontoLixoModel import PontoLixo
from flask import request, jsonify, Blueprint

from sqlalchemy import select
from Models.ExtensionsModel import db

import werkzeug


lixeira = Blueprint('lixeira',__name__)


@lixeira.route('/cadastrar_lixeira',methods=['POST'])
def cadastrar_lixeira():

    if request.method == 'POST':

        try:

            data = request.get_json()   

            if not data.get('mat_colet_id'):

                return jsonify({'message':'Por favor informe o material coletado pela lixeira !'}),400
            
            result = MaterialColetado.select([{'mat_colet_id':data['mat_colet_id']}])

            if len(result) == 0:

                return jsonify({'message':'O material coletado pela lixeira não está cadastrado no sistema !'}),404
            
            if not data.get('grupo_lixeira_id'):

                return jsonify({'message':'O grupo de lixeira deve ser informado para lixeira !'}),400
            
            result = GrupoLixeira.select([{'grupo_lixeira_id':data['grupo_lixeira_id']}])

            if len(result) == 0 :

                return jsonify({'message':'Por favor, o grupo informado para lixeira não está cadastrado no sistema !'}),404
            
            if not data.get('ponto_lixo_id'):

                return jsonify({'message':'O ponto de lixo da lixeira não foi informado !'}),400
            
            result = PontoLixo.select([{'ponto_lixo_id':data['ponto_lixo_id']}])

            if(len(result) == 0):

                return jsonify({'message':'O ponto de lixo informado da lixeira não está cadastrado no sistema !'}),404

            if not data.get('cor_id'):

                return jsonify({'message':'O id da cor da lixeira não foi informada !'}),400
            

            result = Cor.select([{'cor_id':data['cor_id']}])

            if(len(result) == 0):

                return jsonify({'message':'A cor da lixeira não está cadastrada no sistema !'}),404

            lixeira = Lixeira(
                mat_colet_id=data['mat_colet_id'],
                grupo_lixeira_id=data['grupo_lixeira_id'],
                ponto_lixo_id = data['ponto_lixo_id'],
                cor_id = data['cor_id'],
                descricao=data['descricao'],
                capacidade = data['capacidade'],
                nivel_lixeira = data['nivel_lixeira'],
                observacao = data['observacao']
                
            )

            Lixeira.insert(lixeira)

        
            return jsonify({"message":"Lixeira cadastrada com sucesso !"}),201

        except EOFError as e:

            return jsonify({'message':str(e)}),500
        
@lixeira.route("/get_lixeira",methods=["POST"])
def get_lixeira():

    lixeiras = []
    where = []

    data = request.get_json()

    if data.get('grupo_lixeira_id'):

        where.append({'grupo_lixeira_id':data['grupo_lixeira_id']})

    if data.get('lixeira_id'):

        where.append({'lixeira_id':data['lixeira_id']})
        

    for lixeira in Lixeira.select(where):

        dados_lixeira = {

                "id_lixeira":lixeira.Lixeira.id_lixeira,
                "mat_colet_id":lixeira.Lixeira.mat_colet_id,
                "grupo_lixeira_id":lixeira.Lixeira.grupo_lixeira_id,
                "ponto_lixo_id": lixeira.Lixeira.ponto_lixo_id,
                "cor_id": lixeira.Lixeira.cor_id,
                "descricao":lixeira.Lixeira.descricao,
                "capacidade": lixeira.Lixeira.capacidade,
                "nivel_lixeira": lixeira.Lixeira.nivel_lixeira,
                "observacao": lixeira.Lixeira.observacao,
                "criado_em":lixeira.Lixeira.criado_em,
                "editado_em":lixeira.Lixeira.editado_em

        }

        lixeiras.append(dados_lixeira)

    return jsonify(lixeiras),200

@lixeira.route('/atualizar_nivel_lixeira',methods=['PUT'])
def atualizar_nivel_lixeira():

    try:

        data = request.get_json()

        if not data.get('lixeira_id'):

            return jsonify({'message':'Informe o id da lixeira !'}),400
        
        if not data.get('nivel_lixeira'):

            return jsonify({'message':'O nivel da lixeira não foi informado !'}),400
        
        lixeira = Lixeira(

            id_lixeira = data['lixeira_id'],
            nivel_lixeira = data['nivel_lixeira']
            
        )

        dados_inseridos = Lixeira.update(lixeira)
            
        return jsonify({"message":"Lixeira atualizada com sucesso !",'dados':dados_inseridos}),200
    
    except Exception as e:

        return jsonify({'message':f'${str(e)}'})

