listagem = []
maior = menor = 0

for i in range(0, 5):
    listagem.append(int(input('Digite um valor: ')))
    if i == 0:
        maior = menor = listagem[i]
    else:
        if listagem[i] > maior:
            maior = listagem[i]
        if listagem[i] < menor:
            menor = listagem[i]


print(f'Minha lista: {sorted(listagem)}')
print(f'O maior é: {maior}')
print(f'O menor é: {menor}')


