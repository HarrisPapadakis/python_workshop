# Παραδείγματα πλειάδων (tuples) στην Python

# Δημιουργία πλειάδας με διαφορετικούς τύπους δεδομένων
tup = (5, 'Welcome', 7, 'Geeks')
print(tup)

# Δημιουργία πλειάδας με εμφωλευμένες πλειάδες
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print(tup3)

# Δημιουργία πλειάδας με επανάληψη
tup1 = ('Geeks',) * 3
print(tup1)

# Δημιουργία πλειάδας με χρήση βρόχου
tup = ('Geeks')
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)
