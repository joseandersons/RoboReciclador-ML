import random

class AgenteAleatorio:
    def __init__(self, espaco_acoes):
        self.espaco_acoes = espaco_acoes

    def agir(self, estado):
        return random.choice(range(self.espaco_acoes.n))  # Escolhe uma ação aleatória
