# Day1 for 100Days4Python

import sys

print("--string concatenation--")
print("Lee" + "Jeongyun")
print("Lee" + " " + "Jeongyun")

print("\n--print function--")
print("Hello", "World!", sep=" ", end="\n", file=sys.stdout, flush=True)
#function의 def를 확인하자.
#   *values: object,                            출력할 객체를 ','로 구분해 전달.
#   sep: str | None = " ",                      출력할 객체 간 어떤 문자열 삽입할지 지정.
#   end: str | None = "\n",                     출력 이후 어떤 문자열 출력할지 결정
#   file: SupportsWrite[str] | None = None,     출력을 어디에 보낼지 결정. default = sys.stdout(표준출력)
#   flush: Literal[False] = False) -> None      출력 buffer를 강제로 비울지 결정. default = false. true 설정 시 buffer 비우고 강제 출력.

print("\n--input function--")
print("Hello, ", input("What is your name >>> "), "!", sep="")
#   prompt로 user에게 입력할 data에 대한 hint 제공. cursor를 통해 user부터 data를 입력받음.
#   nested function -> input 먼저 실행 후 print 실행.

print("\n--variables--")
name = input("What is your name >>> ")
length = len(name)
print("strlen is %d" %length)
