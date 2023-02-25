# Text Twister

import random


def main():
    # Prompt the user to enter the text to convert to SpongeCase
    message = input('Enter text to convert to Spongecase: ')
    # Call the convert_to_spongecase function to convert the text
    sponge_text = convert_to_spongecase(message)
    # Display the converted text
    print('SpongeCase:', sponge_text)


def convert_to_spongecase(message):
    # Initialize an empty string for storing the converted text
    sponge_text = ''
    # Initialize a flag to track if the next character should be upper or lower case
    use_upper = False

    # Iterate over each character in the input message
    for character in message:
        # If the character is not an alphabet, add it to the result string as is
        if not character.isalpha():
            sponge_text += character
            continue

        # If use_upper is True, make the character upper case, else make it lower case
        if use_upper:
            sponge_text += character.upper()
        else:
            sponge_text += character.lower()

        # Flip the case 90% of the time
        if random.randint(1, 100) <= 90:
            use_upper = not use_upper  # Flip the case

    return sponge_text


if __name__ == '__main__':
    main()
