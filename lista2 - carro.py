class Carro:
    def __init__(self, gasolina=0):
        self.gasolina = gasolina

    def abastecer(self):
        gasoAbastecer = float(input("Digite quantos litros de gasolina deseja colocar no tanque: "))
        self.gasolina += gasoAbastecer
        print(f"O tanque agora contém {self.gasolina} litros de gasolina.")

    def andar(self):
        qtsKM = float(input("Quantos Km deseja andar? "))
        consumo = float(input("Qual o consumo de gasolina do seu carro? "))
        gasto = consumo * qtsKM
        if gasto <= self.gasolina:
            self.gasolina -= gasto
            print(f"Você percorreu {qtsKM} Km. O tanque agora contém {self.gasolina} litros de gasolina.")
        else:
            print("É impossível percorrer essa distância com a quantidade de gasolina disponível.")

    def obterGasolina(self):
        print(f"A quantidade de gasolina disponível no tanque é de: {self.gasolina} litros.")


gasolina = 0
carro1 = Carro(gasolina)

while True:
    opcao = input("Escolha uma opção: 'A' para abastecer, 'C' para andar, 'V' para ver o tanque, ou 'D' para desligar: ")
    
    if opcao in ['A', 'a']:
        carro1.abastecer()
    elif opcao in  ['C', 'c']:
        carro1.andar()
    elif opcao in ['V', 'v']:
        carro1.obterGasolina()
    elif opcao in ['D', 'd']:
        break
    else:
        print("Opção inválida. Tente novamente.")

print("O carro morreu")
