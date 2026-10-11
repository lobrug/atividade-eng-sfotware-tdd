from abc import ABC, abstractmethod


# Padrão Usado Strategy
class EstrategiaFrete(ABC):
    @abstractmethod
    def calcular(self):
        pass


class FretePac(EstrategiaFrete):
    def calcular(self):
        return 15

class FreteSedex(EstrategiaFrete):
    def calcular(self):
        return 30

class FreteTransportadora(EstrategiaFrete):
    def calcular(self):
        return 20

class CalculadoraFrete:
    def __init__(self, estrategia: EstrategiaFrete):
        self.estrategia = estrategia

    def calcular(self):
        return self.estrategia.calcular()


"""
========================================================================================= test session starts ==========================================================================================
platform linux -- Python 3.14.2, pytest-9.1.1, pluggy-1.6.0
rootdir: /workspaces/atividade-eng-sfotware-tdd/Atividade em Sala - Ciclo Vermelho-Verde-Refatorar
plugins: anyio-4.15.1
collected 3 items                                                                                                                                                                                      

teste_frete.py ...                                                                                                                                                                               [100%]

========================================================================================== 3 passed in 0.02s ===========================================================================================
"""

"""
AUTOAVALIAÇãO:

Nesta atividade sinto que a maior dificuldade foi lembrar sobre padrões de projeto e como aplica-lá em código. Consegui atingir todas as metas própostas na atividade.
O código mudou significativamente da fase verde para o refactor mudando ambos os arquivos para a implementação do Strategy. 

USO DE I.A:
Nesta atividade, diferente das ultimas decidi usar bem mais a I.A, sendo util na hora de organizar as informações, tirar dúvidas, como usar o pytest corretamente e como implementar o strategy em python.
Não sinto que ela tenha me atrapalhado na atividade.
Link I.A: https://chatgpt.com/share/6acb09e4-f170-83e9-a0bd-7c059588e990
"""
