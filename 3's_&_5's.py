def is_div(num):
    if (num % 3 == 0):
        return num
    if (num % 5 == 0):
        return num
    else :
        return 0

num = 999
total = 0

while (num > 0):
    total = total + is_div(num)
    num -= 1

print(total)
    
