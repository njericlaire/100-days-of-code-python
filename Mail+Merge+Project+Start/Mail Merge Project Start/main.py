PLACEHOLDER = "[name]"

# Read the names from 'invited_names.txt'
with open("./Input/Names/invited_names.txt") as letter_names:
    names = letter_names.readlines()
    print(names)

# Read the template letter from 'starting_letter.txt'
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()


 # Create each letter and save it in 'ReadyToSend'
for name in names:
    # Remove any extra whitespace/newline characters from the name
    name = name.strip("\n")

    # Replace the placeholder in the letter with the current name
    final_letter = letter_content.replace(PLACEHOLDER, name)

    # Save the letter with the recipient's name in 'ReadyToSend' folder
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:

        completed_letter.write(final_letter)
    print(f"Letter created for {name}")
