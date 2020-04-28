def binary_conv(n):
    p1 = 1
    p2 = 1
    lst = list()
    counter1 = 0
    counter2 = 0

    while p1 <= n:
        p1 *=2
        counter1 += 1

    len_bin = counter1
    lst = len_bin*[0]
    counter1 -= 1

    while n > 0:
        p2 *= 2
        counter2 += 1
        if (p2*2) == p1 or p2 == p1:
            if n<2:
                counter2-=1
            lst[counter1-counter2] = 1
            p1 = p2
            p2 = 1
            n = n-p1
            counter2= 0
