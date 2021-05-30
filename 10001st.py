def gen_next_prime(prim_arr):

    cndd8 = prim_arr[-1] + 1
    count = 0
    check = 0

    while(check == 0):
        for i in prim_arr:
            if (cndd8 % i == 0):
                count = 0
                cndd8 += 1
                break
            else:
                count += 1

            if (count == len(prim_arr)):
                check = 1
                prim_arr.append(cndd8)

    return prim_arr

prim_arr = [2, 3, 5, 7]

while (len(prim_arr) < 10001):
    gen_next_prime(prim_arr)

print(prim_arr[-1])
