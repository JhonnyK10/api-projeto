from flask import Flask
from config import app, db
from routes.professor_routes import professor_bp
from routes.turma_routes import turma_bp
from routes.aluno_routes import aluno_bp

# Registrar os blueprints com prefixo '/api'
app.register_blueprint(professor_bp, url_prefix='/api')
app.register_blueprint(turma_bp, url_prefix='/api')
app.register_blueprint(aluno_bp, url_prefix='/api')

# Criar as tabelas no banco de dados
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])
