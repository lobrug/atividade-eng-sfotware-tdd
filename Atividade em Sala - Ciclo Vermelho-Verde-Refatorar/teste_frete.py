"""
-Aluno: Lorenzo Brugnolo Rosa
-Plano: Calculadora de frete para e-commerce.
-Padrão de Projeto Strategy
-Casos de Teste:
    1. PAC (R$15 fixo)
    2. SEDEX (R$30 fixo)
    3. Transportadora (R$20 fixo)
-Tempo estimado: Red(10 min) Green(10 min) Refactor(25 min)
-Uso de I.A: https://chatgpt.com/share/6acb0706-8d78-83e9-b989-4518ad97edb8
"""

import pytest
from frete import CalculadoraFrete, FretePac, FreteSedex, FreteTransportadora

def test_frete_pac():
    calc = CalculadoraFrete(FretePac())
    assert calc.calcular() == 15.0

def test_frete_sedex():
    calc = CalculadoraFrete(FreteSedex())
    assert calc.calcular() == 30.0

def test_frete_transportadora():
    calc = CalculadoraFrete(FreteTransportadora())
    assert calc.calcular() == 20.0
