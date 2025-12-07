import os, shutil
from pathlib import Path

def deleteFiles(path):
    folderContents = path.iterdir()
    for i in folderContents:
        if (os.path.getsize(i) / 1024**2) >= 100:
            print(i)

path = Path('E:/Downloads')
deleteFiles(path)

