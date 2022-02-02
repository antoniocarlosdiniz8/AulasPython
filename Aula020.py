lista = []
maior = menor = 0
for i in range(0, 5):
    lista.append(int(input('Digite um numero:')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
print(f'Minha lista: {sorted(lista)}')
print(f'O maior é: {maior} \nO menor é: {menor}')
print('Oi eu sou\t')
print('gohu\t')

