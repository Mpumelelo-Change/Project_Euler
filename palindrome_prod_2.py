def is_palindrome(num):
    num_str = str(num)

    if (num_str[0] == num_str[-1]):
        if (num_str[1] == num_str[-2]):
            if (num_str[2] == num_str[-3]):
                return True

    return False


candid8 = 990099
pro1 = 999
pro2 = 100
count = 0

while (candid8 >= 100001):
    if (is_palindrome(candid8)):
        print(candid8)
        pro1 = 999
        while (pro1 >= pro2):
            if (candid8 % pro1 == 0):
                print(pro1)
                print(candid8 / pro1)
                print(candid8)
                break
            pro1 -= 1
    if (count != 10 and count > -1):
        candid8 -= 1100
        count += 1
    elif (count == 10):
        candid8 -= 10010
        count = -1
    elif (count == -1):
        candid8 -= 11
        count == 0
    
