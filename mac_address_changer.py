#!/usr/bin/env python

import os, subprocess

__author__ = "Muhammad Zeeshan Munir"
__copyright__ = "Copyright 2013, Muhammad Zeeshan Munir"

'''
   Check and tested with CentOS 6.4 for KVM machines with Python 2.7 and Python 3.3
   You just need to change 'new_mac_addr' field to the address from VM details.
   You can find it in details of VM in KVM or in VCenter.
   Using python's subprocess.Popen to execute the commands in shell. 
   '''
def executeCmd(command):
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
  print('Command completed successfully')

''' return number of lines in /etc/udev/rules.d/70-persistent-net.rules ''' 
def line_count(file_name):
  with open(file_name) as f:
    return (len(f.readlines()))


rules_file = '/etc/udev/rules.d/70-persistent-net.rules'
eth_file = '/etc/sysconfig/network-scripts/ifcfg-eth0'
new_mac_addr = input('Please enter a new MAC address: ') #'00:00:00:00:00:00' #Don't forget to change it.
cmd_mac_replace = "sed  -i -r 's/(..:){5}../"+new_mac_addr+"/' "+eth_file
cmd_subsystem_comment = "sed -i -r 's/^SUBSYSTEM/#SUBSYSTEM/g' " + rules_file
last_line = line_count(rules_file)
cmd_subsystem_uncomment = "sed -i -r '"+str(last_line)+"s/^#SUBSYSTEM/SUBSYSTEM/' "+rules_file
cmd_subsystem_replace_mac = "sed -i -r '"+ str(last_line)+"s/(..:){5}../"+new_mac_addr+"/' "+rules_file
cmd_subsystem_replace_eth_name = "sed -i -r '"+ str(last_line)+"s/eth1/eth0/' "+rules_file
cmd_udev = "start_udev"

#Executing commands in shell
executeCmd(cmd_mac_replace)
executeCmd(cmd_subsystem_comment)
executeCmd(cmd_subsystem_uncomment)
executeCmd(cmd_subsystem_replace_mac)
executeCmd(cmd_subsystem_replace_eth_name)
executeCmd(cmd_udev)

