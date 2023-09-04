
# Standard file reading
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Better file reading
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# File writing
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")


# If the file doesn't exist, mode="w" will create it for you
with open("new_file.txt", mode="w") as file:
    file.write("\nEven more text.")
