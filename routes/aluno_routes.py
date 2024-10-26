from flask import Blueprint
from controllers.aluno_controller import create_aluno, get_alunos, get_aluno, update_aluno, delete_aluno

aluno_bp = Blueprint('aluno_bp', __name__)

aluno_bp.route('/alunos', methods=['POST'])(create_aluno)
aluno_bp.route('/alunos', methods=['GET'])(get_alunos)
aluno_bp.route('/alunos/<int:aluno_id>', methods=['GET'])(get_aluno)
aluno_bp.route('/alunos/<int:aluno_id>', methods=['PUT'])(update_aluno)
aluno_bp.route('/alunos/<int:aluno_id>', methods=['DELETE'])(delete_aluno)
