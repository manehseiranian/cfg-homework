"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""

#The commented out rows can be undone to help with viewing the answers

def generate_phrase(characters, phrase):
    character_list = [character for character in characters]
    phrase_list = [letter for letter in phrase]
    # print(character_list)
    # print(phrase_list)
    binary_result = []
    for x in character_list:
        if character_list.count(x) >= phrase_list.count(x):
            binary_result.append(True)
        else:
            binary_result.append(False)
    if False not in binary_result:
        print(True)
    else:
        print(False)



# test cases:

generate_phrase("cbacba", "aabbccc")
generate_phrase("cbacba", "aabbcc")
generate_phrase("cbac ba", "a abbcc")
generate_phrase("cb- caba", "a abbcc")
generate_phrase("ccccbacba", "aabbccc")
generate_phrase("ccccbajfghsijcb", "aabbccc")

