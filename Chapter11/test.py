from pathlib import Path
import shutil
import send2trash
import os
import zipfile

h = Path.cwd() / 'Test_Scripts'
'''
(h/'spam').mkdir(exist_ok=True)
with open(h/'spam/file1.txt', 'w', encoding='utf-8') as file:
    file.write('Hello')
'''

h2 = h /'spam'

#shutil.copy(h2/'file1.txt',h)
#shutil.copy(h2/'file1.txt', h2/'file2.txt')

#shutil.copytree(h2,h/'spam_backup')

#(h / 'spam2').mkdir()
#shutil.move(h / 'spam/file1.txt', h / 'spam2')

#shutil.move(h / 'spam/file1.txt', h / 'spam2/new_name.txt')

#send2trash.send2trash('./Test_Scripts/file1.txt')


#(h / 'spam').mkdir(exist_ok=True)
#(h/'spam/eggs').mkdir(exist_ok=True)
#(h/'spam/eggs2').mkdir(exist_ok=True)
#(h/'spam/eggs/bacon').mkdir(exist_ok=True)
#shutil.copy(h/'spam_backup/file1.txt',h/'spam')

'''
for f in [h2/'file1.txt', h2/'eggs/file2.txt', h2/'eggs/file3.txt', h2/'eggs/bacon/file4.txt']:
    with open(h2/f, 'w', encoding='utf-8') as file:
        file.write('Hello')
'''
'''
for folder_name, subfolders, filenames in os.walk(h2):
    print('The current folder is:'+folder_name)

    for subfolder in subfolders:
        print('SUBFOLDER OF '+folder_name+': '+subfolder)

    for filename in filenames:
        print('FILE INSIDE '+folder_name+': '+filename)
        # Rename file to uppercase:
        p = Path(folder_name)
        shutil.move(p/filename, p/filename.upper())

    print('')
'''
'''
with open('file1.txt', 'w', encoding='utf-8') as file_obj:
    file_obj.write('Hello' * 10000)

with zipfile.ZipFile('example.zip', 'w') as example_zip:
    example_zip.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
'''

# Of note is that if you specify the directories it puts all those directories in the zip file
#   To solve this either use files in the cwd, or change your directory
'''
example_zip = zipfile.ZipFile('example.zip')
file1_info = example_zip.getinfo('file1.txt')
print(file1_info.file_size)
print(file1_info.compress_size)

print(f'Compressed file is {round(file1_info.file_size / file1_info.compress_size, 2)}x smaller!')
example_zip.close()
'''
'''
example_zip = zipfile.ZipFile('example.zip')
example_zip.extractall()
example_zip.close()
'''








