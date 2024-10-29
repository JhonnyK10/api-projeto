from flask import request, jsonify
from models.aluno import Aluno, aluno_por_id, listar_alunos, adicionar_aluno, atualizar_aluno, excluir_aluno, AlunoNaoEncontrado
from models.turma import Turma
from config import db

def create_aluno():
    data = request.get_json()
    turma_id = data.get('turma_id')
    if not turma_id or not Turma.query.get(turma_id):
        return jsonify({'message': 'Turma não encontrada!'}), 404
    adicionar_aluno(data)
    return jsonify({'message': 'Aluno criado com sucesso!'}), 201

def get_alunos():
    alunos = listar_alunos()
    return jsonify(alunos), 200

def get_aluno(aluno_id):
    try:
        aluno = aluno_por_id(aluno_id)
        return jsonify(aluno), 200
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado!'}), 404

def update_aluno(aluno_id):
    data = request.get_json()
    try:
        atualizar_aluno(aluno_id, data)
        return jsonify({'message': 'Aluno atualizado com sucesso!'}), 200
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado!'}), 404

def delete_aluno(aluno_id):
    try:
        excluir_aluno(aluno_id)
        return jsonify({'message': 'Aluno deletado com sucesso!'}), 200
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado!'}), 404
