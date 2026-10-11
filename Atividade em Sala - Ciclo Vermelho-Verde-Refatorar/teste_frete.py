"""
-Plano: Calculadora de frete para e-commerce.
-Padrão de Projeto Strategy
-Casos de Teste:
    1. PAC (R$15 fixo)
    2. SEDEX (R$30 fixo)
    3. Transportadora (R$20 fixo)
-Tempo estimado: Red(10 min) Green(10 min) Refactor(25 min)
-Uso de I.A: 
"""

import pytest
from frete import CalculadoraFrete

def test_frete_pac():
    calc = CalculadoraFrete()
    assert calc.calcular(10.0, "PAC") == 15.0

def test_frete_sedex():
    calc = CalculadoraFrete()
    assert calc.calcular(10.0, "SEDEX") == 30.0

def test_frete_transportadora():
    calc = CalculadoraFrete()
    assert calc.calcular(10.0, "Transportadora") == 20.0