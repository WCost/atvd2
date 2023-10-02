class conta_corrente:
    def __init__(self, numeroConta, nome , saldo) :
       self.numeroConta = numeroConta
       self.nome = nome
       self.saldo = saldo
    
    def alterarNome(self, novoNome):
        self.nome = novoNome 
        return self.nome
    
    def deposito(self, dinheiroDeposito):
        self.saldo = self.saldo + dinheiroDeposito
        return self.saldo

    def saque(self, dinheiroSaque):
        if saldo >= dinheiroSaque:
            self.saldo = self.saldo - dinheiroSaque
            return self.saldo
        else:
            print("Saldo insuficiente!!")
        

numeroConta = input("Digite o número da Conta: ")
nome = input("Digite o nome do  correntista: ")
saldo = float(input("Digite o saldo inicial: "))

conta1 = conta_corrente (numeroConta, nome, saldo)
print("Deseja alterar o nome do correntista? ")
resposta2 = input("Digite 'S' para sim e 'N' para não")
if resposta2 in ['S', 's']:
    novoNome = input("Qual o novo nome do correntista? ")
    print ("Nome alterado  com sucesso, o novo nome do correntista é", novoNome)
elif resposta2 in ['N', 'n']:
    pass
else:
    print("Opção inválida!!")

print("Deseja realizar um saque ou depósito? ")
resposta = input("Digite 'S' para saque e 'D' para depósito:")

if resposta in ['S' , 's']:
    dinheiroSaque = float(input("Qual o valor do saque? "))
    novoSaldo = conta1.saque(dinheiroSaque)
    if saldo > dinheiroSaque:
        print("Saque realizado, seu saldo é de:", novoSaldo)
elif resposta in ['D', 'd'] :
    dinheiroDeposito = float(input("Qual o valor do depósito?"))
    novoSaldo= conta1.deposito(dinheiroDeposito)
    print ("Depósito realizado com sucesso, seu saldo é de:", novoSaldo)
else:
    print("Digite uma opção válida!!")
