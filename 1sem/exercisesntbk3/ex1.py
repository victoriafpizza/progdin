# # Try yourself the above function, with the numbers: 2, 4,7. Set the results into an array.

""" 1. O fatorial de um número natural n é o produto de todos os inteiros positivos menores ou iguais a n.
   Crie a chamada recursiva de n fatorial"""

def fatorial(n):
	if n == 1:
		return 1

	return n* fatorial(n - 1)