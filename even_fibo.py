def fib_gen(length):
    
    fib_arr = [1, 2]
    count = 2

    while (count <= length):
        fib_arr.append(fib_arr[count - 1] + fib_arr[count - 2])
        count += 1

        if (fib_arr[-1] == 3524578):
            break

    return fib_arr

def arr_tot(arr) :
    x = len(arr)
    count = 0
    tot = 0

    while (count < x) :
        tot = tot + ret_if_even(arr[count])
        count += 1

    return tot

def ret_if_even(num) :
    if (num % 2 == 0) :
        return num
    else :
        return 0
    
length = 100


print(arr_tot(fib_gen(length)))
