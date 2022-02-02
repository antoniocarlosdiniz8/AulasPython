'''import numpy as np
a = np.array([3, 5, 1, 2])
i_max = a.argmax()
i_min = a.argmin()
print(a)
print(f'O índice do maior valor é: {i_max}')
print(f'O índice do menor valor é: {i_min}')
print(f'O valor do maior elemento é: {a[i_max]}')
print(f'O valor do menor elemento é: {a[i_min]}')'''

valores = [3, 5, 1, 2]

maior = max(valores)
menor = min(valores)
print(valores)
print(f'O maior é: {maior}')
print(f'O menor é: {menor}')

print(f'O indice do maior é: {valores[max(valores)]}')
print(f'O índice do menor é: {valores[min(valores)]}')

