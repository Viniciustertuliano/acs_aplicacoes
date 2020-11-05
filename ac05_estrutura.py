class TabelaDispersao:

    def __init__(self, tamanho_tabela):
        self.tamanho_tabela = tamanho_tabela
        self.tabela = [None] * tamanho_tabela

    def hash_int(self, item):
        return item % self.tamanho_tabela

    def hash_string(self, item):
        soma = 0
        for pos in range(len(item)):
            soma = soma + (ord(item[pos]) * (pos+1))
        return soma % self.tamanho_tabela

    def hash(self, item):
        if type(item) is int:
            posicao = self.hash_int(item)
        else:
            posicao = self.hash_string(str(item))
        return posicao

    def adicionar(self, item):
        posicao = self.hash(item)
        if self.tabela[posicao] is None:  # verifica se o slot é None
            self.tabela[posicao] = [item]
        else:
            self.tabela[posicao].append(item)

    def remover(self, item):
        posicao = self.hash(item)
        # se o slot não é None, então ele é uma lista (encadeamento)
        if self.tabela[posicao] is not None:
            # percorre a lista do slot para remover o item, se ele existir
            for i in range(len(self.tabela[posicao])):
                if item == self.tabela[posicao][i]:
                    # remove o item da lista daquele slot específico
                    self.tabela[posicao].pop(i)
                    break
            # se a lista ficar vazia, mudamos o valor do slot para None
            if len(self.tabela[posicao]) == 0:
                self.tabela[posicao] = None

    def buscar(self, item):
        posicao = self.hash(item)
        # se o slot não é None, então ele é uma lista (encadeamento)
        if self.tabela[posicao] is not None:
            # percorre a lista do slot para procurar o item, se ele existir
            for i in range(len(self.tabela[posicao])):
                if item == self.tabela[posicao][i]:
                    return True
        return False

def fator_de_carga(self):
    pass

def eh_primo(self, numero):
    pass

def redimensionar(self, novo_tamanho, tamanho_primo):
    pass
