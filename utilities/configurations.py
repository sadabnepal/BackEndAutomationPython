import configparser
import mysql.connector
from mysql.connector import Error
import paramiko as paramiko


def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


def getGitUserName(username):
    return username


def getGitPassword(password):
    return password


connect_config = {
    'host': getConfig()['SQL']['host'],
    'database': getConfig()['SQL']['database'],
    'user': getConfig()['SQL']['user'],
    'password': getConfig()['SQL']['password']
}


def createConnection():
    try:
        con = mysql.connector.connect(**connect_config)
        if con.is_connected():
            print("Connection is Successful")
            return con
    except Error as e:
        print(e)


def connectToLinux():
    host = getConfig()['Linux']['host']
    port = getConfig()['Linux']['port']
    username = getConfig()['Linux']['username']
    password = getConfig()['Linux']['password']
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh = ssh.connect(host, port, username, password)
    return ssh

def getQuery(query):
    con = createConnection()
    cursor = con.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    con.close()
    return row


def sftpuploadfile(destinationpath, localpath):
    ssh = paramiko.SSHClient()
    sftp = ssh.open_Sftp()
    destinationpath = destinationpath
    localpath = localpath
    sftp.put(localpath, destinationpath)


def sftpDownloadfile(destinationpath, localpath):
    ssh = paramiko.SSHClient()
    sftp = ssh.open_Sftp()
    destinationpath = destinationpath
    localpath = localpath
    sftp.get(localpath, destinationpath)
