class Fase():
    def __init__(self):
        self._passaros = []
        self._porcos = []
        self._obstaculos = []

    def adicionar_obstaculo(self, *obstaculos):
        self._obstaculos.extend(obstaculos)

    def adicionar_porco(self, *porcos):
        self._porcos.extend(porcos)

    def adicionar_passaro(self, *passaros):
        self._passaros.extend(passaros)

    def acabou(self,tempo):
        return True
