import paramiko
import time
from datetime import datetime, timedelta
import stat
import os
import shutil
import sys

try:
    rangeA = raw_input('Date 1 range*  YYYY MM DD HH \n')
    rangeB = raw_input('Date 2 range*  YYYY MM DD HH \n')
    # ask for input without a dash because we will be splitting the date so we wont need more than 2 inputs
    list1 = map(int, rangeA.split())
    list2 = map(int, rangeB.split())       
except (TypeError, ValueError, NameError):
    print('Not a proper date format!')
    sys.exit()

try:
    nrnr = str(input("Input  nr "))       
except (TypeError, ValueError, NameError):
    print ("ERROR - Not a proper num")
os.mkdir(nrnr)
# try and except so we dont run into errors if the user inputs not an int

while True: 
    ips = ['139', '140', '140', '140']  #ip end     
    name = ['process'] 
    for number, letter in enumerate(name):
        print(number, letter)
    choice = int(input('\n  Which server? 1-10 ')) # we use the input of the user to take value of the list of ips and processes
    # this could be done easier with an external json file
    def main():          
        os.mkdir(nrnr+'\\'+name[choice]) 
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname='IPSTART.'+ips[choice],username='name',password='pass',port=22) # login
        sftp_client=ssh.open_sftp()
        dir1 = '/crc/logs/'+name[choice]+"/"
        dir2 = 'C:\\Users\\user\\Desktop\\'+nrnr+'\\'+name[choice]+'\\' # where we place the logs
        rfiles = sftp_client.listdir(dir1)
        rfile = ''
        utime = sftp_client.stat(dir1+rfile).st_mtime 
        last_modified = datetime.fromtimestamp(utime) # we get the date of last modified so we can iterate through them all and look for the date range
        # paramiko doesnt have a native module to grab files by date 
        for rfile in rfiles:
            utime = sftp_client.stat(dir1+rfile).st_mtime 
            last_modified = datetime.fromtimestamp(utime)
            if datetime(list1[0], list1[1], list1[2], list1[3]) > last_modified > datetime(list2[0], list2[1], list2[2], list2[3]):
                print (last_modified)
                sftp_client.get(dir1+rfile, dir2+rfile)
                a = sftp_client.get(dir1+rfile, dir2+rfile)
                # with paramiko we cant natively keep the date created of a file, this work around from pysftp( which works natively ) helps us 
                sftpattrs = sftp_client.stat(dir1+rfile) 
                os.utime(dir2+rfile, (sftpattrs.st_atime, sftpattrs.st_mtime))
        sftp_client.close()
        ssh.close()
        shutil.make_archive(dir2, 'zip', dir2)
        shutil.rmtree(dir2)      
        # we zip, we remove the folder after zipping and done!
    main()    


# p.s. its created for an old system with python 2.7!
















        


