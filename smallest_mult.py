candid8 = 325679
broken = 0

while (candid8 < 1000000):
    count = 0
    print(candid8)
    for i in range(20, 11, -1):
        if (candid8 % i == 0) :
            print(count)
            count += 1
        if (count == 9) :
            print(candid8)
            broken = 1
            break

    if (broken == 1) :
        break

    candid8 += 1
