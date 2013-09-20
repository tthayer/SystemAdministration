#!/usr/bin/env python

import paramiko, os


''' A simple ssh client using RSA Key using paramiko python ssh library - Tested on Python 2.7'''

__author__ = "Muhammad Zeeshan Munir"
__copyright__ = "Copyright 2013, Muhammad Zeeshan Munir"


hostname = 'zee.linxsol.com'
port = 3333
user_name = 'zee'
rsa_key_file = '/Users/Zeeshan/.ssh/id_rsa'



def create_connection(hostname, user_name, key_file, port=22):
  '''Method for establishing SSH connection'''
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  if os.path.exists(rsa_key_file):
    rsakey = paramiko.RSAKey.from_private_key_file(key_file)
    ssh.connect(hostname,port, username=user_name, pkey=rsakey)
  else:
    raise TypeError('Private key file does not exist')
  return ssh

def close_connection(ssh):
  '''Lets be good cops and close the connection'''
  if ssh != None:
    ssh.close()
    print('Connection closed')
  
def send_command(ssh, command):
  '''Method to execute commands on the server'''
  print('Executing..... ' +command)
  stdin, stdout, stderr = ssh.exec_command(command)
  output = stdout.readlines()
  return output


ssh = create_connection(hostname, user_name,rsa_key_file,port)
output = send_command(ssh, 'ls -l')
