#rota = ['MARUAGA', 'SINGOLARE', 'MAGISTRAL', 'BRUNCH', 'CARITÓ', 'SACCARO', 'BRILANTE']

rota = []

while True:
    cliente = str(input('Digite um cliente:'))
    rota.append(cliente)
    resp = str(input('Quer continuar? S/N')).upper()[0].strip()
    if resp in 'N':
        break

print('CARREGAMENTO 1025 TARDE 26-12-2021')
print('PHR-2H05')

print('motorista:')
print('ajudante: ')

print(f'{"km inicial:"} ')
print(f'{"hora inicial:"}')
for i, v in enumerate(rota):
    print(f'{i+1}. {v.upper()}')

print('HORA FINAL')
print('KM FINAL')








