"""
Christina Wang	7/30/22	CSCI-UA 2 - 002
Assignment #5 Problem #1a
"""
# function:   ascii_shift
# input:      a word to shift (String) and an amount to shift by (integer)
# processing: shifts each character in the supplied word to another position in the ASCII
#             table. the new position is dictated by the supplied integer.  for example,
#             if word = "apple" and num=1 the newly generated word would be:
#
#             bqqmf
#
#             because we added +1 to each character. if we were to call the function with
#             word = "bqqmf" and num=-1 the newly generated word would be:
#           
#             apple
#
#             because we added -1 to each character, which shifted each character down by
#             one position on the ASCII table.
#
#             in the event that an empty string is supplied no shift will occur and an empty 
#             string should be returned
#
# output:     returns the newly generated word

def ascii_shift(word,i):
    user_string = word
    str_length = len(user_string)
    characters=[]
    new_characters = []

#converts word to ascii_values in list
#adds i
#remakes list
    count=0
    for count in range(count, str_length,1):
        c= user_string[count]
        ascii_value = ord(c)
        characters.append(ascii_value)

    numbers= list(map(lambda x: x + i, characters))


#converts ascii_values to a word again
    count=0
    for count in range(count, str_length,1):
        n = numbers[count]
        new_chara = chr(n)
        new_characters.append(new_chara)

#prints new word
    string=''.join(new_characters)
    return string

# function:   shift_right
# input:      a word to shift (String)
# processing: shifts all characters in the string to the right. the last character in the string
#             will be shifted to the beginning of the string.  for example:
#
#             apple -> eappl
#
#             in the event that an empty string is supplied no shift will occur and an empty 
#             string should be returned
#
# output:     returns the newly generated word

def shift_right(word):
    user_string=word
    string=user_string[:-1]
    new_string= user_string[-1] + string
    return new_string

# function:   shift_left
# input:      a word to shift (String)
# processing: shifts all characters in the string to the left. the first character in the string
#             will be shifted to the end of the string.  for example:
#
#             apple -> pplea
#
#             in the event that an empty string is supplied no shift will occur and an empty 
#             string should be returned
#
# output:     returns the newly generated word

def shift_left(word):
    user_string=word
    string=user_string[1:]
    new_string= string + user_string[0]
    return new_string

# function:   flip
# input:      a word to flip (String)
# processing: flips the first half of the string with the second half of the string.
#             if the string has an even number of characters this function will work as follows:
#
#             ABCD -> CDAB
#
#             if the string has an odd number of characters this function will work as follows:
#
#             ABCDE -> DECAB
#
#             in the event that an empty string is supplied no flip will occur and an empty 
#             string should be returned
#
# output:     returns the newly generated word

def flip(word):
    user_string=word
    string=user_string[::-1]
    return string

# function:   add_letters
# input:      a word to scramble (String) and a number of letters (integer)
# processing: adds a number of random letters (A-Z; a-z) after each letter 
#             in the supplied word. for example, if word="cat" and num=1 
#             we could generate any of the following:
#             cZaQtR
#             cwaRts
#             cEaett
# 
#             if word="cat" and num=2 we could generate any of the following:
#             cRtaHFtui
#             cnnaNYtjn
#             czAaAitym
#
# output:     returns the newly generated word

import random
import string

def add_letters(original, num):
    user_string=original
    new_word=[]
    
#make a list of upper and lowercase letters
    string.ascii_letters
    alphabet=list(string.ascii_letters)
#add letters of original word sequentially to list
    for i in range(0, len(user_string)):
        new_word.append(user_string[i])
#pick a letter
        for i in range(num):
            letter=random.choice(alphabet)
#add a letter
            new_word.append(letter)
#convert to string
    new_string=''.join(new_word)
    return new_string

# function:   delete_characters
# input:      a word to analyze (String) and the number of characters to remove (integer)
# processing: the function starts at the first position in the supplied word and keeps it.
#             it then removes "num" characters from the word. the process is repeated again
#             if the word contains additional characters - the next character is kept
#             and "num" more characters are removed.  For example, if word="cZaYtU" and
#             num=1 the function will generate the following:
#        
#             cat (keeping character 0, removing character 1, keeping character 2, removing
#                  character 3, keeping character 4, removing character 5)
#
# output:     returns the newly unscrambed word

import string

def delete_characters(word, num):
    user_string=word
    return(user_string[::num+1])        
