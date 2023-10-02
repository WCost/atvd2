class quadrado :
    def __init__(self, lado):
        self.lado = lado

    def mudarValor(self):
        novoLado = input("Qual é o novo valor do lado de seu Quadrado? ")
        self.lado = novoLado

    def retornarValor(self):
        return self.lado
    
    def calcularArea(self):
        area = self.lado * self.lado
        return area

lado = float(input("Qual o valor do lado de seu Quadrado??"))
meuquadrado = quadrado(lado)
print ("Deseja alterar o valor do lado?")
resposta = input ("Digite 1 para sim e 2 para não")
if resposta == '1':
    meuquadrado.mudarValor()
elif resposta == '2':
    pass 
else :
    print("Digite uma opção válida!!")

print ("Deseja saber o valor do lado?")
resposta2 = input ("Digite 1 para sim e 2 para não")
if resposta2 == '1':
    print ("O valor  do lado é: ", meuquadrado.retornarValor())
elif resposta2 == '2':
    pass 
else :
    print("Digite uma opção válida!!")

print ("A área de seu quadrado é de:", meuquadrado.calcularArea())