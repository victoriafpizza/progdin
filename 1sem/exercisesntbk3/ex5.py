#5 - Make yourself an input case for the function below.

"""Dado um array de inteiros, inverta a posição dos seus elementos"""

def inverte(a, i):
	if i == len(a) / 2:
		return a

	a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]
	return inverte(a, i + 1)