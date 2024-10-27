from flask import request, jsonify
from models.aluno import Aluno
from config import db

def create_aluno():
    data = request.get_json()
    new_aluno = Aluno(
        nome=data['nome'],
        idade=data['idade'],
        turma=data['turma'],
        data_nascimento=data['data_nascimento'],
        nota_primeiro_semestre=data['nota_primeiro_semestre'],
        nota_segundo_semestre=data['nota_segundo_semestre'],
        media_final=data['media_final']
    )
    db.session.add(new_aluno)
    db.session.commit()
    return jsonify({'message': 'Aluno criado com sucesso!'}), 201

def get_alunos():
    alunos = Aluno.query.all()
    return jsonify([aluno.to_dict() for aluno in alunos]), 200

def get_aluno(aluno_id):
    aluno = Aluno.query.get(aluno_id)
    if aluno:
        return jsonify(aluno.to_dict()), 200
    else:
        return jsonify({'message': 'Aluno não encontrado!'}), 404

def update_aluno(aluno_id):
    data = request.get_json()
    aluno = Aluno.query.get(aluno_id)
    if aluno:
        aluno.nome = data.get('nome', aluno.nome)
        aluno.idade = data.get('idade', aluno.idade)
        aluno.turma = data.get('turma', aluno.turma)
        aluno.data_nascimento = data.get('data_nascimento', aluno.data_nascimento)
        aluno.nota_primeiro_semestre = data.get('nota_primeiro_semestre', aluno.nota_primeiro_semestre)
        aluno.nota_segundo_semestre = data.get('nota_segundo_semestre', aluno.nota_segundo_semestre)
        aluno.media_final = data.get('media_final', aluno.media_final)
        db.session.commit()
        return jsonify({'message': 'Aluno atualizado com sucesso!'}), 200
    else:
        return jsonify({'message': 'Aluno não encontrado!'}), 404

def delete_aluno(aluno_id):
    aluno = Aluno.query.get(aluno_id)
    if aluno:
        db.session.delete(aluno)
        db.session.commit()
        return jsonify({'message': 'Aluno deletado com sucesso!'}), 200
    else:
        return jsonify({'message': 'Aluno não encontrado!'}), 404


