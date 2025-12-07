import os, shutil
from pathlib import Path

'''
for i in range(1, 121):
        if i not in (42, 86, 103):
            with open(path/f'spam{str(i).zfill(3)}.txt', 'w') as file:
                pass
'''
def renumberFiles(path):
    fileList = os.listdir(path)
    for i in fileList:
        if i == fileList[0]:    # i is a string 'spam001.txt'
            # Use 'string'.isdigit()  returns True/False
            stemTemp = ''
            for j in range(len(i)):
                if i[j].isdigit():
                    stemTemp = stemTemp+i[j]
            stemTemp = int(stemTemp)
        else:
            stem = ''
            for k in range(len(i)):
                if i[k].isdigit():
                    stem = stem+i[k]
            stem =int(stem)
            #Calc gap
            gap = stem - stemTemp -1
            if gap > 0:
                changeNames(gap,fileList,i)
            stemTemp=stem

def changeNames(gap,fileList,fileName):
    #print(gap)
    pos = fileList.index(fileName)
    for i in range(len(fileList)):
        if i >= pos:
            #TODO:change name: with open and write


path = Path.cwd()/'Test_Scripts/test2'
renumberFiles(path)