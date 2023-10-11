class Bomba_de_combustível:
    def __init__(self, tipoCombustivel, valorLitro, qtdCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.qtdCombustivel = qtdCombustivel

    def abastecerPorValor(self):
        valor = float(input("Digite o valor que quer abastecer: "))
        if self.tipoCombustivel == 1:
            total = valor / self.valorLitro
            print(f"Você abasteceu {total} litros de etanol")
        elif self.tipoCombustivel == 2:
            total = valor / self.valorLitro
            print(f"Você abasteceu {total} litros de gasolina")
        elif self.tipoCombustivel == 3:
            total = valor / self.valorLitro
            print(f"Você abasteceu {total} litros de gasolina aditivada")

    def abastecerLitro(self):
        litros = float(input("Digite a quantidade de litros que deseja abastecer: "))
        valor = litros * self.valorLitro
        print(f"Você abasteceu R${valor:.2f}")
    
    def alterarValor(self):
        novoValor = float(input("Digite o  novo valor do litro: "))
        self.valorLitro = novoValor
        return self.valorLitro
    
    def alterarCombustivel(self):
        novoCombustivel = int(input("Para qual combustível deseja alterar? 1 para gasolina, 2 para etanol, 3 para aditivada: "))
        if novoCombustivel in [1, 2, 3]:
            self.tipoCombustivel = novoCombustivel
            print("Tipo de combustível alterado com sucesso.")
            return self.tipoCombustivel
        else:
            print("Digite uma opção válida!!")

        
tipoCombustivel = int(input("Digite o tipo de combustível: 1 - etanol, 2 - gasolina, 3 - gasolina aditivada "))
valorLitro = float(input("Digite o valor por litro: "))
qtdCombustivel = 1000
bomba1 = Bomba_de_combustível(tipoCombustivel, valorLitro, qtdCombustivel)

while True:
    forma = int(input("Deseja abastecer de que forma? 1 - por litro, 2 - por valor, 3 - sair: "))
    if forma == 1:
        bomba1.abastecerLitro()
    elif forma == 2:
        bomba1.abastecerPorValor()
    elif forma == 3:
        break
    else:
        print("Digite uma opção válida!!")
        continue
    nvValor = int(input("Deseja alterar o  valor do preço do litro? 1para sim 2 para não"))
    if nvValor==1:
        bomba1.alterarValor()
    elif nvValor==2:
        pass
    else:
        print("Digite uma opção váloda!!")
        continue
    nvCombustivel = int(input("Deseja alterar o tipo de combustível? 1 para sim, 2 para não: "))
    if nvCombustivel == 1:
        bomba1.alterarCombustivel()
    elif nvCombustivel == 2:
        pass
    else:
        print("Digite uma opção válida!!")
        continue
