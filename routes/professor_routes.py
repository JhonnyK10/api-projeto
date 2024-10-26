from flask import Blueprint
from controllers.professor_controller import create_professor, get_professores, get_professor, update_professor, delete_professor

professor_bp = Blueprint('professor_bp', __name__)

professor_bp.route('/professores', methods=['POST'])(create_professor)
professor_bp.route('/professores', methods=['GET'])(get_professores)
professor_bp.route('/professores/<int:professor_id>', methods=['GET'])(get_professor)
professor_bp.route('/professores/<int:professor_id>', methods=['PUT'])(update_professor)
professor_bp.route('/professores/<int:professor_id>', methods=['DELETE'])(delete_professor)
