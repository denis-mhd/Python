import random 
import math
import sys

counter = 0

def generate_permutattions(a, n):
    global counter
    
    if counter == 20:
        return

    if n == 0:
        value = random.randint(counter,21)
        
        if counter == value:      
            counter += 1
            print(''.join(a))     
    else:
        for i in range(n):
            generate_permutattions(a, n-1)
            j = 0 if n % 2 == 0 else i
            a[j], a[n] = a[n], a[j]
        generate_permutattions(a, n-1)


if len(sys.argv) != 2:
    sys.stderr.write('Exactly one argument is required\n')
    sys.exit(1)


word = sys.argv[1]

generate_permutattions(list(word), len(word)-1)   