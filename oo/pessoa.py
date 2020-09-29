class Pessoa:
    def __init__(self, *filho, nome = None, idade=20):
        self.idade = idade
        self.nome = nome
        self.filho = list(filho)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    luciano = Pessoa(nome='Luciano')
    roberto = Pessoa(luciano, nome='Roberto')
    print(Pessoa.cumprimentar(roberto))
    print(id(roberto))
    print(roberto.cumprimentar())
    print(roberto.nome)
    print(roberto.idade)
    for filhos in roberto.filho:
        print(filho.nome)