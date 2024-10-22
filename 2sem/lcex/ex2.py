#Problema: dada uma lista de numeros inteiros, crie uma nova lista contendo o somatorio de todos os subarrays continuos de tamanho k
#subarrays consecutivos
 
k = 3 
nums = [2,6,8,5,3,4,7]
sum = [sum(nums[i:i+k] for i in range(len(nums - k + 1)))]
sum 