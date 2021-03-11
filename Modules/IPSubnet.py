#! python3
""""
this programm created subnets from supernets and creates
csv file with each subnet, Broadcast address and the Mask.
Also will ask prin or save to csv file the IPs from a range
author: Madolka
"""

from IPy import IP, _ipVersionToLen
import netaddr
from netaddr import IPNetwork
import sys
import ipaddress
import csv
import os
import shutil
from datetime import date
from datetime import datetime
import pandas as pd


class User:

    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def subnet(self):
        try:
            ip = IPNetwork(self.input1)
            subnets = ip.subnet(int(self.input2))
            return list(subnets)
        except:
            print("\n\nIvalid Entry!. Try again...\n")
            Menu_two()

    @classmethod
    def from_input(cls):
        return cls(
            input("Enter the Supernet (exm: either 10.0.0.0/20 or 10.0.0.0/255.255.255.0): "),
            input("Enter the Subnet Mask(exm: 30): "),
        )
    
class Path:

    def __init__(self,input3): 
        self.input3 = input3
    
    def path(self):
	    path = (str(self.input3))
	    path = path.split(',')
	    global dst
	    dst = os.path.join(*path)
	    return dst
		
    @classmethod
    def from_input(cls):
        return cls(
        input('Provide the path to the Subnets folder in the main folder(copy/paste from the folder) or any folder you want:\n'),
        )
		
def Menu_two():
    try:
        print('   ' * 30)
        print('===' * 30)
        print(
            '***' + ' This Program will ask for Supernet(exm: 10.0.0.0/22) and will ask for Mask(exm: 30) and\n will provide information '
                    'how many new subnets will be created.Also will create csv file with\n the new subnets, mask and Broadcast address. \n '
                    'The program will ask to diplay the availbe IPs from the generated subents if you want.'
            + '***')
        print('===' * 30)
        print('   ' * 30)
        print('---' * 30)
        user = User.from_input()
        global subnet
        subnet = user.subnet()
        print('---' * 30)
        print('This will generate ' + str(len(subnet)) + ' subnets: ')
        print('---' * 30)
        user_input3 = input(
            "If that is fine press 'y' or 'n' to start again or 'q' to exit: ")
        while user_input3 != ' ':
            if user_input3 == 'y':
                Gen_subnets()
            elif user_input3 == 'n':
                Menu_two()
            elif user_input3 == 'q':
                sys.exit()
            else:
                print('---' * 30)
                print("Unknown command - try again!")
                print('---' * 30)
                user_input3 = input(
                "If that is fine press 'y' or 'n' to start again or 'q' to exit: ")
    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit()

def menu_two():
    try:
        user_input = input(
            "Enter:\n '1' to print(save to file) the Available IPs from a range\n '2' Go back to main Menu\n 'q' to quit: ")
        while user_input != ' ':
            if user_input == '1':
                Ip_address()
            elif user_input == '2':
                Menu_two()
            elif user_input == 'q':
                sys.exit()
            else:
                print('---' * 30)
                print("Unknown command - try again!")
                print('---' * 30)
                user_input = input(
                  "Enter:\n '1' to print(save to file) the Available IPs from a range\n '2' Go back to main Menu\n 'q' to quit: ")
    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit()

def menu_three():
    try:
        user_input = input(
            "Enter:\n '1' If you want to create another IP range \n '2' Go back to the menu\n 'q' to quit: ")
        while user_input != ' ':
            if user_input == '1':
                Ip_address()
            elif user_input == '2':
                Menu_two()
            elif user_input == 'q':
                sys.exit()
            else:
                print('---' * 30)
                print("Unknown command - try again!")
                print('---' * 30)
                user_input = input(
                  "Enter:\n '1' If you want to create another IP range \n '2' Go back to t\n 'q' to quit: ")
    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit()


