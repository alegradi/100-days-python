
# FileNotFound
try:
    file = open("afile.txt")
except FileNotFoundError:
    file = open("afile.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()


# KeyError
# dictionario = {"ferkok": "cuccos"}
# value = dictionario["non_existant_key"]

# IndexError
# super_list = [1, 4, 7]
# my_number = super_list[3]

# TypeError
# text = "abc"
# print(text + 5)
