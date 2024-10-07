# Day24 for 100Days4Python
# Day24 : Access Local Files and Directories

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# ¡MY CODE!
# make name list from the invited_names.txt
with open("./Input/Names/invited_names.txt", mode="r") as invited_names:
    name_list = invited_names.readlines()

for i in range(len(name_list)):
    name_list[i] = name_list[i].strip()

# get letter format from the starting_letter.txt
with open("./Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    letter_format = starting_letter.read()

# write name for each letter and save them with different file name
for name in name_list:
    with open(f"./Output/ReadyToSend/letters_for_{name}.txt", mode="w") as letter_for_one:
        letter = letter_format.replace("[name]", name)
        new_letter = letter_for_one.write(letter)

# ¡SOLUTION!
PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
