from config import db

class Turma(db.Model):
    __tablename__ = 'turmas'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    ativo = db.Column(db.Boolean, default=True)

    # Relacionamento com Professor
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)

    # Relacionamento com Aluno
    alunos = db.relationship('Aluno', backref='turma', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'ativo': self.ativo,
            'professor_id': self.professor_id
        }
