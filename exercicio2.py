#Montar um programa que solicite 3 preços de um produto. O sistema deverá calcular a média dos preços. Os valores digitados não poderão ser valores negativos.

def PedirPreco(frase):
    while True:
        preco = float(input(frase))
        if preco >= 0:
            break
    return preco
    
preco1 = PedirPreco("Digite o preço do 1º Produto: ")
preco2 = PedirPreco("Digite o preço do 2º Produto: ")
preco3 = PedirPreco("Digite o preço do 3º Produto: ")


mediaPreco = (preco1+preco2+preco3) / 3
print(f"A média de preços é {mediaPreco:,.2f}")