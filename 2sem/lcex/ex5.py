# Soma maxima de subsequencia não adjacente 
# Problema: dada ums lista de inteiros, contore a soma maxima de uma subsequencia não adjacente. 

zahl = [3, -2,5 -6,4,1,7]
dp = [0] * (len(zahl)+1)
[dp.append(max(dp[i],dp[i-1]+zahl[i-1])) for i in range(2,len(zahl)+1)]