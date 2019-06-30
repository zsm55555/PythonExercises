# This program is taken from Automate The Boring Stuff With Python by: Al Sweigart
# Chapter 8 - Practice Project - Mad Libs
# reads in This program reads text files and lets the user add their own text
# anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
import re

with open('MadLibs.txt', 'r') as f:
    textContent = f.read()

regex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)')

for i in regex.findall(textContent):
    for j in i:
        if j != '':
            reg = re.compile(r'{}'.format(j))
            user = input('Enter the substitute for %s: ' %j)
            textContent = reg.sub(user,textContent,1)

print(textContent)

with open('MadLibs_updated.txt','w') as f:
    updatedContent = f.write(textContent)
