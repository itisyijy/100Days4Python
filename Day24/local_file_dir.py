# Day24 for 100Days4Python
# Day24 : Access Local Files and Directories

# open the file
file = open("./text.txt")

# return content of the file into string
content = file.read()
print(content)

# after do something with file, then close the file -> free computer's resources
file.close()

# 'with' keyword -> no need to use '.close' method
# 'with' mange files directly
print("-------------------------------")
with open("./text.txt", mode="r") as file_with:
    content_with = file_with.read()
    print(content_with)

print("-------------------------------")
with open("./new_file.txt", mode="w") as file_with:
    file_with.write("[w]rite mode can make file with content or overwrite the content.")
    
print("-------------------------------")
with open("./text.txt", mode="a") as file_with:
    file_with.write("[a]ppend mode can append content on existing content.")
    print(content_with)
