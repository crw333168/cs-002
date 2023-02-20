"""
Christina Wang	7/31/22	CSCI-UA 2 - 002
Assignment #5 Problem #1b
"""
import WangChristina_assign5_part1a

pattern=input("Enter an encoding pattern, 'end' to end: ")
while pattern != 'end':
    word= input("Enter a word to encode/decode: ")

    #for each item in list
    for character in pattern:
        if 'A' in character:
            new_word=WangChristina_assign5_part1a.add_letters(word, 1)
            print("Added 1 character: ", new_word)
            word=new_word
            continue
        elif 'X' in character:
            new_word=WangChristina_assign5_part1a.delete_characters(word, 1)
            print("Deleted 1 character: ", new_word)
            word=new_word
            continue
        elif 'F' in character:
            new_word=WangChristina_assign5_part1a.flip(word)
            print("Flipped: ", new_word)
            word=new_word
            continue
        elif 'U' in character:
            new_word=WangChristina_assign5_part1a.ascii_shift(word,1)
            print("ASCII shifted up: ", new_word)
            word=new_word
            continue
        elif 'D' in character:
            new_word=WangChristina_assign5_part1a.ascii_shift(word,-1)
            print("ASCII shifted down: ", new_word)
            word=new_word
            continue
        elif 'L' in character:
            new_word= WangChristina_assign5_part1a.shift_left(word)
            print("Shifted left: ", new_word)
            word=new_word
            continue
        elif 'R' in character:
            new_word=WangChristina_assign5_part1a.shift_right(word)
            print("Shifted right: ", new_word)
            word=new_word
            continue
    break
