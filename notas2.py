while True: 
    nota1bim = float(input("Digite a nota do 1º Bimestre: "))
    if (nota1bim <= 10) and (nota1bim >= 0):
        break 

while True:
    nota2 = float(input("Digite a nota do 2º Bimestre: "))
    if nota2 <= 10 and nota2 >= 0:
        break

while True:
    nota3 = float(input("Digite a nota do 3º Bimestre: "))
    if nota3 <= 10 and nota3 >=0:
        break

while True:   
    nota4 = float(input("Digite a nota do 4º Bimestre: "))
    if nota4 <= 10 and nota4 >= 0:
        break

media = (nota1bim + nota2 + nota3 + nota4)/4

print(f"Sua média é {media:,.2f}")

if (media >= 5):
    print("Aluno A P R O V A D O !!!")
elif (media >= 3):
    print("Aluno em Recuperação")    
else:
    print("Aluno R E P R O V A D O !!!")    

print("Fim do ano letivo !")
