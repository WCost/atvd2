class tamagushi:
    def __init__(self, nome , fome , saude , idade ) :
        self.nome = nome 
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, nomeNovo):
        nomeNovo = input("Qual será o novo nome do Tamagushi?  ")
        self.nome = nomeNovo
        return self.nome

    def alimentar (self): 
        alimento = int(input("O quanto deseja me alimentar? (Digite o número de 1 a 10)"))
        if 1<= alimento <= self.fome:
            self.fome = self.fome - alimento
            print("Obrigado por me alimentar, meu nível de fome está em ", self.fome)
        elif alimento > self.fome:
            print ("Minha fome não é tão grande, vou acabar ficando gordinho ")
        else:
            print("Escolha uma quantidade de alimento entre 1 e ", self.fome)

    def cuidar(self):
        remedio = int(input("O quanto deseja cuidar de mim? (Escolha um número de 1 a 10): "))
        if 1 <= remedio <= 10:  
            if self.saude == 10:
                 print("Minha saúde já está ótima!")
            else:
                 self.saude += remedio
                 print("Obrigado por cuidar de mim, minha saúde está em ", self.saude)
        else:
             print("Escolha uma quantidade de cuidado entre 1 e 10.")

    def humor(self, fome , saude ):
        if saude < 5 and fome > 5:
            print ("Estou  xoxo, capenga e tristonho ")
        elif saude < 5 and fome < 5 :
            print("Estou carente e querendo chameguinho ")
        elif saude > 5 and fome > 5 :
            print("Estou puto e bolado com a vida !!!")
        else :
            print("Eita como to de boa")

nome = input("Qual será o nome de seu Tamagushi?  ")
fome = int(input("Defina o nivel de fome de seu tamagushi(Digite um nível de 0 a 10)  "))
saude = int(input("Defina o nível de saúde de seu tamagushi(Escolha um nível de 0 a 10)  "))
idade = int(input("Quantos anos seu Tamagushi terá?  "))

bichinho1 = tamagushi(nome, fome, saude, idade)

print("Deseja alterar o nome do seu Tamagushi?")
resposta1 = input("Digite 'S' para sim ou 'N' para não:  ")
if resposta1 in ['S', 's']:
    bichinho1.alterar_nome(nome)
elif resposta1 in ['N', 'n']:
    pass
else:
    print("Opção inválida!!")

print ("Criação de tamagushi concluída!")
print ("Olá, sou seu tamagushi", bichinho1.nome, "muito prazer em conhecê-lo")

print ("Deseja me alimentar?")
resposta2 = input("Digite 'S' para sim e 'N' para não:  ")
if resposta2 in ['S', 's']:
    bichinho1.alimentar()
elif resposta2 in ['N', 'n']:
    pass
else:
    print("Opção inválida!!")

print ("Deseja cuidar da minha saúde?")
resposta3 = input("Digite 'S' para sim e 'N' para não:  ")
if resposta3 in ['S', 's']:
    bichinho1.cuidar()
elif resposta3 in ['N', 'n']:
    pass
else:
    print("Opção inválida!!")


print("Deseja saber como está meu humor?")
resposta4 = input("Digite 'S' para sim e 'N' para não:  ")
if resposta4 in ['S', 's']:
    bichinho1.humor(fome, saude)
elif resposta4 in ['N', 'n']:
    pass
else:
    print("Opção inválida!!")

print ("O resumo dos meus dados é:")
print ("Meu nome é: ", bichinho1.nome)
print ("Minha fome está no nível: ", bichinho1.fome)
print ("Minha saúde está no nível: ", bichinho1.saude)
print ("Tenho ", bichinho1.idade, " anos")

