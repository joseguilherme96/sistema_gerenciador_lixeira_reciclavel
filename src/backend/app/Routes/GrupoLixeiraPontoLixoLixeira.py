from flask import request, jsonify, Blueprint
from Models.GrupoLixeiraModel import GrupoLixeira
from Models.PontoLixoModel import PontoLixo
from Models.LixeiraModel import Lixeira
from Routes.GrupoLixeira import inserir_grupo_lixeira
from Routes.PontoLixo import insert as insert_ponto_lixo
from Routes.Lixeira import cadastrar_lixeira
from Models.ExtensionsModel import db
import json
import requests
from flask_jwt_extended import jwt_required


grupo_lixeira_ponto_lixo_lixeira = Blueprint('grupo_lixeira_ponto_lixo_lixeira',__name__)
@grupo_lixeira_ponto_lixo_lixeira.route('/cadastrar_grupo_lixeira_ponto_lixo_lixeira',methods=['POST'])
@jwt_required()
def cadastrar_grupo_lixeira_ponto_lixo_lixeira():


    try:

        # with faz com que não precise utilizar db.session.commit() caso este código seja executado com sucesso !
        with db.session.begin():
            
            data = request.get_json()
            quantidade_lixeiras_para_cadastro = len(data['lixeiras'])
            ponto_lixo_criado = []

            retorno_inserir_grupo_lixeira = inserir_grupo_lixeira()
            status_code = retorno_inserir_grupo_lixeira[1]
            retorno_data_json = retorno_inserir_grupo_lixeira[0].get_data(as_text=True)
            retorno_data_json = retorno_inserir_grupo_lixeira[0].get_data(as_text=True)
            retorno_data_objeto = json.loads(retorno_data_json)

            if status_code != 201:

                return retorno_inserir_grupo_lixeira

            grupo_lixeira_id = retorno_data_objeto["dados"][0]['id_grupo_lixeira']

            # Cadastra pontos de lixos
            for _ in range(0,quantidade_lixeiras_para_cadastro):

                retorno_ponto_lixo = insert_ponto_lixo(data = [],chamada_interna_api = True)
                data_json = retorno_ponto_lixo[0].get_data(as_text=True)
                ponto_lixo = json.loads(data_json)
                ponto_lixo_criado.append(ponto_lixo["dados"]) 

            
            # Vincula cada ponto de lixo criado a uma lixeira
            # Vincula também  grupo_lixeira_id criado a todas a lixeiras
            for (key,lixeira) in enumerate(data["lixeiras"],0):

                lixeira["ponto_lixo_id"] = ponto_lixo_criado[key]["ponto_lixo_id"]
                lixeira["grupo_lixeira_id"] = grupo_lixeira_id

            resposta_cadastro_lixeira = cadastrar_lixeira(data['lixeiras'],chamada_interna_api = True)
            resposta_cadastro_lixeira_data_json = resposta_cadastro_lixeira[0].get_data(as_text=True)
            resposta_cadastro_lixeira_objeto = json.loads(resposta_cadastro_lixeira_data_json)
            status_code = resposta_cadastro_lixeira[1]
            

            if status_code != 201:

                db.session.rollback()
                return jsonify(resposta_cadastro_lixeira_objeto),status_code
        
        
            return jsonify({
                "dados_grupo_criado":retorno_data_objeto['dados'][0],
                "dados_ponto_lixo_criado":ponto_lixo_criado,
                "dados_lixeira_criado":resposta_cadastro_lixeira_objeto["dados"],
                "message":"O grupo, os pontos de lixo e lixeiras foram criados com sucesso !"
                
            }),201

    except Exception as e:

        db.session.rollback()
        return jsonify({'message':f'${str(e)}'})