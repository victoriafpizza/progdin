# Exercise # 3 - Using the function below, make a function to make an array from two previous lists. 
#The first shall consider the sum of the numbers up to 12. The second list shall take the sum of the numbers up to 7. 
# The target array shall have the second result first.

"""Usando recursividade, calcule a soma de todos os valores de um array de reais"""

def soma(a, n):
	if n == len(a):
		return 0

	return a[n] + soma(a, n + 1)