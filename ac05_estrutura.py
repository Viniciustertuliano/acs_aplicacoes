import hashlib
import inspect
import re

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
        if self.tabela[posicao] is None:  # verifica se o slot  ́e None
            self.tabela[posicao] = [item]
        else:
            self.tabela[posicao].append(item)

    def remover(self, item):
        posicao = self.hash(item)
        # se o slot n~ao  ́e None, ent~ao ele  ́e uma lista (encadeamento)
        if self.tabela[posicao] is not None:
            # percorre a lista do slot para remover o item, se ele existir
            for i in range(len(self.tabela[posicao])):
                if item == self.tabela[posicao][i]:
                    # remove o item da lista daquele slot espec ́ıfico
                    self.tabela[posicao].pop(i)
                    break
            # se a lista ficar vazia, mudamos o valor do slot para None
            if len(self.tabela[posicao]) == 0:
                self.tabela[posicao] = None

    def buscar(self, item):
        posicao = self.hash(item)
        # se o slot n~ao  ́e None, ent~ao ele  ́e uma lista (encadeamento)
        if self.tabela[posicao] is not None:
            # percorre a lista do slot para procurar o item, se ele existir
            for i in range(len(self.tabela[posicao])):
                if item == self.tabela[posicao][i]:
                    return True
            return False

    def fator_de_carga(self):
        cont = 0
        for a in self.tabela:
            if a is not None:
                if type(a) == type([]):
                    for b in a:
                        cont += 1
                else:
                    cont += 1
        return cont / self.tamanho_tabela

    def eh_primo(self, numero):
        if numero == 2 or (numero != 1 and numero % 2 == 1):
            primo = True
        else:
            primo = False

        divisor = 3
        while divisor < numero // 2 and primo:
            if numero % divisor == 0:
                primo = False
            divisor += 2

        if primo:
            return True
        else:
            return False

    def redimensionar(self, novo_tamanho, tamanho_primo):
        aux = []
        for a in self.tabela:
            if a is not None:
                if type(a) == type([]):
                    for b in a:
                        print(a)
                        print(b)
                        aux.append(b)
                self.remover(a)
                else:
                    self.remover(a)
            else:
                self.remover(a)
        if tamanho_primo == True:
            novo_tamanho += 1
            while self.eh_primo(novo_tamanho) != True:
                novo_tamanho += 1
            self.__init__(novo_tamanho)
        else:
            self.__init__(novo_tamanho)
        for a in aux:
            self.adicionar(a)

        

# ==========================
# Codigo auxiliar: nao altere as definicoes abaixo.
# Nao se preocupe com esse codigo. Ele serve apenas para testar sua atividade.
# ==========================

def testa_eh_primo():
    fonte = inspect.getsource(TabelaDispersao.eh_primo)
    elementos = re.sub('\s+', ' ', fonte).strip().split(' ')
    ok = False
    for e in elementos:
        dig = hashlib.sha256(e.encode('utf-8')).hexdigest()
        if dig == '07a8750738828ffd36a9bbfc198cf5d3bfd93e9f86b0e16e5aedeef8426804cf' or dig == '10c22bcf4c768b515be4e94bcafc71bf3e8fb5f70b2584bcc8c7533217f2e7f9':
            ok = True
            break
    return ok


def testa_atividade(nome_teste, valor=None):
    if nome_teste == 'fator_de_carga':
        tamanho = valor['tamanho']
        itens = valor['itens']
        td = TabelaDispersao(tamanho)
        for i in itens:
            td.adicionar(i)
        print('%.3f' % (td.fator_de_carga()))
    elif nome_teste == 'eh_primo':
        num = valor['numero']
        td = TabelaDispersao(11)
        if testa_eh_primo():
            if td.eh_primo(num):
                print('Numero primo')
            else:
                print('Numero composto')
    elif nome_teste == 'redimensionar':
        tamanho_antigo = valor['tamanho_antigo']
        tamanho_novo = valor['tamanho_novo']
        tamanho_primo = valor['tamanho_primo']
        itens = valor['itens']
        td = TabelaDispersao(tamanho_antigo)
        for i in itens:
            td.adicionar(i)
        print(td.tabela)
        td.redimensionar(tamanho_novo, tamanho_primo)
        print(td.tabela)
        if (not tamanho_primo and td.tamanho_tabela == tamanho_novo) or (tamanho_primo and td.tamanho_tabela >= tamanho_novo and (td.eh_primo(td.tamanho_tabela))):
            print('Tamanho OK')
        else:
            print('Tamanho errado')


def main():
    nome_teste = input()
    valor = eval(input())
    testa_atividade(nome_teste, valor)


main()
