class retangulo :
    def __init__(self, base , altura):
        self.base = base
        self.altura = altura
    def mudarValorBase(self):
        novabase = float(input("Qual o valor da nova base? "))
        self.base = novabase
    def mudarValorAltura(self):
        novaaltura = float(input("Qual o valor da nova altura? "))
        self.altura = novaaltura
    def area(self):
        area = self.base * self.altura
        return area
    def perimetro(self):
        alturas = self.altura * 2
        bases = self.base * 2
        Perimetro = alturas + bases
        return Perimetro 

base= float(input("Qual o valor da base do retângulo? "))
altura = float(input("Qual a altura de seu retângulo?"))
meuretangulo = retangulo(base,altura)

resposta1 = int(input("Deseja alterar a base? 1 para sim e 2 para não"))
if resposta1 == 1:
    meuretangulo.mudarValorBase()
elif resposta1 == 2:
    pass
else :
    print ("Opção inválida")

resposta2 = int(input("Deseja alterar a altura? 1 para sim e 2 para não"))
if resposta2 == 1:
    meuretangulo.mudarValorAltura()
elif resposta2 == 2:
    pass
else :
    print ("Opção inválida")

print ("A área do retângulo é de: ", meuretangulo.perimetro(), " metros")
print ("Já a área é de: " , meuretangulo.area(), " metros quadrados")

pisos = float(input("Digite qual a medida do piso que utilizará, em metros : "))
rodape = float(input("Digite qual a largura dos rodapés que utilizará, em metros : "))

qtdPisos = meuretangulo.area() / pisos
qtdRodape = meuretangulo.perimetro() / rodape

print ("A quantidade de pisos utilizados é de :{:.2f}".format(qtdPisos ))
print ("A quantidade de rodapés utilizados é de :{:.2f}".format(qtdRodape))