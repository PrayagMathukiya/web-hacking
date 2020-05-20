#!/usr/bin/env python
# Don't Change The Rights , Remember Not Tool Make A Hacker , A Hacker Make Tool ;)
from urllib2 import *
from colorama import init
from termcolor import colored
import md5
init()

print(colored("""
[+]==========================Prayag Mathukiya=======================[+]
  ____      _    _____            _      _____       _____           _ 
 / ___|   _| |__|___ / _ __ _ __ (_)_ __|___  |_ _  |_   _|__   ___ | |
| |  | | | | '_ \ |_ \| '__| '_ \| | '_ \  / / _` |   | |/ _ \ / _ \| |
| |__| |_| | |_) |__) | |  | |_) | | | | |/ / (_| |   | | (_) | (_) | |
 \____\__, |_.__/____/|_|  | .__/|_|_| |_/_/ \__,_|   |_|\___/ \___/|_|
      |___/                |_|
      
[+]==========================Cyb3rpin7a Tool========================[+]
""", 'green'))
counter = 1

pass_in = raw_input("please enter the md5 hash:")
pwfile = raw_input("please enter the password file name:")

try:
        pwfile = open(pwfile, "r")
except:
        print "\nfile not found."
        quit()

for password in pwfile:
        filemd5 = md5.new(password.strip()).hexdigest()
        print "Trying password number %d: %s " % (counter,password.strip())

        counter += 1

        if pass_in == filemd5:
                print "\nMatch found. \npassword is: %s" % password
                break

else: print"\npassword not found."

k=input (colored(("press close to exit"),'red'))


