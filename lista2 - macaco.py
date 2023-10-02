class Macaco():
    def __init__(self, nome, bucho ):
        self.nome = nome
        self.bucho = bucho

    def comer(self):
        pass

    def verBucho(self):
        pass

    def digerir(self):
        pass

nome1 = input("Qual o nome do primeiro macaco? ")
bucho1 = 0
nome2 = input("Qual o nome do segundo macaco? ")
bucho2 = 0  
macaco1 = Macaco(nome1 , bucho1)
macaco2 = Macaco(nome2 ,bucho2)

banana = 5
melao = 3
goiaba = 1

print("Deseja alimentar qual macaco?")
resposta1= int(input("Digite 1 para o primeiro e 2 para o segundo"))
if  resposta1 == 1:
    pass
elif resposta1 == 2:
    pass
else:
    print ("Digite uma opção válida!!")