numeros = []
maior = menor = 0
for c in range(0, 5):
    numeros.append(int(input(f'Digite um numero  na posição: {c+1}º')))

    if c == 0:#Na posição zero ñ existe maior e nem menor:
        maior = numeros[c]#Por isso aqui ambos recebem o primeiro valor lido
        menor = numeros[c]
    else:
        if numeros[c] > maior:#Agora aqui se o programa ler um valor maior ele é guardado na variavel maior
            maior = numeros[c]
        if numeros[c] < menor:#Mesma coisa, se o programa ler um valor menor ele é guardado na variavel menor
            menor = numeros[c]
'''AMANHÃ CEDO DESENVOLVER QUE ÍNDICES ESTÃO MAIOR E MENOR'''
print(f'Sua lista: {numeros}')
print(f'O maior é {maior} e tá na posição: ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i+1}...')

print(f'O menor é: {menor} e tá na posição:', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i+1}...')













