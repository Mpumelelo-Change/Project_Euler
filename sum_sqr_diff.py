def sqr_of_sum(num):
    tot = 0
    
    for i in range(1, num + 1) :
        tot += i

    return (tot**2)

def sum_of_sqr(num):

    tot = 0

    for i in range(1, num + 1) :
        tot += i**2

    return (tot)

spec = 100

print(sqr_of_sum(spec) - sum_of_sqr(spec))
