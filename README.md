# Text Twister

## Description
This Python script turns user-supplied text into SpongeCase, a text format in which the case of each alphabet character is randomly altered between upper and lower case.

## Getting Started
To execute this script, you must have Python3 installed on your computer:
1. Download or copy the text twister.py file to your computer.
2. Open your terminal or command prompt and go to the location where you stored the file.
3. To launch the program, type python3 text twister.py and press enter.

## Usage
After you launch the application, you will be requested to enter the text to be altered to SpongeCase. After you enter your text, the application changes it and displays the results in the terminal.

## Implementation Details
The convert_to_spongecase function transforms the supplied text into SpongeCase. It begins by creating an empty string to hold the translated text and a flag to indicate whether the following letter should be upper or lower case. It then iterates through the input text, checking each character to see if it is an alphabet character. If the character is not an alphabet, it is simply appended to the output string. If it's an alphabet character, the function randomly swaps the case between upper and lower case with a 90% chance.
The main function is in charge of soliciting the user for text input, executing the convert_to_spongecase function to convert the text, and showing the results in the terminal.

## Additional Details
1.	The random module is used to flip the case of each alphabet character at random.
2.	The isalpha() function determines whether or not a character is an alphabet character.
3.	If the current letter is not an alphabet character, the continue statement is used to skip the rest of the loop.
4.	The if __name__ == '__main__': sentence guarantees that the main function is only called if the script is performed directly.



## Ideas for Additional Features
1.	1. Allow the user to select the likelihood of switching the case of each alphabet character.
2.	2. Provide a function for converting SpongeCase text back to its original format.
3.	Let the user to select from a variety of SpongeCase styles, such as randomly capitalising words or rotating between upper and lower case within each phrase.
4.	Provide a graphical user interface (GUI) to make the application more user-friendly.
5.	Add support for importing text from external files and exporting SpongeCase text to a file.
6.	Implement a function to verify the spelling and grammar of the input text before converting it to SpongeCase.
