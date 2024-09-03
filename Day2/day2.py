# Day2 for 100Days4Python

# Data Types
#   String.
print("--String--")
var_string = "Hello"
print(var_string[-1])   # subscripting, String에서 특정 문자 추출. 음수, 양수 모두 사용 가능.

#   Integer. 정수
print("\n--Integer--")
var_integer = 123_456_789
print(var_integer)

#   Float. 부동소수점
print("\n--Flaot--")
var_float = 3.141592
print(var_float)

#   Boolean.
print("\n--Boolean--")
var_true = True
var_false = False
print(var_true)
print(var_false)

# Check Data Types -> type()
print("\n--type()--")
print("String  : ", type(var_string))
print("Integer : ", type(var_integer))
print("Float   : ", type(var_float))
print("Boolean : ", type(var_true), type(var_false))

# Type Casting
print("\n--Type Casting--")
print("Without Casting : ", "123" + "456")
print("With    Casting : ",int("123") + int("456"))     # Caution in Type Casting! for Error Occurrence / Loosing Data

int()
float()
str()
bool()

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

# F-String
print("\n--F-String--")
score = 76
grade = 4.2
is_pass = True
print(f"Score = {score}, Grade = {grade:.2f}, Pass = {is_pass}")   # f"~~{variable}~~". float formatting -> {var:.nf}