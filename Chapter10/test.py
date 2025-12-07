from pathlib import Path
import os
import shelve

'''
my_files = ['accounts.txt', 'details.csv', 'invite.docx']
for filenames in my_files:
    print(Path(r'C:/Users/Joris', filenames))
'''
'''
new_dir = 'Test_Scripts'
working_dir = Path.cwd()

#os.makedirs(working_dir / new_dir)
Path(Path.cwd() / new_dir).mkdir()
Path(Path.cwd()/'Day1').is_absolute()
'''
'''
for files in Path(Path.cwd() / 'Day1/Chapter1').glob('*'):
    print(files)
'''
'''
p = Path.cwd() / 'Day1/Chapter1'
p2 = Path.cwd() / 'Day10'
if p.exists():
    print('p')
if p2.exists():
    print('p2')
'''
"""
fileName = 'test.txt'
fileTest = open(Path.cwd()/'Test_Scripts'/fileName, 'a', encoding='UTF-8')
fileTest.write('''Yo boys
               
The hell is going on?\n\n''')
fileTest.close()
"""
'''
fileName = 'test.txt'
filePath = Path.cwd()/'Test_Scripts'/fileName

with open(filePath, 'a', encoding='UTF-8') as fileTest:
    fileTest.write('Hallo man\n\n')

with open(filePath, encoding='UTF-8') as fileTest:
    fileContent = fileTest.read()

print(fileContent)
'''
filePath = Path.cwd()/'Test_Scripts'
with shelve.open(filePath/'mydata') as shelf_file:
    shelf_file['teammembers'] = ['Hendo', 'Lamaker', 'Jing Ping', 'Rutger Ouwe', 'De Baas']

