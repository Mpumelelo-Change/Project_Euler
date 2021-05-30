#Upper Limit 810000 = 999 * 999
#Lower Limit 10000 = 100 * 100

def is_palindrome(num):
    num_str = str(num)

    if (num_str[0] == num_str[-1]):
        if (num_str[1] == num_str[-2]):
            if (num_str[2] == num_str[-3]):
                return True

    return False

candid8 = 799997
pro_1 = 999
pro_l = 100

while (candid8 >= 100001):
    print(candid8)
    if (is_palindrome(candid8)):
        print("Hell Yeah!!")
        pro_1 = 999
        while (pro_1 >= pro_l):
            print(pro_1)
            if (candid8 % pro_1 == 0):
                print(pro_1)
                print(candid8 / pro_1)
                print(candid8)
                break
            pro_1 -= 1
    candid8 -= 1
