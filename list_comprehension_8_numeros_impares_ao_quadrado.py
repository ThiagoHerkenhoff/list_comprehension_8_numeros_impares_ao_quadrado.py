"""
Dada uma lista de números, crie uma nova lista que contenha o quadrado de cada
número que seja ímpar.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Requisito: Utilize list comprehension para gerar a nova lista.

"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

impares_quadrado = [num ** 2 for num in numeros if num % 2 != 0]

print(impares_quadrado)