class Pessoa:
    def __init__(self, *filhos, nome = None, idade=20):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    luciano = Pessoa(nome='Luciano')
    roberto = Pessoa(nome='Roberto')
    print(Pessoa.cumprimentar(roberto))
    print(id(roberto))
    print(roberto.cumprimentar())
    print(roberto.nome)
    print(roberto.idade)
    for filho in roberto.filhos:
        print(filho.nome)
    luciano.sobrenome='Ramalho'
    del luciano.filhos
    print(luciano.__dict__)
    print(roberto.__dict__)
