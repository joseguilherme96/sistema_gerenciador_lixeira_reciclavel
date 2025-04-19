from Models.GrupoLixeiraModel import GrupoLixeira  # Importa o db e o modelo
from flask import jsonify,Blueprint,request

# Blueprint é uma extensão do Flask que pode oferecer diversos recursos, onde permite criação de componentes, para que
# depois estes componentes possam se integrar com o flask novamente. Como este projeto tem varias rotas para diferentes componentes. O Blueprint cria
# e empacota varias rotas para depois acoplar a instancia principal do flask no arquivo app.py
lixeira = Blueprint('lixeira', __name__)

@lixeira.route('/grupo_lixeira', methods=['GET'])
def select_grupo_lixeira():

    lixeiras = []

    for lixeira in GrupoLixeira.select():

        dados_lixeira = {

            "id_lixeira":lixeira.GrupoLixeira.id_lixeira,
            "nome":lixeira.GrupoLixeira.nome,
            "descricao":lixeira.GrupoLixeira.descricao,
            "cep":lixeira.GrupoLixeira.cep,
            "endereco": lixeira.GrupoLixeira.endereco,
            "cidade":lixeira.GrupoLixeira.cidade,
            "estado":lixeira.GrupoLixeira.estado
        }
        lixeiras.append(dados_lixeira)

    return jsonify(lixeiras)

@lixeira.route('/cadastrar_grupo_lixeira',methods=['POST'])
def inserir_grupo_lixeira():

    if request.method == 'POST':

        try:

            data = request.get_json()

            if(not data.get('nome')):

                return jsonify({"message":"O nome é obrigatório ser enviado !"})

            if(not data.get('descricao')):

                return jsonify({"message":"A descrição é obrigatória ser enviada !"})

            if(not data.get('cep')):

                return jsonify({"message":"O CEP é obrigatório ser enviado !"})

            if(not data.get('endereco')):

                return jsonify({"message":"O endereço é obrigatório ser enviado !"})

            if(not data.get('cidade')):

                return jsonify({"message":"A cidade é obrigatória ser enviada !"})

            if(not data.get('estado')):

                return jsonify({"message":"O estado é obrigatório ser enviado !"})

            grupo_lixeira = GrupoLixeira(
                
                nome = data['nome'],
                descricao = data['descricao'],
                cep = data['cep'],
                endereco = data['endereco'],
                cidade = data['cidade'],
                estado = data['estado']

            )

            inserir = GrupoLixeira.insert(grupo_lixeira)

            if not inserir:

                return jsonify({"message":"Erro ao inserir lixeira!"})
                
            return jsonify({"message":"Lixeira inserida com sucesso!"})
        
        except EOFError as e:

            return jsonify({'message':str(e)}),500





