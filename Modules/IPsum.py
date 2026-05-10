#! python3
import sys
import os
from netaddr import *



def Menu_tree():
	print('   ' * 30)
	print('===' * 30)
	print('***' + '  This Program will summarize Subnets.Add the Subnets in Subnets.txt file.\n '
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
				from Menu.user_menu import user_menu
				user_menu()
			else:
				print("Unknown command - try again!")
			user_input = input(
		   "Have you updated the subents.txt file with the Subnet ranges?(y/n): ")
	except KeyboardInterrupt:
                print("\n\nProgram aborted by user. Exiting...\n")
                sys.exit()  
		
def sum():
    try:
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        subnets_file = os.path.join(project_root, 'Subnets.txt')
        with open(subnets_file, 'r') as in_file:
            dat_ips = [IPNetwork(line) for line in in_file.read().splitlines() if line.strip()]
        dat_merged_ips = cidr_merge(dat_ips)
        print('\n')
        print('----------------Summary address(es):')
        for x in dat_merged_ips:
            print(x)
        print('------------------------------------')
        print('\n')
        try:
            user_input = input(
                "Enter:\n '1' Go back to main Menu\n 'q' to quit (Ctrl + C to exit at any time): ")
            while user_input != ' ':
                if user_input == '1':
                    from Menu.user_menu import user_menu
                    user_menu()
                elif user_input == 'q':
                    sys.exit()
                else:
                    print('===' * 10)
                    print("Ivalid Entry!. Try again...")
                    print('===' * 10)
                user_input = input(
                    "Enter:\n '1' Go back to main Menu\n 'q' to quit (Ctrl + C to exit at any time): ")
        except KeyboardInterrupt:
            print("\n\nProgram aborted by user. Exiting...\n")
            sys.exit()

    except IOError:
        print('File error detected:')

