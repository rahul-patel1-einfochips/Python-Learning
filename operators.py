# Arithmetic
# +, -, *, /, //, **
var1 = 5
var2 = 10
value = var1 + var2
print(value)

value = var1 - var2
print(value)

value = var1 * var2
print(value)

var1 = 55
var2 = 10
value = var1 / var2
print(value)

var1 = 5
var2 = 2
value = var1 ** var2
print(value)

var1 = 57
var2 = 10
value = var1 // var2
print(value)

# Comparison
# <, >, <=, >=, ==, !=
value = var1 > var2
print(value)

value = var1 < var2
print(value)

value = var1 <= var2
print(value)

value = var1 >= var2
print(value)

var1, var2 = 5, 6
value = var1 == var2
print(value)

var1, var2 = 5, 5
value = var1 != var2
print(value)

# Logical
# and, or, not

# and
# A  B  Result
# F  F  F
# F  T  F
# T  F  F
# T  T  T

# or
# A  B  Result
# 0  0  0
# 0  1  1
# 1  0  1
# 1  1  1

# not
# A  Result
# 0  1
# 1  0

var1 = 25
var2 = 20
var3 = 30
#       False         and True
value = (var1 < var2) and (var1 < var3) or (var2 < var3)
print("AND::", value)

#       False         or False
value = (var1 < var2) or (var1 > var3)
print("OR::", value)

#           True
value = not (var1 > var2)
print("NOT::", value)

a = 15
# if not a == 10:
if a != 10:
    print("A is not 10")

# Assignment
a = 10
a = 10 + 20
a += 20 # a = a + 20
a -= 20 # a = a - 20
a *= 20 # a = a * 20
a /= 20 # a = a / 20

# Identity
# is
a = 10
b = 10
c = a is b
print(id(a), id(b))
print(c)

# Membership
# in
name = 'Rahul'
value = 'A' in name
print(value)
