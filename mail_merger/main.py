
# Read all the names
with open("input/names/invited_names.txt") as names_file:
    names = names_file.readlines()
    for name in names:
        # print(name.strip())  # Debug info

        # Do a 'replace' in a file and save it elsewhere
        with open("input/letters/starting_letter.txt") as letter_file:
            file_data = letter_file.read()

        file_data = file_data.replace('[name]', name.strip())

        with open(f"output/ready_to_send/{name}.txt", mode="w") as file:
            file.write(file_data)
