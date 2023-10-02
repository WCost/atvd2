class Circulo:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self):
        nova_cor = input("Qual deseja que seja a nova cor?")
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor

cor = input("Qual a cor do círculo?")
circunferencia = float(input("Qual a circunferência do círculo?"))
material = input("Qual o material do seu círculo?")
circulo = Circulo(cor, circunferencia, material)

print("Deseja alterar a Cor do seu círculo?")
resposta = int(input("Digite 1 para sim e 2 para não"))
if resposta == 1:
    circulo.trocaCor()
elif resposta == 2:
    pass
else:
    print("Digite uma opção válida!!")

print("Deseja saber a cor do seu círculo?")
resposta2 = input("Digite 1 para sim e 2 para não")
if resposta2 == "1":
    print("A cor do seu círculo é:", circulo.mostraCor())
elif resposta2 == "2":
    pass
else:
    print("Digite uma opção válida!!")

