from types import MethodType
from flask import Flask, jsonify, request, make_response


app = Flask(__name__)

pessoa = []
database = {}
matches = {}

@app.route('/pessoas', methods=['GET'])
def lista():
    return jsonify(pessoa)


@app.route('/pessoas', methods=['POST'])
def criaPessoa():
    pessoa.append(request.json)
    return jsonify({"status": "200"})


@app.route('/pessoas/<int:id>', methods=['GET'])
def pessoaPorId(id):
    for p in pessoa:
        if id == p['id']:
            return p


@app.route('/interesses/<int:id>', methods=['GET'])
def interesses(id):
    if id in database:
        print(database)
        return jsonify(database[id])
    else:
        return jsonify([])


@app.route('/sinalizar_interesse/<int:id1>/<int:id2>/', methods=['PUT'])
def sinalizarInteresse(id1, id2):
    ache_p1, achei_p2 = False, False
    for p in pessoa:
        if id1 == p['id']:
            ache_p1 = True
        if id2 == p['id']:
            achei_p2 = True
    if not ache_p1:
        return make_response(jsonify({"status": "404"}), 404)
    if not achei_p2:
        return make_response(jsonify({"status": "404"}), 404)
    if ache_p1 == achei_p2:
        if id1 in database:
            database[id1].append(id2)
        else:
            database[id1] = [id2]
        return jsonify({"status": "200"})

'''
@app.route('/matches/<int:id>', methods=['GET'])
def lista_matches(id):
    if id in database:
        for a in database[id]:
            if a in database:
                if id in database[a]:
                    if id in matches:
                        matches[id].append(a)
                    else:
                        matches[id] = [a]
                    return jsonify(matches[id])
            else:
                return jsonify([])
'''


# Limpa Lista de pessoas
@app.route('/reseta', methods=['POST'])
def resetaPessoas():
    while pessoa != []:
        for p in pessoa:
            if p['id'] in database:
                database.pop(p['id'])
        pessoa.pop()
    if pessoa == []:
        return jsonify({"status": "200"})


if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)
