#Montar um programa, utilizando o for, que monte a tabuada do 2 ao 10.

for tabuada in range(11):
    for contador in range(11):  
        print(f'{tabuada} X {contador} = {tabuada*contador}')
    