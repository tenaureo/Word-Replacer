import os
import mmap

filepath = input("Please enter your filepath: ")

wordToReplace = input("Word to replace: ")

f = open(filepath, "r+")
data = f.read()

wordToReplaceWith = input("Word to replace with: ")

#Word to replace is replaced here
data = data.replace(wordToReplace, wordToReplaceWith)
f.close

f = open(filepath, "w+")
f.write(data)
f.close

if (wordToReplace == wordToReplaceWith):
    print("The two words are the same, please try again")
else:
    print("Every instance of " + wordToReplace + " has been replaced with " + wordToReplaceWith)