#!/usr/bin/env python
__author__ = "Muhammad Zeeshan Munir, modified by Anthony Thayer"
__copywrite__ = "Original Copyright 2013, Muhammad Zeeshan Munir, https://github.com/ZeeshanMunir/SystemAdministration"

''' Use popen to execute commands '''
def executeCmd(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    print('Command completed successfully')

''' return number of lines in /etc/udev/rules.d/70-persistent-net.rules '''
def line_count(file_name):
    with open(file_name) as f:
        return (len(f.readlines()))

## Define files to be altered
rules_file = '/etc/udev/rules.d/70-persistent-net.rules'
eth_file = '/etc/sysconfig/network-scripts/ifcfg-eth0'

## Get the new MAC address from the bad interface
## This isn't using executeCmd because new_mac_addr uses the variable being defined.
get_mac_addr = subprocess.Popen("ifconfig eth1 | awk '" + \
                                "{print $5}'", shell=True, stdout=subprocess.PIPE)

## Convert get_mac_addr to a string value and strip the newline
new_mac_addr = get_mac_addr.communicate()[0].strip()

## Find the last line number from the rules file
last_line = line.count(rules_file)

## Display the new MAC address to be used
print(new_mac_addr)

## Replace the mac address in the ifcfg-eth0 file
cmd_sed_replace_eth_file = "sed -i -r 's/(..:){5}../" + \
    new_mac_addr + "/' " + eth_file
print(cmd_sed_replace_eth_file)

## Replace the incorrect udev entries with one sed command (sed -e)
cmd_sed_replace_rules_file = "sed -i -r -e 's/^SUBSYSTEM/#SUBSYSTEM/g' " + \
    "-e '" + str(last_line) + "s/^#SUBSYSTEM/SUBSYSTEM/' " + \
    "-e '" + str(last_line) + "s/(..:){5}../" + new_mac_addr + "/' " + \
    "-e '" + str(last_line) + "s/eth1/eth0/' " + rules_file
print(cmd_sed_replace_rules_file)

## Define the start_udev command to be run last
cmd_udev = "start_udev"

#Executing Commands in shell
executeCmd(cmd_sed_replace_eth_file)
executeCmd(cmd_sed_replace_rules_file)
executeCmd(cmd_udev)
