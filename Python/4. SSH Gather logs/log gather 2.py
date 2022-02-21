import glob
import shutil
import os

while True:     
    choice1 = int(input('Which server? 1-13'))
    clientas = ['server']
    choice2 = int(input('server'))
    dir1 = '\\'+'\\IP'+str(50+choice1)+'\\c$\\app\\'+clientas[choice2]+'\\logs\\*' 
    dir2 = str(choice1)+'_'+clientas[choice2]
    os.makedirs(dir2)
    os.system('powershell.exe copy-item '+dir1+'  '+dir2)
    shutil.make_archive(dir2, 'zip', dir2)
    shutil.rmtree(dir2)


