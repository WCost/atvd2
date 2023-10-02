class tv:
    def __init__(self, canal , volume) :
        self.canal = canal
        self.volume = volume

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal
        return self.canal

    def aumentar_volume(self, volume ):
        if volume < 100:
            self.volume =self.volume + 1
            return self.volume
        else:   
            print ("no  volume máximo")

    def diminuir_volume(self, volume ):
        if volume>0:
            self.volume = self.volume - 1
            return self.volume
        else:
            print("no volume mínimo")    

canal = input("A qual canal deseja assistir?")
volume = int(input("Qual deseja que seja o  volume? (De 0 a 100)"))
tv1 = tv(canal, volume)

print("Deseja alterar o canal ?")
resposta1 = input("Digite 'S' para sim e 'N' para não: ")
if resposta1 in ['S', 's']:
    novo_canal = input("Qual canal deseja assistir? ")
    tv1.mudar_canal(novo_canal)
elif resposta1 in ['N', 'n']:
    pass
else:
    print("Digite  uma opção válida!!")

print ("Deseja mudar o volume ?")
resposta2 = input("Digite 'S' para sim e 'N' para não: ")
if resposta2 in ['S', 's']:
    print ("Deseja aumentar ou diminuir o volume?")
    resposta3 = input("Digite 'A' para aumentar e 'D' para diminuir: ")
    if resposta3 in ['A', 'a']:
        tv1.aumentar_volume(volume)
    elif resposta3 in ['D', 'd']:
        tv1.diminuir_volume(volume)
    else:
        print("Opção inválida!!")
elif resposta1 in ['N', 'n']:
    pass
else:
    print ("Digite uma opção válida!!")

print("A televisão está no canal ", tv1.canal, " e o volume está em ", tv1.volume)