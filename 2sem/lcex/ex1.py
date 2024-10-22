# Fatorial de uma lista de numeros
# Problemas: dada uma lista de numeros inteiros, retorne uma nova lista contendo o fatorial de cada numero

import math 
nums = [5,2,4,6]
fact = [math.factorial(num) for num in nums]
print(fact)