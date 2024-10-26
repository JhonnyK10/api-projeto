from flask import request, jsonify
from models.professor import Professor
from config import db

def create_professor():
    data = request.get_json()
    new_professor = Professor(
        nome=data['nome'],
        idade=data['idade'],
        materia=data['materia'],
        observacoes=data.get('observacoes')
    )
    db.session.add(new_professor)
    db.session.commit()
    return jsonify({'message': 'Professor criado com sucesso!'}), 201

def get_professores():
    professores = Professor.query.all()
    return jsonify([professor.serialize() for professor in professores]), 200

def get_professor(professor_id):
    professor = Professor.query.get(professor_id)
    if professor:
        return jsonify(professor.serialize()), 200
    else:
        return jsonify({'message': 'Professor não encontrado!'}), 404

def update_professor(professor_id):
    data = request.get_json()
    professor = Professor.query.get(professor_id)
    if professor:
        professor.nome = data.get('nome', professor.nome)
        professor.idade = data.get('idade', professor.idade)
        professor.materia = data.get('materia', professor.materia)
        professor.observacoes = data.get('observacoes', professor.observacoes)
        db.session.commit()
        return jsonify({'message': 'Professor atualizado com sucesso!'}), 200
    else:
        return jsonify({'message': 'Professor não encontrado!'}), 404

def delete_professor(professor_id):
    professor = Professor.query.get(professor_id)
    if professor:
        db.session.delete(professor)
        db.session.commit()
        return jsonify({'message': 'Professor deletado com sucesso!'}), 200
    else:
        return jsonify({'message': 'Professor não encontrado!'}), 404

