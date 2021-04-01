counter = 0
for c in range(1,48):
    for b in range(1,c):
        for a in range(1,b):
            if a * a + b * b == c * c:
                print('{}, {}, {}'.format(a,b,c))
                counter += 1


print(counter)