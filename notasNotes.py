#Entrada de dados
nota1bim = float(input("Digite a nota do 1º Bimestre: "))
nota2bim = float(input("Digite a nota do 2º Bimestre: "))
nota3bim = float(input("Digite a nota do 3º Bimestre: "))
nota4bim = float(input("Digite a nota do 4º Bimestre: "))

#Processamento de dados
media = (nota1bim+nota2bim+nota3bim+nota4bim) / 4

#Análise de Condição
if media >= 5:
    print("Aluno Aprovado!")
elif media >= 3:
    print("Aluno em Recuperação") 
else:
    print("Aluno Reprovado!")       

    #Podemos ter comandos com IF, ELIF e ELSE, apenas com IF e ELIF, com vários ELIF, OU sem o ELSE. ELSE é o final, não precisa de condição.

    #Comando While (enquanto) - While True (enquanto for verdade) - ou while 1==1 - BREAK, só para quando a condição é verdadeira
while True: 
    nota1bim = float(input("Digite a nota do 1º Bimestre: "))
    if (nota1bim <= 10) and (nota1bim >= 0):
        break    

while True:
    nota2bim = float(input("Digite a nota do 2º Bimestre: "))
    if (nota2bim <= 10) and (nota2bim >= 0):
        break

while True:
    nota3bim = float(input("Digite a nota do 3º Bimestre: "))
    if (nota3bim <= 10) and (nota3bim >=0):
        break

while True:   
    nota4bim = float(input("Digite a nota do 4º Bimestre: "))
    if (nota4bim <= 10) and (nota4bim >= 0):
        break

#OU
#Criar comando "def" um comando personalizado

def PedirNota(frase):
    while True:
        nota = float(input(frase))
        if nota >= 0 and nota <= 10:
            break
    return nota
    
nota1bim = PedirNota("Digite a nota do 1º Bimestre: ")
nota2bim = PedirNota("Digite a nota do 2º Bimestre: ")
nota3bim = PedirNota("Digite a nota do 3º Bimestre: ")
nota4bim = PedirNota("Digite a nota do 4º Bimestre: ")

media = (nota1bim+nota2bim+nota3bim+nota4bim) / 4
print(f"Sua média é {media:,.2f}")

if media >= 5:
    print("Aluno Aprovado!")
elif media >= 3:
    print("Aluno em Recuperação") 
else:
    print("Aluno Reprovado!")  

    