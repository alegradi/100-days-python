import pandas


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_alphabet)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please enter a word: ").upper()
output_list = [nato_alphabet[letter] for letter in user_input]

print(output_list)
