n = int(input())
sum = 0
for i in range (1, n):
    sum +=  i * (i + 1)
for i in range (1, n - 1):
    print(i, '*', (i + 1), '+', sep = '', end = '')
    
print((n -1), '*',n , '=', sum, sep = '')