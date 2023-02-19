"""
Christina Wang	8/17/22	CSCI-UA 2 - 006
Assignment #7 Problem #2
"""

#a
import re
# function:   cleanup_string
# input:      a string to clean up
# processing: (1) makes the entire string lowercase.
#             (2) retains only alphabetic, numeric and space characters
#                 [all punctuation and special characters removed]
# output:     returns the cleaned up string
def cleanup_string(data):
    lowerstring=data.lower()
    cleanstring=re.sub("[!@#$%^&*().,?]","",lowerstring)
    return cleanstring

#b
import os
files = os.listdir("data")
#print (files)

#c

def convert(lst):
    it = iter(lst)
    res_dct= dict(zip(it,it))
    return res_dct

#create dictionary
#search = {}
#open file for reading
#f_0jOHqNrSpo = open('data/0jOHqNrSpo.txt', 'r')
#read all data as one long string
#f_0jOHqNrSpo_all=f_0jOHqNrSpo.read()
#run cleanup_string on it
#f_0jOHqNrSpo_clean=cleanup_string(f_0jOHqNrSpo_all)
#cut apart string based on " "
#f_0jOHqNrSpo_split=f_0jOHqNrSpo_clean.split()
#if words repeated within string, delete
#f_0jOHqNrSpo_norepeat=" ".join(sorted(set(f_0jOHqNrSpo_split), key=f_0jOHqNrSpo_split.index))
#cut again
#f_0jOHqNrSpo_norepeatsplit=f_0jOHqNrSpo_norepeat.split()
#convert list to resemble dictionary
#for i in range(len(f_0jOHqNrSpo_norepeatsplit)):
#    f_0jOHqNrSpo_norepeatsplit.insert((i*2)+1, '0jOHqNrSpo.txt')
#enter words into dictionary
#search=convert(f_0jOHqNrSpo_norepeatsplit)
#close file
#f_0jOHqNrSpo.close()

#run for all files

directory= 'data'

#create dictionary
search={}
searchfile={}
#run for all files
for file in files:
    if file.endswith('.txt'):
        #open file for reading
        f_file = open(os.path.join(directory, file), 'rt')
        #read all data as one long string
        f_file_all=f_file.read()
        #run cleanup_string on it
        f_file_clean=cleanup_string(f_file_all)
        #cut apart string based on " "
        f_file_split=f_file_clean.split()
        #if words repeated within string, delete
        f_file_norepeat=" ".join(sorted(set(f_file_split), key=f_file_split.index))
        #cut again
        f_file_norepeatsplit=f_file_norepeat.split()
        #convert list to resemble dictionary
        for i in range(len(f_file_norepeatsplit)):
            f_file_norepeatsplit.insert((i*2)+1, file)
        #enter words into dictionary
        searchfile=convert(f_file_norepeatsplit)
        #update dictionary to big dictionary
        search.update(searchfile)
        #close file
        f_file.close()
        continue
    else:
        continue

print ('happy:', search['happy'])
print ('cat:', search['cat'])
print ('rainbow:', search['rainbow'])
print ('apple:', search['apple'])




















