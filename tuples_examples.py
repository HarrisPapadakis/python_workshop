# Πρόγραμμα εξάσκησης σε πλειάδες (tuples)

# Πλειάδα με αριθμούς και συμβολοσειρές
data = (10, "Python", 3.14, "Tuples")
print("Αρχική πλειάδα:", data)

# Πλειάδες μέσα σε πλειάδα
numbers = (1, 2, 3)
words = ("code", "learn")
combined = (numbers, words)
print("Εμφωλευμένη πλειάδα:", combined)

# Πλειάδα με επαναλαμβανόμενα στοιχεία
repeat_tuple = ("IT",) * 4
print("Πλειάδα με επανάληψη:", repeat_tuple)

# Δημιουργία πλειάδας σταδιακά με επανάληψη
value = "Start"
times = 4

for i in range(times):
    value = (value,)
    print(f"Βήμα {i + 1}:", value)
