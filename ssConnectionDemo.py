from utilities.configurations import *
import csv


command1 = "ls -a"
command2 = "cat demofile"

#Create connection
ssh = connectToLinux()

#execute command
stdio, stdout, stderr = ssh.exec_command(command1)
print(stdout.readlines())

#extract output
stdio, stdout, stderr = ssh.exec_command(command2)
# print(stdout.readlines())
lines = stdout.readlines()
print(lines[1])

#Upload file from local to Linux machine
destinationpath = "script.py"
localpath = "batchFiles/script.py"
sftpuploadfile(localpath, destinationpath)


destinationpath = "loanasa.csv"
localpath = "batchFiles/loanasa.csv"
sftpuploadfile(localpath, destinationpath)

#Trigger the Batch commands
stdio, stdout, stderr = ssh.exec_command("python script.py")

#Download file to local System
sftpDownloadfile("loanasa.csv", "outputFiles/loanasa.csv")

#Parse output file with CSV
with open("outputFiles/loanasa.csv") as csvFile:
    csvReader = csv.reader(csvFile, delimeter=',')
    for row in csvReader:
        if(row[0] == "32321"):
            assert row[1] == "rejected"


ssh.close()