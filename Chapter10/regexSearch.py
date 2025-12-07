from pathlib import Path
import os
import re

# \b(ADJECTIVE|NOUN|VERB)\b

path = Path.cwd()/'Test_Scripts'

print('Give a regular expression:')
regex = input()
regex = re.compile(regex)

for files in Path(path).glob('*.txt'):
    text = open(files, encoding='UTF-8').read()
    mo = regex.findall(text)
    if not mo:
        continue
    else:
        print('\nFile: ' +files.name +' contains this list of words mathing the regular expression:')
        print(mo)
        print('\n')
