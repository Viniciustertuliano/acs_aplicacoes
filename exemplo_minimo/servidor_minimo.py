from types import MethodType
from flask import Flask, jsonify, request

app = Flask(__name__)

alunos = []

@app.route('/alunos', methods=['GET'])
def lista():
    return jsonify(alunos)

@app.route('/alunos', methods=['POST'])
def adiciona():
    alunos.append(request.json)
    return jsonify({'status':'ok'})


@app.route('/alunos/<int:id>', methods=['GET'])
def aluno_id(id):
    for a in alunos:
        if id == a['id']:
            return a

@app.route('/reseta', methods=['POST'])
def reseta_alunos():
    while alunos != []:
        alunos.pop()
    if alunos == []:
        return jsonify({"status":"200"})



# pessoa mais velha
# lista de chamada
# consulta uma pessoa especifica
# proximo ra valido
# validar dicionario
# criar sem RA

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)