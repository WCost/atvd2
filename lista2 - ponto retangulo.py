class Ponto :
    def __init__(self, pontoX, pontoY):
        self.pontoX = pontoX
        self.pontoY = pontoY
    
    def  x(self):
        self.x = float(input ("Digite uma coordenda em X: "))

    def y(self):
        self.y = float(input("Digite uma coordenada em Y: "))

    def imprimir_valores(self):
        print("Os valores escolhidos para coordenada do ponto são:", self.x , "em X e ", self.y, "em Y")

class Retangulo:
    def __init__(self, base , altura) :
        self.base = base 
        self.altura = altura

    def mudarBase(self):
        novaBase = float(input("Para qual base deseja alterar?"))
        self.base = novaBase
        
    def mudarAltura(self):
        novaAltura = float(input("Digite a nova altura: "))
        self.altura = novaAltura

    def coordenadaxRet (self):
        metadeX = self.base / 2
        calculox = metadeX + ponto1.pontoX
        return calculox

    def coordenadayRet (self):
        metadeY = self.altura / 2
        calculoY = ponto1.pontoY + metadeY
        return calculoY
    
    def centroRet(self):
        print("As coordenadas do centro do retângulo são:", self.coordenadaxRet(), "em x e", self.coordenadayRet(), "em y")

ponto1 = Ponto( 0,0 )

coordenadaX = ponto1.x()
coordenadaY = ponto1.y()

vizu = input("Deseja ver as coordenadas do ponto? ('S' para sim e 'N' para não)")
if vizu in ['S', 's']:
    ponto1.imprimir_valores()
elif vizu in ['N','n']:
    pass
else:
    print("Digite uma opção válida!!")

base = float(input("Digite qual o valor da base do retangulo: "))
altura = float(input("Digite o valor da altura do retangulo: "))
retangulo1 = Retangulo(base, altura)

resposta1 = input("Deseja alterar a base? 'S' para sim e 'N' para não")
if resposta1 in ['S', 's']:
    retangulo1.mudarBase()
elif resposta1 in ['N', 'n']:
    pass
else :
    print ("Opção inválida")

resposta2 = input("Deseja alterar a altura? 'S' para sim e 'N' para não")
if resposta2 in ['S','s']:
    retangulo1.mudarAltura()
elif resposta2 in ['N', 'n']:
    pass
else :
    print ("Opção inválida")

verCentro = input("Deseja ver as  coordenadas do centro  do  retângulo?('S' para sim e 'N'  para não)")
if verCentro in ['S', 's']:
    retangulo1.centroRet()
elif verCentro in ['N', 'n']:
    pass
else :
    print("Digite uma opção válida!!")
