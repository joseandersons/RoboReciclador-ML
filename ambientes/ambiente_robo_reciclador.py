import gym
from gym import spaces
import numpy as np
import random

class AmbienteRoboReciclador(gym.Env):
    def __init__(self):
        super(AmbienteRoboReciclador, self).__init__()

        # Espaço de ações: [Mover para frente, trás, esquerda, direita, coletar]
        self.espaco_acoes = spaces.Discrete(5)

        # Espaço de observação: [Posição do robô, tipo do objeto, posição do objeto]
        self.espaco_observacao = spaces.Box(
            low=0, high=10, shape=(5,), dtype=np.float32
        )

        # Estado inicial
        self.posicao_robo = [0, 0]
        self.posicao_objeto = [random.randint(0, 9), random.randint(0, 9)]
        self.tipo_objeto = random.choice(["reciclavel", "nao_reciclavel"])
        self.passos = 0
        self.max_passos = 50

    def resetar(self):
        # Reinicia o ambiente
        self.posicao_robo = [0, 0]
        self.posicao_objeto = [random.randint(0, 9), random.randint(0, 9)]
        self.tipo_objeto = random.choice(["reciclavel", "nao_reciclavel"])
        self.passos = 0
        return self._obter_estado()

    def executar_acao(self, acao):
        self.passos += 1

        # Movimentos básicos
        if acao == 0:  # Mover para frente
            self.posicao_robo[1] += 1
        elif acao == 1:  # Mover para trás
            self.posicao_robo[1] -= 1
        elif acao == 2:  # Mover para a esquerda
            self.posicao_robo[0] -= 1
        elif acao == 3:  # Mover para a direita
            self.posicao_robo[0] += 1
        elif acao == 4:  # Coletar
            if self.posicao_robo == self.posicao_objeto:
                if self.tipo_objeto == "reciclavel":
                    recompensa = 10
                else:
                    recompensa = -5
                self.posicao_objeto = [random.randint(0, 9), random.randint(0, 9)]
                self.tipo_objeto = random.choice(["reciclavel", "nao_reciclavel"])
            else:
                recompensa = -1
        else:
            recompensa = -1

        # Penalidade por passos extras
        recompensa = -0.1 if acao != 4 else recompensa

        # Estado final (termina após um número de passos ou se "limpar tudo")
        terminou = self.passos >= self.max_passos

        return self._obter_estado(), recompensa, terminou, {}

    def renderizar(self, modo='humano'):
        print(f"Posição do Robô: {self.posicao_robo}, Objeto: {self.tipo_objeto} em {self.posicao_objeto}")

    def _obter_estado(self):
        return np.array(self.posicao_robo + [1 if self.tipo_objeto == "reciclavel" else 0] + self.posicao_objeto)
