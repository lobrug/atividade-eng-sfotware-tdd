class CalculadoraFrete:
    def calcular(self, peso, tipo_frete):
        if tipo_frete == "PAC":
            return 15
        elif tipo_frete == "SEDEX":
            return 30
        elif tipo_frete == "Transportadora":
            return 20