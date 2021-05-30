"""
smp_n = 1

for i in range(1,11):
    #print(i)
    if (smp_n % i != 0):
        while (smp_n % i != 0):
            smp_n *= i

print(smp_n)
"""

arr_2 = [8, 7, 9, 10, 11, 13, 17, 19]

arr = [4, 7, 9, 10]
prod = 1

for i in arr_2:
    prod *= i

print(prod)
            
