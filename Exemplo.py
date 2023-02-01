import os
os.system('cls')
class Produto: 
    def __init__(self,nome,preco,estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    def exibir (self,indice = 0):
        print(f"{indice} === Nome: {self.nome} - Preco: {self.preco}")
produto_um = Produto("Massa de pizaa",5,400)
produto_dois = Produto("Tomate",2,100)

produtos = [produto_um,produto_dois]
for produto in produtos:
    indice = produtos.index(produto)
    produto.exibir(indice)
indice_selecionado = int(input("Selecione o produto: "))
if indice_selecionado > len(produtos):
    print("Produto inexistente")
else:
    produto = produtos [indice_selecionado]
    quantidade = int(input("Informe a quantidade: "))
    print(f"O valor total é R$ {quantidade * produto.preco}")


quantidade = int(input("Informe a quantidade: "))
print(f"o valor total é: R$ {quantidade} * {produto.preco}")
