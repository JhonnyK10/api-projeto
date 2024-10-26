from flask import request, jsonify
from models.turma import Turma
from config import db

def create_turma():
    data = request.get_json()
    new_turma = Turma(
        descricao=data['descricao'],
        ativo=data['ativo'],
        professor_id=data['professor_id']
    )
    db.session.add(new_turma)
    db.session.commit()
    return jsonify({'message': 'Turma criada com sucesso!'}), 201

def get_turmas():
    turmas = Turma.query.all()
    return jsonify([turma.serialize() for turma in turmas]), 200

def get_turma(turma_id):
    turma = Turma.query.get(turma_id)
    if turma:
        return jsonify(turma.serialize()), 200
    else:
        return jsonify({'message': 'Turma não encontrada!'}), 404

def update_turma(turma_id):
    data = request.get_json()
    turma = Turma.query.get(turma_id)
    if turma:
        turma.descricao = data.get('descricao', turma.descricao)
        turma.ativo = data.get('ativo', turma.ativo)
        turma.professor_id = data.get('professor_id', turma.professor_id)
        db.session.commit()
        return jsonify({'message': 'Turma atualizada com sucesso!'}), 200
    else:
        return jsonify({'message': 'Turma não encontrada!'}), 404

def delete_turma(turma_id):
    turma = Turma.query.get(turma_id)
    if turma:
        db.session.delete(turma)
        db.session.commit()
        return jsonify({'message': 'Turma deletada com sucesso!'}), 200
    else:
        return jsonify({'message': 'Turma não encontrada!'}), 404

