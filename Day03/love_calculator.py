# Day03 for 100Days4Python

def name_check(word, name):
	score = 0
	word = word.lower()
	name = name.lower()
	for name_char in name:
		for word_char in word:
			print(name_char, word_char)
			if name_char == word_char:
				score += 1
	return score

print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?")

true = name_check("true", name1) + name_check("true", name2)
love = name_check("love", name1) + name_check("love", name2)
total = true * 10 + love

print(f"Your score is {total}", end="")
if total < 10 or total > 90:
	print(", you go together like coke and mentos.")
elif 40 <= total <= 50:
	print(", you are alright together.")
else:
	print(".")