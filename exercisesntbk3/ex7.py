#7 In text check points, we need to know how many times a certain digit appears within a number. 
#How to use recursion to operate over the number 1020345903?

"""Em uma função recursiva determine quantas vezes um digito k ocorre em um numero natural n."""

def conta_digito(d, n, i):
	n = str(n)
	d = str(d)

	if i == len(n):
		return 0

	if n[i] == d:
		return 1 + conta_digito(d, n, i + 1)

	return conta_digito(d, n, i + 1)