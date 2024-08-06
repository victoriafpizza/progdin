# Use the function below with the following numbers:
# a) 3 and 87
# b) 24 and 108
# c) 33, 45 and 99.
# d) 16 and 89.

"""O máximo divisor comum de dois números inteiros x e y pode ser calculado usando-se uma definição recursiva:
 mdc(x, y) = mdc(x - y, y) , se x > y
 mdc(x, y) = mdc(y,x)
 mdc(x, x) = x """

def mdc(x, y):
	if x == y:
		return x

	if x > y :
		return mdc(x - y, y)

	return mdc(y, x)