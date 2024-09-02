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
print("String : ", type(var_string))
print("Integer : ", type(var_integer))
print("Float : ", type(var_float))
print("Boolean : ", type(var_true), type(var_false))

# Type Casting
print("\n--Type Casting--")
print("Without Casting : ", "123" + "456")
print("With    Casting : ",int("123") + int("456")) #Caution in Type Casting! for Error Occurrence / Loosing Data