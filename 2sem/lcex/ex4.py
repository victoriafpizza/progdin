#Filtrando numeros pares em subsequencias
#problema. dada uma lista de listas, retome uma nova lista contendo apenas os numeros pares de cada sublista

listg = [[1,2,3],[4,5,6],[6,7,8]]
listg = [[num for num in sub if num % 2 == 0] for sub in listg]
litg