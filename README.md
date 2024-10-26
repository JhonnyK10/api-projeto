# Projeto API
 
Como utilizar: 

1- Iniciar banco de dados:

python app.py

2- Testar o CRUD do projeto: 

2.1- listar alunos (Postman - GET) - http://localhost:8000/alunos/

2.2- add alunos (Postman - POST) - http://localhost:8000/alunos/
no body: 

{
  "nome": "Novo Aluno"
}

2.3- atualizar alunos (Postman - PUT) - http://localhost:8000/alunos/1
no body: 

{
  "nome": "Aluno Atualizado"
}

2.4- deletar alunos (Postman - DELETE) - http://localhost:8000/alunos/1

3- Fazer o teste unitário:

python unittest/test_core.py