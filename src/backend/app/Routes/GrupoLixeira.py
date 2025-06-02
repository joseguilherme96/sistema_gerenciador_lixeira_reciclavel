from Models.GrupoLixeiraModel import GrupoLixeira  # Importa o db e o modelo
from flask import jsonify,Blueprint,request
from Models.LixeiraModel import Lixeira
import math
from datetime import datetime,time

# Blueprint é uma extensão do Flask que pode oferecer diversos recursos, onde permite criação de componentes, para que
# depois estes componentes possam se integrar com o flask novamente. Como este projeto tem varias rotas para diferentes componentes. O Blueprint cria
# e empacota varias rotas para depois acoplar a instancia principal do flask no arquivo app.py
grupo_lixeira = Blueprint('grupo_lixeira', __name__)

@grupo_lixeira.route('/grupo_lixeira', methods=['POST'])
def select_grupo_lixeira():

    lixeiras = []
    where = []

    data = request.get_json()

    if data.get('grupo_lixeira_id'):

        where.append({'grupo_lixeira_id':data['grupo_lixeira_id']})

    if data.get('nome'):

        where.append({'nome':data['nome']})

    if data.get('descricao'):

        where.append({'descricao':data['descricao']})

    if data.get('logradouro'):

        where.append({'logradouro':data['logradouro']})

    if data.get('cidade'):

        where.append({'cidade':data['cidade']})
    
    if data.get('cep'):

        where.append({'cep':data['cep']})

    if data.get('bairro'):

        where.append({'bairro':data['bairro']})

    if data.get('estado'):

        where.append({'estado':data['estado']})

    if data.get('uf'):

        where.append({'uf':data['uf']})

    if data.get('data'):

        where.append({'data':data['data']})

    if data.get('hora'):

        where.append({'hora':data['hora']})

    for lixeira in GrupoLixeira.select(where):

        grupo_id,media_nivel_lixeira_por_grupo = Lixeira.calcular_media_nivel_lixo_por_grupo([{'grupo_lixeira_id':lixeira.GrupoLixeira.id_grupo_lixeira}])[0]
        grupo_id,soma_capacidade_lixeira_por_grupo = Lixeira.calcular_soma_capacidade_total_armazenamento_de_lixo_por_grupo([{'grupo_lixeira_id':lixeira.GrupoLixeira.id_grupo_lixeira}])[0]

        dados_lixeira = {

            "id_grupo_lixeira":lixeira.GrupoLixeira.id_grupo_lixeira,
            "nome":lixeira.GrupoLixeira.nome,
            "descricao":lixeira.GrupoLixeira.descricao,
            "nivel_lixeira": math.ceil(media_nivel_lixeira_por_grupo),
            "capacidade_total_lixo": math.ceil(soma_capacidade_lixeira_por_grupo),
            "cep":lixeira.GrupoLixeira.cep,
            "endereco": lixeira.GrupoLixeira.endereco,
            "bairro":lixeira.GrupoLixeira.bairro,
            "cidade":lixeira.GrupoLixeira.cidade,
            "estado":lixeira.GrupoLixeira.estado,
            "uf":lixeira.GrupoLixeira.uf,
            "data": datetime.strftime(lixeira.GrupoLixeira.data, "%d/%m/%Y"),
            "hora": time.strftime(lixeira.GrupoLixeira.hora, "%H:%M:%S")
        }
        lixeiras.append(dados_lixeira)

    return jsonify(lixeiras),200

@grupo_lixeira.route('/cadastrar_grupo_lixeira',methods=['POST'])
def inserir_grupo_lixeira():

    if request.method == 'POST':

        try:

            data = request.get_json()

            if(not data.get('nome')):

                return jsonify({"message":"O nome é obrigatório ser enviado !"}),400

            if(not data.get('descricao')):

                return jsonify({"message":"A descrição é obrigatória ser enviada !"}),400

            if(not data.get('cep')):

                return jsonify({"message":"O CEP é obrigatório ser enviado !"}),400

            if(not data.get('endereco')):

                return jsonify({"message":"O endereço é obrigatório ser enviado !"}),400
            
            if(not data.get('bairro')):
                return jsonify({"message":"O bairro é obrigatório ser enviado !"}),400

            if(not data.get('cidade')):

                return jsonify({"message":"A cidade é obrigatória ser enviada !"}),400

            if(not data.get('estado')):

                return jsonify({"message":"O estado é obrigatório ser enviado !"}),400

            grupo_lixeira = GrupoLixeira(
                
                nome = data['nome'],
                descricao = data['descricao'],
                cep = data['cep'],
                endereco = data['endereco'],
                bairro = data['bairro'],
                cidade = data['cidade'],
                estado = data['estado']

            )

            dados_inseridos = GrupoLixeira.insert(grupo_lixeira)

            return jsonify({"message":"Grupo lixeira inserido com sucesso!",'dados':dados_inseridos}),201
        
        except Exception as e:

            return jsonify({'message':str(e)}),500





