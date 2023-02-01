import os
os.system('cls')
class Produto: 
    def __init__(self,nome,preco,estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    def exibir (self):
        print(f"Nome: {self.nome} -Preco: {self.preco}")
produto = Produto("Massa de pizaa",5,400)
produto.exibir()

quantidade = int(input("Informe a quantidade: "))
