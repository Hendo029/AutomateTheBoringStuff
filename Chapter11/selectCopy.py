import shutil, os
from pathlib import Path


def copyFiles(folder, extension):
    backup = 'backup_docx'
    if not Path(backup).exists():
        Path(backup).mkdir()

    for folder_name, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if Path(filename).suffix == extension:
                shutil.copy(Path(folder_name)/filename,Path(backup))
                #print('copying: '+str(folder_name)+'\\'+filename+' to backup folder')



path = Path('./Test_Scripts')
extension = '.docx'

copyFiles(path, extension)