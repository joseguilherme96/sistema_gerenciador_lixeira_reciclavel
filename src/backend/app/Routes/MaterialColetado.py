from flask import request, jsonify, Blueprint
from Models.MaterialColetadoModel import MaterialColetado
from flask_jwt_extended import jwt_required

material_coletado = Blueprint('material_coletado',__name__)


@material_coletado.route('/cadastrar_material_coletado',methods=['POST'])
@jwt_required()
def insert():

    try:


        data = request.get_json()

        if not data.get('nome'):

            return jsonify({'message':'Por favor informe o material coletado !'})
        
        material_coletado = MaterialColetado(

            nome= data['nome']


        ) 

        dados_inseridos = MaterialColetado.insert(material_coletado)

        return jsonify({'message':'Material coletado foi inserido com sucesso !','dados':dados_inseridos})
    
    except Exception as e:

        return jsonify({'message':f'${str(e)}'})

@material_coletado.route('/material_coletado',methods=['POST'])
def select_material_coletado():

    try:
        data = request.get_json()

        where = []
        material_coletado = []

        if data.get('mat_colet_id'):

            where.append({"mat_colet_id":data['mat_colet_id']})

        if data.get('nome'):

            where.append({"nome":data['nome']})

        if data.get('criado_em'):

            where.append({"criado_em":data['criado_em']})

        for material in MaterialColetado.select(where):

            encontrado = {

                "mat_colet_id" : material.MaterialColetado.id_mat_colet,
                "nome": material.MaterialColetado.nome,
                "criado_em": material.MaterialColetado.criado_em
                
            }

            material_coletado.append(encontrado)

        if(len(material_coletado) == 0):

            return jsonify({'message':'Nenhum material encontrado !'}),404
        
        return jsonify(material_coletado)

    except Exception as e:

        return jsonify({'message':f'${str(e)}'}),400



    