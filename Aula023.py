vel = int(input('Digite a velocidade atual do carro.'))

if(vel >= 80):
    tm = (vel - 80) * 7
    print(f'Voçê foi multado e vai pagar {tm:.2f} R$ de multa.')
else:
    print('Tenha um bom dia, Dirija com segurança:')
