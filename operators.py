# ============================================================
#                    PYTHON OPERATORS
# ============================================================


# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================

print("\n" + "=" * 55)
print("              1. ARITHMETIC OPERATORS")
print("=" * 55)

a = 10
b = 3

print("\nGiven:")
print("a =", a)
print("b =", b)

print("\nResults:")
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a // b =", a // b)
print("a % b  =", a % b)
print("a ** b =", a ** b)


# ============================================================
# 2. COMPARISON OPERATORS
# ============================================================

print("\n" + "=" * 55)
print("              2. COMPARISON OPERATORS")
print("=" * 55)

a = 10
b = 20

print("\nGiven:")
print("a =", a)
print("b =", b)

print("\nResults:")
print("a == b  ->", a == b)
print("a != b  ->", a != b)
print("a > b   ->", a > b)
print("a < b   ->", a < b)
print("a >= b  ->", a >= b)
print("a <= b  ->", a <= b)


# ============================================================
# 3. LOGICAL OPERATORS
# ============================================================

print("\n" + "=" * 55)
print("                3. LOGICAL OPERATORS")
print("=" * 55)

age = 21

print("\nValue:")
print("age =", age)

print("\nAND:")
print("age >= 18 and age <= 60")
print("Result:", age >= 18 and age <= 60)

print("\nOR:")
print("age < 18 or age > 60")
print("Result:", age < 18 or age > 60)

print("\nNOT:")
print("not True")
print("Result:", not True)


# ============================================================
# 4. ASSIGNMENT OPERATORS
# ============================================================

print("\n" + "=" * 55)
print("               4. ASSIGNMENT OPERATORS")
print("=" * 55)

x = 10

print("\nInitial value:")
print("x =", x)

x += 5
print("x += 5  ->", x)

x -= 3
print("x -= 3  ->", x)

x *= 2
print("x *= 2  ->", x)

x /= 4
print("x /= 4  ->", x)


# ============================================================
# 5. MEMBERSHIP OPERATORS
# ============================================================

print("\n" + "=" * 55)
print("               5. MEMBERSHIP OPERATORS")
print("=" * 55)

name = "Harsh"

print("\nString:")
print("name =", name)

print("\nChecking membership:")
print("'H' in name      ->", "H" in name)
print("'z' in name      ->", "z" in name)
print("'z' not in name  ->", "z" not in name)


# ============================================================
# 6. IDENTITY OPERATORS
# ============================================================

print("\n" + "=" * 55)
print("                6. IDENTITY OPERATORS")
print("=" * 55)

x = None

print("\nValue:")
print("x =", x)

print("\nChecking identity:")
print("x is None      ->", x is None)
print("x is not None  ->", x is not None)


# ============================================================
# 7. BITWISE OPERATORS
# ============================================================

print("\n" + "=" * 55)
print("                  7. BITWISE OPERATORS")
print("=" * 55)

a = 5
b = 3

print("\nGiven:")
print("a =", a, "-> Binary: 101")
print("b =", b, "-> Binary: 011")

print("\nResults:")
print("a & b  ->", a & b)
print("a | b  ->", a | b)
print("a ^ b  ->", a ^ b)
print("a << 1 ->", a << 1)
print("a >> 1 ->", a >> 1)


# ============================================================
#                    QUICK REVISION
# ============================================================

print("\n" + "=" * 55)
print("                    QUICK REVISION")
print("=" * 55)

print("""
Arithmetic   : +  -  *  /  //  %  **
Comparison   : ==  !=  >  <  >=  <=
Logical      : and  or  not
Assignment   : =  +=  -=  *=  /=  //=  %=  **=
Membership   : in  not in
Identity     : is  is not
Bitwise      : &  |  ^  ~  <<  >>
""")

print("=" * 55)
print("              END OF PYTHON OPERATORS")
print("=" * 55)