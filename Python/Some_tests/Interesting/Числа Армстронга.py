for i in range(1, 32000):
    k = str(i)
    counter = 0
    for j in range(len(k)):
        p = int(k[j])** int(len(k))
        counter += p
    if counter == i:
        print(i)
