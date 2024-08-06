#6 We have the following array: [2,3,5,8,12,32,4,5,10,11]. Using recursion, how the array order can be inverse?

"""Dado um array de inteiros inverta a posição dos seus elementos"""

def inverte(a, i):
	if i == len(a) / 2:
		return a

	a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]
	return inverte(a, i + 1)