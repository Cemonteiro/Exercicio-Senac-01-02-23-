import os
os.system('cls')
class Produto: 
    def __init__(self,nome,preco,estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
produto = Produto("Massa de pizaa",5,400)
quantidade = int(input("Informe a quantidade: "))
print(quantidade)