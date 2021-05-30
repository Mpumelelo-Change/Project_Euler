import math

broken = 0

for i in range (1, 1000):
    for j in range (1, 1000):

        k_2 = i**2 + j**2
        k = math.sqrt(k_2)

        if (int(k + 0.5) ** 2 == k_2) and (i + j + k == 1000):
            print (i*j*k)
            print (i, j, k)
            broken = 1
            break

    if (broken == 1):
        break
        
