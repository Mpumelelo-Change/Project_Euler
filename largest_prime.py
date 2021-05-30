import math

def is_prime(num) :

    start = 2

    while (start < num):
        if (num % start == 0):
            return False
        else:
            start += 1

    return True


num = 600851475143
tmp = 3
stor = [1, 2]

for i in range(50000):
    if (is_prime(tmp)):
        if (num % tmp == 0):
            stor.append(tmp)
    tmp += 1

stor.append(num/stor[-1])
print(stor)