def Gen_subnets():		
        user = Path.from_input()
        path = user.path()
        outputfile = str(date.today())
        file1 = ('Subnets-' + outputfile + ".csv")
        f = open(file1, 'w')
        writer = csv.DictWriter(f, fieldnames=["SUBNETS", "MASK", "BROADCAST"], lineterminator='\n', delimiter=',')
        writer.writeheader()
        for ip in subnet:
            mask = IP(str(ip)).netmask()
            bcast = IP(str(ip)).broadcast()
            f.write('{0},{1},{2}\n'.format(ip, mask, bcast))
            f.flush()
        f.close()
        print('   ' * 30)
        print('===' * 30)
        print('***' * 8 + " Completed! File: " + file1 + " has been created! " + '***' * 8)
        print('===' * 30)
        print('   ' * 30)
        for filecsv in os.listdir():
            if 'Subnets-' in filecsv:
                shutil.move(filecsv, os.path.join(str(dst), filecsv))
        user_input3 = input(
            "Enter 'y' to display the file and generate IPs from a range or 'q' to exit: ")
        try:
            while user_input3 != ' ':
                if user_input3 == 'y':
                    df = pd.read_csv (os.path.join(dst, file1))
                    df1=df.to_string(index=False)
                    print('---' * 30)
                    print (df1)
                    print('---' * 30)
                    print('\n')
                    menu_two()
                elif user_input3 == 'q':
                    print('---' * 30)
                    print("Bye!")
                    print('---' * 30)
                    sys.exit()
                else:
                    print('---' * 30)
                    print("Unknown command - try again!")
                    print('---' * 30)
                    user_input3 = input(
                     "Enter 'y' to display the file and generate IPs from a range or 'q' to exit: ")
        except KeyboardInterrupt:
            print("\n\nProgram aborted by user. Exiting...\n")
            sys.exit()
            
def Ip_address():
                try:
                    print('\n')
                    iprange_input = input("Enter the IP range from the above (either format: x.x.x.x/24 or x.x.x.x/255.255.255.0): ")
                    iprange = iprange_input.strip()
                    print('---' * 30)
                    user_input = input("Enter '1' to display the file or '2' to print to csv file: ")
                    while user_input != ' ':
                        if user_input == '1':
                            try:
                                if '/' in iprange:
                                    n = ipaddress.ip_network(iprange)
                                    first, last = n[0], n[-1]
                                    print('===' * 5 + ' ' + "Network Address: " + str(first) + ' ' + '===' * 5)
                                    print("Available adresses:")
                                    for x in n.hosts():
                                        print(x)
                                    print('===' * 5 + ' '+  "Broadcast Address: " + str(last) + ' ' + '===' * 5)
                                    print('===' * 5 + ' '+ 'Mask: ' + str(IP(iprange).netmask()) + ' ' + '===' * 5)                        
                                    print('\n')
                                    menu_three()
                                else:
                                    print('---' * 30)
                                    print("\nIvalid Ip and Mask!. Try again...")
                                    print('---' * 30)
                                    Ip_address()  
                            except ValueError:
                                print('---' * 30)
                                print("\nIvalid Ip and Mask!. Try again...")
                                print('---' * 30)
                                Ip_address()                            
                        elif user_input == '2':
                            try:
                                if '/' in iprange:
                                    print('===' * 10)
                                    #path = path.split(',')
                                    #dst = os.path.join(*path)
                                    outputfile = str(date.today())
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
                                    print('***' * 2 + '  The file has been saved in the same Folder as the Subnet file: ' + dst + '***' * 2)
                                    print('===' * 30)
                                    print('   ' * 30)
                                    for filecsv in os.listdir():
                                        #if filecsv.endswith(".csv"):
                                        if 'IP_range_' in filecsv:
                                            shutil.move(filecsv, os.path.join(dst,filecsv))
                                    menu_three()
                                else:
                                    print('---' * 30)
                                    print("\nIvalid Ip and Mask!. Try again...")
                                    print('---' * 30)
                                    Ip_address() 
                            except ValueError:
                                print("\n\nIvalid Ip and Mask!. Try again...\n")
                                Ip_address() 
                        else:
                              print('---' * 30)
                              print("Unknown command - type 1 or 2!")
                              print('---' * 30)
                              user_input = input("Enter '1' to display the file or '2' to print to csv file: ")
                except KeyboardInterrupt:
                    print("\n\nProgram aborted by user. Exiting...\n")
                    sys.exit()

