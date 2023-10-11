class Funcionario:
    def __init__(self, nome , salario):
        self.nome  = nome 
        self.salario = salario
    
    def nomear (self):
        print("olá, boa tarde", nome)

    def pagar(self):
        print("Seu salário é de:", salario, "reais")

    def aumentarSal(self):
        aumento = float(input("Qual a porcentagem que deseja  aumentar o salário?"))
        porcentagem = aumento/100
        novoSal = salario * porcentagem + salario
        print("Com o aumento, o novo salário do funcionário é de: ", novoSal, "reais")

nome = input("Olá, digite seu nome: ")
salario = float(input("Digite seu salário"))
pessoa1 = Funcionario(nome, salario)
pessoa1.nomear()
pessoa1.pagar()
resposta  = input("Deseja aumentar o salario do funcionario? 'S' para sim e 'N' para não")
if resposta in ['s', 'S']:
    pessoa1.aumentarSal()
elif resposta in ['n', 'N']:
    pass
else:
    print("Digite uma opção válida!!")
