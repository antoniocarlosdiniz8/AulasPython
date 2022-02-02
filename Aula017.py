numeros = []

while True:
    n = int(input('Digite um numero:'))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Numero já adicionado. gigite outro.')
    resp = str(input('Quer conitunuar, S/N')).strip().upper()[0]
    if resp in 'Nn':
        break
print(f'my list: {numeros}')

