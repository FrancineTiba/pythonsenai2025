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