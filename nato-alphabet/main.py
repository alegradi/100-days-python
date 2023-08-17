import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_alphabet)

output_list = []


def get_user_input():
    global output_list
    user_input = input("Please enter a word: ").upper()

    try:
        output_list = [nato_alphabet[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the Latin alphabet please")
        get_user_input()


get_user_input()
print(output_list)
