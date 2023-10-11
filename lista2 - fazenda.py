import random

class Bichinho:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 10)
        self.saude = random.randint(0, 10)

    def humor(self):
        if self.saude < 5 and self.fome > 5:
            return f"{self.nome}: Estou xoxo, capenga e tristonho."
        elif self.saude < 5 and self.fome < 5:
            return f"{self.nome}: Estou carente e querendo chameguinho."
        elif self.saude > 5 and self.fome > 5:
            return f"{self.nome}: Estou puto e bolado com a vida!"
        else:
            return f"{self.nome}: Eita como tô de boa."

    def alimentar(self):
        self.fome -= 2
        if self.fome < 0:
            self.fome = 0

    def brincar(self):
        self.fome += 1
        self.saude += 1

def main():
    fazenda = []
    num_bichinhos = int(input("Quantos bichinhos você quer criar na fazenda? "))

    for i in range(num_bichinhos):
        nome = input(f"Nome do bichinho {i + 1}: ")
        fazenda.append(Bichinho(nome))

    while True:
        print("\nMenu:")
        print("1. Alimentar todos os bichinhos")
        print("2. Brincar com todos os bichinhos")
        print("3. Ouvir todos os bichinhos")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            for bichinho in fazenda:
                bichinho.alimentar()
        elif escolha == '2':
            for bichinho in fazenda:
                bichinho.brincar()
        elif escolha == '3':
            for bichinho in fazenda:
                print(bichinho.humor())
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")

if __name__ == "__main__":
    main()
