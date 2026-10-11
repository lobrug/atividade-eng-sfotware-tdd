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