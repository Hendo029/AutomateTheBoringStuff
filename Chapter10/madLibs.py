from pathlib import Path
import os
import re

path = Path.cwd()/'Test_Scripts'
regexes = re.compile(r'\b(ADJECTIVE|NOUN|VERB)\b')
text = open(Path.cwd()/'Test_Scripts/text.txt', 'r', encoding='UTF-8').read()

for m in re.finditer(regexes, text):
    temp = m.group()
    if temp == 'NOUN':
        print('Enter a noun:')
    elif temp == 'VERB':
        print('Enter a verb:')
    elif temp == 'ADJECTIVE':
        print('Enter an adjective:')
    newWord = input()
    text = text.replace(temp, newWord, 1)

with open(path/'newText.txt', 'w', encoding='UTF-8') as f:
    f.write(text)

print(text)