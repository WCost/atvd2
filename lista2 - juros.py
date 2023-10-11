class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros / 100  

    def adicioneJuros(self):
        juro = self.saldo * self.taxa_juros
        self.saldo += juro

conta_poupanca1 = ContaInvestimento(1000.00, 10.0)

for _ in range(5):
    conta_poupanca1.adicioneJuros()

print(f"Saldo final após aplicar juros é de {conta_poupanca1.saldo:.2f} reais")
