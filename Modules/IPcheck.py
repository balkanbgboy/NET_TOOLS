#! python3
"""
author: Madolka
"""
from IPy import IP, _ipVersionToLen
import sys
import ipaddress
import os
import csv
import shutil
from datetime import date
from datetime import datetime
import random
import sys
import re



def Menu_one():
    print('\n')
    print('   ' * 30)
    print('===' * 30)
    print('***' + ' This Program will ask for IP and the Mask(in 0.0.0.0 format) and\n will provide information '
	 ' about the Network, Broadcast and the Mask in bits.\n For convinience, it has Bits(/24) to octet(255.255.255.0) convertor '
	 + '***')
    print('===' * 30)
    print('   ' * 30)
    print('\n')
    try:
        user_input = input(
	"Do you have the Mask in octets(255.0.0.0 formats )?(y/n) : ")
        while user_input != 'q':
            if user_input == 'y':
                subnet_calc()
            elif user_input == 'n':
                Ip_mask()
            else:
                print('\n')
                print("Unknown command - try again!(type y or n)")
                Menu_one()
    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit()

def Ip_mask():
    try:
        print('\n')
        mask = input("Enter the Mask(example: 24):  ")
        try:
            if re.match('^\d\d?$', mask) is not None:
                iprange = ('0.0.0.0/' + mask)
                print('\n')
                print('===' *10)
                print('Subnet Mask: ' + str(IP(iprange).netmask()))
                print('===' *10)
                subnet_calc()
            else:
                print('\n')
                print('===' * 10)
                print("Ivalid Entry!. Try again...")
                print('===' * 10)
                Ip_mask()
        except ValueError:
            print("Ivalid Mask!. Try again...")
            print('===' * 10)
            Ip_mask()        
    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit()

