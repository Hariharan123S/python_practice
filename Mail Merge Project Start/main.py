PLACEHOLDER = "[name]"


with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()


with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        strip_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, strip_name)
        with open(f"./Output/ReadyToSend/letter_for_{strip_name}.txt", mode='w') as completed_file:
            completed_file.write(new_letter)
