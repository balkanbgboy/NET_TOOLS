#! python3
"""
author: Madolka
"""
from IPy import IP
from netaddr import IPAddress
from datetime import date
import netaddr
import sys
import ipaddress
import os
import csv
import shutil
import re
def Ip_mask():
    try:
        print('\n')
        user_input = input(
        "Enter:\n '1' if you want Mask to CIDR(/0 to 0.0.0.0)\n '2' for CIDR to Mask(0.0.0.0 to /0): ")        
        while user_input != ' ':
            if user_input == '1':
                Mask()
            elif user_input == '2':
                Cidr()
            else:
                print('\n')
                print('===' * 10)
                print("Ivalid Entry!. Try again...")
                print('===' * 10)
            Ip_mask()
    except KeyboardInterrupt:
            print("\n\nProgram aborted by user. Exiting...\n")
            sys.exit()


def Mask():
    try:
        print('\n')
        mask = input("Enter the Mask(example: 24):  ")
        try:
            if re.match('^\d\d?$', mask) is not None:
                iprange = ('0.0.0.0/' + mask)
                print('\n')
                print('===' *10)
                print('Cidr: ' + str(IP(iprange).netmask()))
                input_subnet = IP(iprange).netmask()
                octet_subnet = [int(j) for j in str(input_subnet).split(".")]
                wild_mask = []
                for i in octet_subnet:
                    wild_bit = 255 - i
                    wild_mask.append(wild_bit)
                wildcard = ".".join([str(i) for i in wild_mask])
                print('Wildcard mask: ' + wildcard)
                print('====' *10)
                menu2()
            else:
                print('\n')
                print('===' * 10)
                print("Ivalid Entry!. Try again...")
                print('===' * 10)
                Mask()
        except ValueError:
            print("Ivalid Mask!. Try again...")
            print('===' * 10)
            Mask()        
    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit()
        
def Cidr():
    try:
        from netaddr.core import AddrFormatError
        print('\n')
        cidr_user = input("Enter the CIDR(0.0.0.0 format):  ")
        try:
            if re.match('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', cidr_user) is not None:
                cidr = IPAddress(cidr_user).netmask_bits()
                print('\n')
                print('====' *10)
                print('Mask: ' + '/' + str(cidr))
                octet_subnet = [int(j) for j in str(cidr_user).split(".")]
                wild_mask = []
                for i in octet_subnet:
                     wild_bit = 255 - i
                     wild_mask.append(wild_bit)
                wildcard = ".".join([str(i) for i in wild_mask])
                print('Wildcard mask: ' + wildcard)
                print('====' *10)
                menu2()
            else:
                print('\n')
                print('===' * 10)
                print("Ivalid Entry!. Try again...")
                print('===' * 10)
                Cidr()   
        except AddrFormatError:
            print('\n')
            print('===' * 10)
            print("Invalid Cidr!. Try again...")
            print('===' * 10)
            Cidr()
    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit()   
		
def Ip_address():
                try:
                    print('\n')
                    print('===' * 10)
                    iprange = input("Enter the IP range(either format: x.x.x.x/24 or x.x.x.x/255.255.255.0): ")
                    print('===' * 10)
                    user_input = input("Enter '1' to display the file or '2' to print to csv file: ")
                    while user_input != ' ':
                        if user_input == '1':
                            try:
                                print('\n')
                                if '/' in iprange:
                                    n = ipaddress.ip_network(iprange)
                                    first, last = n[0], n[-1]
                                    print('===' * 5 + ' ' + "Network Address: " + str(first) + ' ' + '===' * 5)
                                    print("Available adresses:")
                                    for x in n.hosts():
                                        print(x)
                                    print('===' * 5 + ' '+  "Broadcast Address: " + str(last) + ' ' + '===' * 5)
                                    print('===' * 5 + ' '+ 'Mask: ' + str(IP(iprange).netmask()) + ' ' + '===' * 5)                        
                                    menu1()
                                else:
                                    print('===' * 10)
                                    print("\nIvalid Ip and Mask!. Try again...")
                                    print('===' * 10)
                                    Ip_address()  
                            except ValueError:
                                print('===' * 10)
                                print("\nIvalid Ip and Mask!. Try again...")
                                print('===' * 10)
                                Ip_address()                            
                        elif user_input == '2':
                            try:
                                if '/' in iprange:
                                    print('===' * 10)
                                    path = input('Provide the path to the "IPranges" folder in the main  folder(copy/paste from the folder) or any folder you want:\n')
                                    path = path.split(',')
                                    dst = os.path.join(*path)
                                    outputfile = iprange.replace('/','_')
                                    file1 = ('IP_range_' + outputfile + ".csv")
                                    f = open(file1, 'w')
                                    writer = csv.DictWriter(f, fieldnames=["  IP ADDRESSES ", "  NETWORK", "  BROADCAST", "  MASK"], lineterminator='\n', delimiter=',')
                                    writer.writeheader()
                                    network = IP(iprange)
                                    n = ipaddress.IPv4Network(iprange)
                                    first, last = n[0], n[-1]
                                    mask = str(IP(iprange).netmask())
                                    f.write('{0},{1},{2},{3}\n'.format('Usable Addresses',first, last, mask))
                                    f.flush()
                                    for ip in list(network)[1:-1]:
                                        f.write('{0}\n'.format(ip))
                                        f.flush()
                                    f.close()
                                    print('   ' * 30)
                                    print('===' * 30)
                                    print('***' * 8 + '  Completed! The file: ' + file1 + ' has been created!' + '***' * 8)
                                    print('===' * 30)
                                    print('   ' * 30)
                                    for filecsv in os.listdir():
                                        #if filecsv.endswith(".csv"):
                                        if 'IP_range_' in filecsv:
                                            shutil.move(filecsv, os.path.join(dst,filecsv))
                                    menu1()
                                else:
                                    print('===' * 10)
                                    print("\nIvalid Ip and Mask!. Try again...")
                                    print('===' * 10)
                                    Ip_address() 
                            except ValueError:
                                print("\n\nIvalid Ip and Mask!. Try again...\n")
                                Ip_address() 
                        else:
                              print('===' * 10)
                              print("Ivalid Entry!. Try again...")
                              print('===' * 10)
                              user_input = input("Enter '1' to display the file or '2' to print to csv file: ")
                except KeyboardInterrupt:
                    print("\n\nProgram aborted by user. Exiting...\n")
                    sys.exit()

def menu1():
    try:
        print('\n')
        user_input = input(
            "Enter:\n '1' Print another IP range\n 'q' to quit (Ctrl + C to exit at any time): ")
        while user_input != ' ':
            if user_input == '1':
                Ip_address()
            elif user_input == 'q':
                print('\n')
                sys.exit()
            else:
                print('===' * 10)
                print("Ivalid Entry!. Try again...")
                print('===' * 10)
            menu1()
    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit()
		
		
def menu2():
    try:
        print('\n')
        user_input = input(
            "Enter:\n '1' Print Another Mask\n 'q' to quit (Ctrl + C to exit at any time): ")
        while user_input != ' ':
            if user_input == '1':
                Ip_mask()
            elif user_input == 'q':
                print('\n')
                sys.exit()
            else:
                print('===' * 10)
                print("Ivalid Entry!. Try again...")
                print('===' * 10)
            menu2()
    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit()
