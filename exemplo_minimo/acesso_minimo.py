import requests

#vai usar o verbo post - vai ser util na parte do treinador
def cria_pessoa(nome, ra):
    url = "http://localhost:5002/pessoas"
    r = requests.post(url,json={'nome':nome, 'ra':ra})
    #            ----
    #            verbo
    #                     ----------------------------
    #                     mandei um dicionario que
    #                     o python colocou num arquivo .json
    #                     (escrevi json={"chave":"valor"...})
    #                     precisa escrever esse json=, 
    #                     nao basta só passar o segundo argumento

#pega pessoas usa o verbo get, já sabemos como é
def pega_pessoas():
    url = "http://localhost:5002/pessoas"
    r = requests.get(url)
    return r.json()

#experimentar também o postman
