for i in range(1, 10001):
    k = i
    counter = 0
    i -= 1
    while i != 0:
        if k // i * i == k:
            counter += i
            i -= 1
        else:
            i -= 1
    answer = counter
    counter = 0
    for j in range(1, answer // 2 + 1):
        if answer // j * j == answer:
            counter += j
    if k == counter and k != answer:
        print(k, answer)
