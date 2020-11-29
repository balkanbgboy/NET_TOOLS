#! python3
import sys
import os
from netaddr import *



def Menu_tree():
	print('   ' * 30)
	print('===' * 30)
	print('***' + ' This Program will summarize Subnets.Add the Subnets in Subnets.txt file in following format:\n '
				'   10.0.0.0/30\n'
				'    10.0.0.4/30\n'
				'    10.0.0.8/30\n'
				'    Run the program.The summary addresses will be displayed  '
		+ '***')
	print('===' * 30)
	print('   ' * 30)
	try:
		user_input = input(
			'Have you updated the "Subents.txt" file with the Subnet ranges?(y/n): ')
		while user_input != ' ':
			if user_input == 'y':
				sum()
			elif user_input == 'n':
				print('\n')
				print('-------------------------------------------')
				print("Update the file and run the program again!!")
				print('-------------------------------------------')
				print('\n')
				sys.exit()
			else:
				print("Unknown command - try again!")
			user_input = input(
		   "Have you updated the subents.txt file with the Subnet ranges?(y/n): ")
	except KeyboardInterrupt:
                print("\n\nProgram aborted by user. Exiting...\n")
                sys.exit()  
		
def sum():
    try:
        path = input('Provide the path where the Subnet.txt file is(copy/paste) :\n ')
        os.chdir(path)		
        with open('Subnets.txt', 'r') as in_file:
            dat_ips = [IPNetwork(line) for line in in_file.read().splitlines()]
        dat_merged_ips = cidr_merge(dat_ips)
        print('\n')
        print('----------------Summary address(es):')
        for x in dat_merged_ips:
            print(x)
        print('------------------------------------')
        print('\n')
        sys.exit()
        
    except IOError:
        print('File error detected:')

