a = int(input())
b = int(input())
c = int(input())

# Calculate all possible expressions
expressions = [
    a + b + c,
    a + b * c,
    a * b + c,
    a * b * c,
    (a + b) * c,
    a * (b + c)
]

max_value = max(expressions)
print(max_value)
    