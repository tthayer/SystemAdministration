'''A very simple log parser for ssh connections'''

SSH_LOG_FILE_NAME = '/var/log/secure'

for line in open(SSH_LOG_FILE_NAME):
  if "sshd" in line:
    if "Accepted" in line:
      print "Connection is accepted from "
      print "User: ", line.split()[8], "IP: ", line.split()[10]
    if "session closed" in line:
      print "Connection is closed from "
      print "User: ", line.split()[10]
