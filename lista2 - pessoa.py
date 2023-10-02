class Pessoa:
    def __init__(self, nome,idade ,peso ,  altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade = self.idade + 1 
        return self.idade

    def engordar(self, pesoGanho):
        self.peso = self.peso + pesoGanho
        return self.peso

    def emagrecer(self, pesoPerdido):
        self.peso = self.peso - pesoPerdido
        return self.peso

    def crescer(self):
       self.altura = self.altura + 0.05
       return self.altura

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

pessoa1 = Pessoa(nome, idade, peso, altura)
resposta = input("Deseja envelhecer? Digite 1 para sim e 2 para não: ")
resposta2 = input ("Deseja engordar? Digite 1 para sim e 2 para não: ")
resposta3 = input ("Deseja emagrecer? Digite 1 para sim e 2 para não: ")

if resposta == '1':
    if pessoa1.idade < 22:
        print("Sua idade é:" , pessoa1.envelhecer(), "anos")
        print("Sua altura é de:", pessoa1.crescer(), "metros")
    else:
        print("Sua idade é de:", pessoa1.envelhecer())
        print ("e sua altura é de :", altura)
elif resposta == '2':
    pass
else:
    print ("Digite uma opção válida!")

if resposta2 == '1':
    pesoGanho =  float(input("Digite quanto peso ganhou: "))
    print("Seu novo peso é de:", pessoa1.engordar(pesoGanho), "kg")
elif resposta2 == '2':
    pass
else : 
    print ("Digite uma opção válida!")

if resposta3 == '1':
    pesoPerdido = float(input("Digite quanto peso perdeu: "))
    print("Seu novo peso é de" , pessoa1.emagrecer(pesoPerdido), "kg")
elif resposta3 == '2':
    pass
else :
    print("Digite uma opção válida!")