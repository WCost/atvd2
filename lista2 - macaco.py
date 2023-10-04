class Macaco():
    def __init__(self, nome, bucho, capacidadeBucho):
        self.nome = nome
        self.bucho = bucho
        self.capacidadeBucho = capacidadeBucho

    def comer(self, comida):
        if self.bucho + comida <= self.capacidadeBucho:
            self.bucho += comida
        else:
            print("O macaquinho explodiu de tanto comer !!!")

    def verBucho(self):
        espaco_disponivel = self.capacidadeBucho - self.bucho
        print("O espaço disponível no estômago de", self.nome, "é de:", espaco_disponivel)

    def digerir(self):
        if self.bucho > 0 :
            self.digerir = self.bucho - dig
            print("Foi digerido", dig)
        else:
            print("Este macaco já está com o estomago vazio")


nome1 = input("Qual o nome do primeiro macaco? ")
bucho1 = 0
nome2 = input("Qual o nome do segundo macaco? ")
bucho2 = 0
capacidadeBucho = 10
capacidadeBucho1 = 10
capacidadeBucho2 = 10
macaco1 = Macaco(nome1, bucho1, capacidadeBucho1)
macaco2 = Macaco(nome2, bucho2, capacidadeBucho2)

banana = 2
melao = 3
goiaba = 1
pesoMacaco = 5


# Alimentar macaco 1 #
print("Deseja alimentar o macaco ", macaco1.nome, "?")
resposta1 = input("digite 'S' para sim e 'N' para não")
if resposta1 in ['S', 's']:
    while True:
        qualFruta = input("Deseja dar qual alimento para " + macaco1.nome + "? (Banana - 'B', Melão - 'M', Goiaba - 'G', ou 'S' para sair): ")
        if qualFruta in ['B', 'b']:
            comida = banana
        elif qualFruta in ['M', 'm']:
            comida = melao
        elif qualFruta in ['G', 'g']:
            comida = goiaba
        elif qualFruta in ['S', 's']:
            break 
        else:
            print("Opção inválida! Tente novamente.")
            continue
        macaco1.comer(comida)
elif  resposta1 in ['N', 'n']:
    pass
else :
    print("Digite uma opção válida")
# Alimentar macaco 2 #
print("Deseja alimentar o macaco ", macaco2.nome, "?")
resposta2 = input("digite 'S' para sim e 'N' para não")
if resposta2 in ['S', 's']:
    while True:
        qualFruta = input("Deseja dar qual alimento para " + macaco2.nome + "? (Banana - 'B', Melão - 'M', Goiaba - 'G', ou 'S' para sair): ")
        if qualFruta in ['B', 'b']:
            comida = banana
        elif qualFruta in ['M', 'm']:
            comida = melao
        elif qualFruta in ['G', 'g']:
            comida = goiaba
        elif qualFruta in ['S', 's']:
            break  # Sair do loop
        else:
            print("Opção inválida! Tente novamente.")
            continue

        macaco2.comer(comida)
elif resposta2 in ['N', 'n']:
    pass
else:
    print("Digite uma opção válida!")


# Verificar o quanto o bucho do macaquinho1 está cheio
print ("Deseja ver como está o estomago do", macaco1.nome,"?")
vizu1 = input("Sim - 'S', Não - 'N'")
if vizu1 in ['S', 's']:
    macaco1.verBucho()
elif vizu1 in ['N', 'n']:
    pass
else:
    print("Digite uma opção válida!!")


# Verificar o quanto o bucho do macaquinho2 está cheio
print ("Deseja ver como está o estomago do", macaco2.nome,"?")
vizu2 = input("Sim - 'S', Não - 'N'")
if vizu2 in ['S', 's']:
    macaco2.verBucho()
elif vizu2 in ['N', 'n']:
    pass
else:
    print("Digite uma opção válida!!")

#Digerir macaquinho1
print("deseja digerir do estomago do macaco", macaco1.nome, "?")
digerir1  = input("Digite 'S' para sim e 'N' para não")
if digerir1 in ['S', 's']:
    dig = int(input("Digite um número entre 0 e " + str(macaco1.bucho) + ": "))
    macaco1.digerir()
elif digerir1 in ['N', 'n']:
    pass
else:
    print("Digite uma opção  inválida")

#Digerir macaquinho2
print("deseja digerir do estomago do macaco", macaco2.nome, "?")
digerir2  = input("Digite 'S' para sim e 'N' para não")
if digerir2 in ['S', 's']:
    dig = int(input("Digite um número entre 0 e " + str(macaco2.bucho) + ": "))
    macaco2.digerir()
elif digerir1 in ['N', 'n']:
    pass
else:
    print("Digite uma opção  inválida")

if macaco1.bucho == 0:
    print("O macaco", macaco1.nome, "deseja comer o macaco", macaco2.nome, ". Aceita isso?")
    canibal = input("Digite 'S' para sim e 'N' para não")
    if canibal in ['S', 's']:
        print("O ", macaco2.nome, "Virou sopa de macaco!!")
    elif canibal in ['N', 'n']:
        pass
    else:
        print("Digite uma opção válida!!")
else:
    pass

if macaco2.bucho == 0:
    print("O macaco ", macaco2.nome, "deseja comer o macaco", macaco1.nome, ". Aceita isso?")
    canibal = input("Digite 'S' para sim e 'N' para não")
    if canibal in ['S', 's']:
        print("O ", macaco1.nome, "Virou sopa de macaco!!")
    elif canibal in ['N', 'n']:
        pass
    else:
        print("Digite uma opção válida!!")
else:
    pass
