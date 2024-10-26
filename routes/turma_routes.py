from flask import Blueprint
from controllers.turma_controller import create_turma, get_turmas, get_turma, update_turma, delete_turma

turma_bp = Blueprint('turma_bp', __name__)

turma_bp.route('/turmas', methods=['POST'])(create_turma)
turma_bp.route('/turmas', methods=['GET'])(get_turmas)
turma_bp.route('/turmas/<int:turma_id>', methods=['GET'])(get_turma)
turma_bp.route('/turmas/<int:turma_id>', methods=['PUT'])(update_turma)
turma_bp.route('/turmas/<int:turma_id>', methods=['DELETE'])(delete_turma)
