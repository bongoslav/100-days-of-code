import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

dict_nato = {row.letter: row.code for (index, row) in df.iterrows()}

def generate_phonetic():
    user_input = input("Type a word: ").upper()
    try:
        nato_list = [dict_nato[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet, please.")
        generate_phonetic()
    else:
        print(nato_list)


generate_phonetic()