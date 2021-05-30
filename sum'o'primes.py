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

prim_arr = [2]
sum_o = 0

while (prim_arr[-1] < 2000000):
    print(prim_arr[-1])
    sum_o += prim_arr[-1]
    gen_next_prime(prim_arr)

print(sum_o)
