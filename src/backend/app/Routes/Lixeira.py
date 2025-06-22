from Models.LixeiraModel import Lixeira
from Models.MaterialColetadoModel import MaterialColetado
from Models.GrupoLixeiraModel import GrupoLixeira
from Models.CorModel import Cor
from Models.PontoLixoModel import PontoLixo
from Models.ExtensionsModel import db
from flask import request, jsonify, Blueprint

from Routes.SocketioEnviarAtualizacaoNivelLixeira import enviar_atualizacao_nivel_lixeira
from Routes.Socketio import socketio

from Models.ExtensionsModel import db

from flask_jwt_extended import jwt_required

lixeira = Blueprint('lixeira',__name__)


@lixeira.route('/cadastrar_lixeira',methods=['POST'])
@jwt_required()
def cadastrar_lixeira(data = [], chamada_interna_api = False):

    if request.method == 'POST':

        try:

            realizar_commit = False

            # A responsabilidade da transação fica com a função que chamou a api caso seja uma chamada interna
            if not chamada_interna_api:
                db.session.begin()
                realizar_commit = True
                data = request.get_json()

            if(len(data) == 0):

                return jsonify({'message':'Nenhuma lixeira foi enviada para cadastro !'}),400

            lixeiras = []

            for lixeira in data:

                if not lixeira.get('mat_colet_id'):

                    return jsonify({'message':'Por favor informe o material coletado pela lixeira !'}),400
                
                result = MaterialColetado.select([{'mat_colet_id':lixeira['mat_colet_id']}])

                if len(result) == 0:

                    return jsonify({'message':'O material coletado pela lixeira não está cadastrado no sistema !'}),404
                
                if not lixeira.get('grupo_lixeira_id'):

                    return jsonify({'message':'O grupo de lixeira deve ser informado para lixeira !'}),400
                
                result = GrupoLixeira.select([{'grupo_lixeira_id':lixeira['grupo_lixeira_id']}])

                if len(result) == 0 :

                    return jsonify({'message':'Por favor, o grupo informado para lixeira não está cadastrado no sistema !'}),404
                
                if not lixeira.get('ponto_lixo_id'):

                    return jsonify({'message':'O ponto de lixo da lixeira não foi informado !'}),400
                
                result = PontoLixo.select([{'ponto_lixo_id':lixeira['ponto_lixo_id']}])

                if(len(result) == 0):

                    return jsonify({'message':'O ponto de lixo informado da lixeira não está cadastrado no sistema !'}),404

                if not lixeira.get('cor_id'):

                    return jsonify({'message':'O id da cor da lixeira não foi informada !'}),400
                

                result = Cor.select([{'cor_id':lixeira['cor_id']}])

                if(len(result) == 0):

                    return jsonify({'message':'A cor da lixeira não está cadastrada no sistema !'}),404
                
                lixeiras.append(Lixeira(
                    mat_colet_id=lixeira['mat_colet_id'],
                    grupo_lixeira_id=lixeira['grupo_lixeira_id'],
                    ponto_lixo_id = lixeira['ponto_lixo_id'],
                    cor_id = lixeira['cor_id'],
                    descricao=lixeira['descricao'],
                    capacidade = lixeira['capacidade'],
                    nivel_lixeira = lixeira['nivel_lixeira'],
                    observacao = lixeira['observacao']
                ))

            dados_inseridos = Lixeira.insert(lixeiras)

            lixeiras = []

            for lixeira in dados_inseridos:

                linha = {

                "id_lixeira" : lixeira.id_lixeira,
                "descricao" : lixeira.descricao,
                "mat_colet_id" : lixeira.mat_colet_id,
                "grupo_lixeira_id": lixeira.grupo_lixeira_id,
                "ponto_lixo_id": lixeira.ponto_lixo_id,
                "cor_id": lixeira.cor_id,
                "capacidade ": lixeira.capacidade,
                "nivel_lixeira ": lixeira.nivel_lixeira,
                "esta_aberta ": lixeira.esta_aberta,
                "observacao ": lixeira.observacao,
                "criado_em ": str(lixeira.criado_em),
                "editado_em ": str(lixeira.editado_em)


                }

                lixeiras.append(linha)

                if realizar_commit :
                    
                    db.session.commit()
        
            return jsonify({"message":"Lixeira cadastrada com sucesso !","dados":lixeiras}),201

        except Exception as e:

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
                "esta_aberta": "Aberta" if lixeira.Lixeira.esta_aberta else "Fechada",
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
        
        if data.get('nivel_lixeira') != 0:

            if(not data.get('nivel_lixeira')):

                return jsonify({'message':'O nivel da lixeira não foi informado !'}),400
            
            if(int(data.get('nivel_lixeira')) < 0):

                return jsonify({'message':'O nivel da lixeira não pode menor que 0 !'}),400
        
        if data.get('esta_aberta') == "" and not data.get('esta_aberta'):

            return jsonify({'message':'O estado da lixeira não foi informado !'}),400
        
        lixeira = Lixeira(

            id_lixeira = data['lixeira_id'],
            nivel_lixeira = data['nivel_lixeira'],
            esta_aberta = data['esta_aberta']
            
        )

        dados_inseridos = Lixeira.update(lixeira)
        
        enviar_atualizacao_nivel_lixeira(socketio,dados_inseridos) 
        return jsonify({"message":"Lixeira atualizada com sucesso !",'dados':dados_inseridos}),200
    
    except Exception as e:

        return jsonify({'message':f'${str(e)}'})

