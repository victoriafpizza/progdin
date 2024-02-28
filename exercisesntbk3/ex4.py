#4 - In a commercial operation, we need to compute the multiplication of numbers. 
# Let´s start with the multiplication of the number by 'n' times. 
# The first number will be basis, and the second will be the exponent. 
# Use the function below to create an array with 5 items: 3 and 2, 3 and 4, 2 and 5, 5 and 3, 3 and 2. 
# The array shall have the numbers in reverse order.

"""implemente uma função reccursiva que, dados dois números inteiros x e n, calcula o valor de x ** n"""

def exponencial(x, n):
	if n == 0:
		return 1

	return x * exponencial(x, n - 1)