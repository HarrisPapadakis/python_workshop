squares =[]
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)


#Second method using
squares =[]
for value in range(1,11):
    squares.append(value**2)

print(squares)


#Third method shorter
squares = [value**2 for value in range(1,11)]
print(squares)