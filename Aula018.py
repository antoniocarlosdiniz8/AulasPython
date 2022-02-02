mylist = []
maior = menor = 0

for c in range(0, 5):
    mylist.append(int(input(f'Digite um numero para a posição: {c} ')))
    if c == 0:
        menor = maior = mylist[c]
    else:
        if mylist[c] > maior:
            maior = mylist[c]
        if mylist[c] < menor:
            menor = mylist[c]

print(f'Lista digitada: {mylist}')
print(f'O maior da lista é: {maior} e esta na posição...', end='')
for i, v in enumerate(mylist):
    if v == maior:
        print(f'{i}')
print(f'O menor da lista é: {menor} e está na posição...', end='')
for i, v in enumerate(mylist):
    if v == menor:
        print(f'{i}')


