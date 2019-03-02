import unittest
import random

class Jogada:

    def __init__(self, jogada):
        self.jogada = jogada

    def __eq__(self, other):
        return self.jogada == other.jogada

    def __gt__(self, other):
        if self.jogada == 'papel' and other.jogada == 'pedra':
            return True
        if self.jogada == 'tesoura' and other.jogada == 'papel':
            return True
        if self.jogada == 'pedra' and other.jogada == 'tesoura':
            return True
        return False


def jogo():
    jogadas = ['papel', 'pedra', 'tesoura']

    resultJog1 = Jogada(random.choice(jogadas))
    resultJog2 = Jogada(random.choice(jogadas))

    print("O jogador 1 escolheu " + resultJog1.jogada)
    print("O jogador 2 escolheu " + resultJog2.jogada)

    print(analisa_resultado(resultJog1, resultJog2))

def analisa_resultado(jogada1, jogada2):
    if jogada1 == jogada2:
        return "empate"

    if jogada1 > jogada2:
        return "Jogador 1 venceu"
    else:
        return "Jogador 2 venceu"

jogo()
