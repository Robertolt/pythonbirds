class Pessoa:
    olhos = 2 #atributo default

    def __init__(self, *filhos, nome = None, idade=20):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    print(Pessoa.olhos)
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