def subnet_calc():
    try:
        # Checking IP address validity
        while True:
            print('\n')
            ip_address = input("Enter an IP address: ")

            # Checking octets
            a = ip_address.split('.')

            if (len(a) == 4) and (1 <= int(a[0]) <= 223) and (int(a[0]) != 127) and (int(a[0]) != 169 or int(a[1]) != 254) and (0 <= int(a[1]) <= 255 and 0 <= int(a[2]) <= 255 and 0 <= int(a[3]) <= 255):
                break

            else:
                print("\nThe IP address is INVALID! Please retry!\n")
                continue

        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]

        # Checking Subnet Mask validity
        while True:
            print('===' * 10)
            subnet_mask = input("Enter the subnet mask(ex 255.0.0.0): ")

            # Checking octets
            b = subnet_mask.split('.')

            if (len(b) == 4) and (int(b[0]) == 255) and (int(b[1]) in masks) and (int(b[2]) in masks) and (int(b[3]) in masks) and (int(b[0]) >= int(b[1]) >= int(b[2]) >= int(b[3])):
                break

            else:
                print("\nThe subnet mask is INVALID! Please retry!\n")
                continue

        # Algorithm for subnet identification, based on IP and Subnet Mask

        # Convert mask to binary string
        mask_octets_padded = []
        mask_octets_decimal = subnet_mask.split(".")
        # print mask_octets_decimal

        for octet_index in range(0, len(mask_octets_decimal)):

            # print bin(int(mask_octets_decimal[octet_index]))

            binary_octet = bin(
                int(mask_octets_decimal[octet_index])).split("b")[1]
            # print binary_octet

            if len(binary_octet) == 8:
                mask_octets_padded.append(binary_octet)

            elif len(binary_octet) < 8:
                binary_octet_padded = binary_octet.zfill(8)
                mask_octets_padded.append(binary_octet_padded)

        # print mask_octets_padded

        decimal_mask = "".join(mask_octets_padded)
        # print decimal_mask   #Example: for 255.255.255.0 => 11111111111111111111111100000000

        # Counting host bits in the mask and calculating number of hosts/subnet
        no_of_zeros = decimal_mask.count("0")
        no_of_ones = 32 - no_of_zeros
        # return positive value for mask /32
        no_of_hosts = abs(2 ** no_of_zeros - 2)

        # print no_of_zeros
        # print no_of_ones
        # print no_of_hosts

        # Obtaining wildcard mask
        wildcard_octets = []
        for w_octet in mask_octets_decimal:
            wild_octet = 255 - int(w_octet)
            wildcard_octets.append(str(wild_octet))

        # print wildcard_octets

        wildcard_mask = ".".join(wildcard_octets)
        # print wildcard_mask

        # Convert IP to binary string
        ip_octets_padded = []
        ip_octets_decimal = ip_address.split(".")

        for octet_index in range(0, len(ip_octets_decimal)):

            binary_octet = bin(
                int(ip_octets_decimal[octet_index])).split("b")[1]

            if len(binary_octet) < 8:
                binary_octet_padded = binary_octet.zfill(8)
                ip_octets_padded.append(binary_octet_padded)

            else:
                ip_octets_padded.append(binary_octet)

        # print ip_octets_padded

        binary_ip = "".join(ip_octets_padded)

        # print binary_ip   #Example: for 192.168.2.100 => 11000000101010000000001001100100

        # Obtain the network address and broadcast address from the binary strings obtained above

        network_address_binary = binary_ip[:(no_of_ones)] + "0" * no_of_zeros
        # print network_address_binary

        broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" * no_of_zeros
        # print broadcast_address_binary

        net_ip_octets = []
        for octet in range(0, len(network_address_binary), 8):
            net_ip_octet = network_address_binary[octet:octet+8]
            net_ip_octets.append(net_ip_octet)

        # print net_ip_octets

        net_ip_address = []
        for each_octet in net_ip_octets:
            net_ip_address.append(str(int(each_octet, 2)))

        # print net_ip_address

        network_address = ".".join(net_ip_address)
        # print network_address

        bst_ip_octets = []
        for octet in range(0, len(broadcast_address_binary), 8):
            bst_ip_octet = broadcast_address_binary[octet:octet+8]
            bst_ip_octets.append(bst_ip_octet)

        # print bst_ip_octets

        bst_ip_address = []
        for each_octet in bst_ip_octets:
            bst_ip_address.append(str(int(each_octet, 2)))

        # print bst_ip_address

        broadcast_address = ".".join(bst_ip_address)
        # print broadcast_address

        # Results for selected IP/mask
        print("\n")
        print("Network address is: %s" % network_address)
        print("Broadcast address is: %s" % broadcast_address)
        print("Number of valid hosts per subnet: %s" % no_of_hosts)
        print("Wildcard mask: %s" % wildcard_mask)
        print("Mask bits: %s" % no_of_ones)
        print("\n")

    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit()

    user_input = input(
        "Enter:\n '1' to print the Available IPs\n '2' Go back to check another IP\n 'q' to quit: ")
    while user_input != ' ':
        if user_input == '1':
            iprange = (network_address + '/' + subnet_mask)
            network = IP(iprange)
            n = ipaddress.IPv4Network(iprange)
            first, last = n[0], n[-1]
            print('\n')
            print('===' * 5 + ' ' + "Network Address: " +
                  str(first) + ' ' + '===' * 5)
            print("Available adresses:")
            for ip in list(network)[1:-1]:
                print(ip)
            print('===' * 5 + ' ' + "Broadcast Address: " +
                  str(last) + ' ' + '===' * 5)
            print('===' * 5 + ' ' + 'Mask: ' +
                  str(IP(iprange).netmask()) + ' ' + '===' * 5)
            print('\n')
            sys.exit()
        elif user_input == '2':
             Menu_one()
        elif user_input == 'q':
            sys.exit()
        else:
            print("Unknown command - try again!")
        user_input = input(
        "Enter:\n '1' to print the Available IPs\n '2' Go back to main Menu_one\n 'q' to quit: ")


# Calling the function

