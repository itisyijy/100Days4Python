# Day2 for 100Days4Python
# Operations (+ - * /)
# Priority of Operations    : PEMDAS [Parentheses > Exponents > Multiplication = Division > Addition = Subtraction]
# Order of Operations       : Left to Right

print("\n--Operations--")
plus = 1 + 2            # 3
minus = 3 - 7           # -4
asterisk = 4 * 8        # 32
slash = 10 / 3          # 3.3333333333333335
print("/ Result  :", slash, type(slash))      # result of '/' is always float.
double_slash = 10 // 3  # 3
print("// Result :", double_slash, type(double_slash))      # result of '//' is always integer.
double_asterisk = 3 ** 4       # Exponents, 81

bmi = (65 / (1.72 ** 2))
print("Without round :", bmi)
print("With round    :", round(bmi, 6)) # rounding with precision

# Shorthand
var = 0
var += 3                # var = var + 3
var -= 5                # var = var - 5
var *= -1               # var = var * -1
var /= 2                # var = var / 2