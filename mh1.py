import numpy as np
import math

def q_2(n):
    """Return the 2-adic quotient of n."""
    if n == 0:
        return 0, 0
    p = 0
    while n % 2 == 0:
        n = n // 2
        p += 1
    return n

def q_3(n):
    """Return the 3-adic quotient of n."""
    if n == 0:
        return 0, 0
    while n % 3 == 0:
        n = n // 3
        p += 1
    return n, p

def h(x):
    return q_2(3 * x + 1)

def adic(x):
    """Return the conjugated n-form and p-form of x."""
    def get_adic(x, form):
        if form == "n":
            n = x + 1
        else:  # p-form
            n = x - 1

        # Factor out all 2s
        k = 0
        while n % 2 == 0:
            n = n // 2
            k += 1

        # Factor out all 3s
        l = 0
        while n % 3 == 0:
            n = n // 3
            l += 1

        c = n
        return k, l, c

    n_form = get_adic(x, "n")
    p_form = get_adic(x, "p")

    return n_form, p_form

def loc(x):
    n_f, p_f = adic(x)
    if not (n_f[0] == 1 and p_f[0] == 2):
        return 0, 0 # regular form: not locus
    if n_f[1] == 0 and p_f[1] == 0: # h-locus | 3
        return 3, x
    if n_f[1] == 1 and p_f[1] == 0: # n-locus: 2 y - 1
        y = 3 ** n_f[1] * n_f[2]
        return -1, y
    else:                           # p-locus: 4 y + 1
        y = 3 ** p_f[1] * p_f[2]
        return 1, y

def mh(l, x):                       # modified at n, p-loci
    if l > 0:
        return 3 * x + 2
    else:
        return 3 * x - 2
    


'''for x in range(3, 32, 2):
    print(x, adic(x), loc(x)[0], loc(x)[1])'''

s = 27
r = 30
x = s
seq = [x]
for t in range (r):
    l,y = loc(x)
    if not abs(l) == 1:
        x = h(x)
    else:
        x = mh(l,y)
    seq.append(x)

print(s, x, seq)
        
    

        


'''
def simulate_sequence(start, n=10):
    """Simulate the modified hailstone sequence."""
    sequence = [start]
    seen = set()

    for _ in range(n - 1):
        x = sequence[-1]
        n_form, p_form = adic(x)
        k_minus, l_minus, y_minus = n_form
        k_plus, l_plus, y_plus = p_form

        if k_minus == 1 and k_plus == 2:
            if l_minus > 0:
                # n-loc
                next_x = 3 * (3**l_minus * y_minus) - 2
            elif l_plus > 0:
                # p-loc
                next_x = 3 * (3**l_plus * y_plus) + 2
            else:
                # Standard rule
                next_x = q_2(3 * x + 1)
        else:
            # Standard rule
            next_x = q_2(3 * x + 1)

        if next_x in seen:
            sequence.append(next_x)
            break
        seen.add(next_x)
        sequence.append(next_x)
        if next_x == 1:
            break

    return sequence

# Simulate for odd integers, excluding those already seen
seen_numbers = set()
results = {}

for x in range(3, 18, 2):
    if x not in seen_numbers:
        sequence = simulate_sequence(x)
        results[x] = sequence
        seen_numbers.update(sequence)

# Print results
for start, seq in results.items():
    print(f"Starting from {start}: {seq}")

'''
            
        
