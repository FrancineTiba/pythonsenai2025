#Montar um programa que solicite 3 preços de um produto. O sistema deverá calcular a média dos preços. Os valores digitados não poderão ser valores negativos.

while True: 
    preco1 = float(input("Digite o valor do 1º Produto: "))
    if (preco1 >= 0):
        break 

while True: 
    preco2 = float(input("Digite o valor do 2º Produto: "))
    if (preco2 >= 0):
        break     

while True: 
    preco3 = float(input("Digite o valor do 3º Produto: "))
    if (preco3 >= 0):
        break     

mediaPreco = (preco1+preco2+preco3) / 3
print(f"A média de preços dos produtos é: {mediaPreco:,.2f}")

#Repetir 3 vezes o comando, (while), é aceitável, mas não profissional.


   

