# Arithmetic Operators
a = 10
b = 3

# Addition
add = a + b
print(f'Addition: {a} + {b} = {add}')

# Subtraction
sub = a - b
print(f'Subtraction: {a} - {b} = {sub}')

# Multiplication
mul = a * b
print(f'Multiplication: {a} * {b} = {mul}')

# Division
div = a / b
print(f'Division: {a} / {b} = {div}')

# Modulus
mod = a % b
print(f'Modulus: {a} % {b} = {mod}')

# Exponentiation
exp = a ** b
print(f'Exponentiation: {a} ** {b} = {exp}')

# Floor Division
floor_div = a // b
print(f'Floor Division: {a} // {b} = {floor_div}')

# Relational Operators
a = 10
b = 20

print(f'{a} > {b} is {a > b}')
print(f'{a} < {b} is {a < b}')
print(f'{a} == {b} is {a == b}')
print(f'{a} != {b} is {a != b}')
print(f'{a} >= {b} is {a >= b}')
print(f'{a} <= {b} is {a <= b}')

# Assignment Operator
a = 5
print(f'a = {a}')

a += 3
print(f'a += 3: {a}')

a -= 2
print(f'a -= 2: {a}')

a *= 2
print(f'a *= 2: {a}')

a /= 3
print(f'a /= 3: {a}')

a %= 3
print(f'a %= 3: {a}')

a **= 2
print(f'a **= 2: {a}')

a //= 2
print(f'a //= 2: {a}')

# Logical Operators
a = True
b = False

print(f'a and b is {a and b}')
print(f'a or b is {a or b}')
print(f'not a is {not a}')


# Bitwise Operators
a = 10  # 1010 in binary
b = 4   # 0100 in binary

print(f'a & b = {a & b}')
print(f'a | b = {a | b}')
print(f'a ^ b = {a ^ b}')
print(f'~a = {~a}')
print(f'a << 2 = {a << 2}')
print(f'a >> 2 = {a >> 2}')


# Ternary Operator
a = 10
b = 20

# Using Ternary Operator
max_value = a if a > b else b
print(f'The greater value is {max_value}')

# Membership Operators
list = [1, 2, 3, 4, 5]
a = 3
b = 6

print(f'{a} in list is {a in list}')
print(f'{b} not in list is {b not in list}')


# Identity Operators
a = 10
b = 20
c = a

print(f'a is b: {a is b}')
print(f'a is c: {a is c}')
print(f'a is not b: {a is not b}')


# if statement
a = 10
if a > 5:
    print('a is greater than 5')


# if else statement
a = 10
if a > 15:
    print('a is greater than 15')
else:
    print('a is not greater than 15')


# if-elif-else statement
a = 10
if a > 15:
    print('a is greater than 15')
elif a == 10:
    print('a is 10')
else:
    print('a is less than 10')


# if-elif-else statement
a = 10
if a > 15:
    print('a is greater than 15')
elif a == 10:
    print('a is 10')
else:
    print('a is less than 10')


# nested if
a = 10
if a > 5:
    if a < 15:
        print('a is between 5 and 15')

# while loop
i = 1
while i <= 5:
    print(i)
    i += 1


# for loop
for i in range(1, 6):
    print(i)


# break statement
for i in range(1, 6):
    if i == 3:
        break
    print(i)


# continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# pass statement
for i in range(1, 6):
    if i == 3:
        pass
    print(i)


n = 5
for i in range(1, n + 1):
    print('*' * i)
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
for i in range(n-1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
