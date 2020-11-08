from Modules.IPcheck import Menu_one
from Modules.IPSubnet import Menu_two
from Modules.IPtool import Ip_address,Ip_mask
from Modules.IPsum import Menu_tree
#from IPcheck import Menu
import sys

def user_menu():
    try:
        print('\n')
        user_input = input(
            "Enter:\n '1' Print IP addresses in IP range\n '2' Provide Network and Wildcard mask"
			"\n '3' Check Ip address/mask and provide network information"
			"\n '4' Create Subnets from Supernet: "
			"\n '5' Subnet(Route) Summarization: "
			"\n 'q' to quit (Ctrl + C to exit at any time): ")
        while user_input != ' ':
            if user_input == '1':
                Ip_address()
            elif user_input == '2':
                Ip_mask()
            elif user_input == '3':
                Menu_one()
            elif user_input == '4':
                Menu_two()
            elif user_input == '5':
                Menu_tree()
            elif user_input == 'q':
                print('\n')
                sys.exit()
            else:
                print('\n')
                print('===' * 10)
                print("Ivalid Entry!. Try again...")
                print('===' * 10)
            user_menu()
            
    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit()

user_menu()