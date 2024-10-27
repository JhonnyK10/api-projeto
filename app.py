from flask import Flask
from config import app, db
from routes.aluno_routes import alunos_blueprint
from routes.professor_routes import professores_blueprint
from routes.turma_routes import turmas_blueprint

app.register_blueprint(alunos_blueprint, url_prefix='/api')
app.register_blueprint(professores_blueprint, url_prefix='/api')
app.register_blueprint(turmas_blueprint, url_prefix='/api')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])

