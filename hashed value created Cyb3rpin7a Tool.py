#!/usr/bin/env python
# Don't Change The Rights , Remember Not Tool Make A Hacker , A Hacker Make Tool ;)
from urllib2 import *
from colorama import init
from termcolor import colored
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
def hashing_method(passwd_hash):
	hash1 = hashlib.md5(passwd_hash)
	print (colored('your hahshed password is:','yellow')),(colored(hash1.hexdigest(),'green'))
	
def main():
	print 'password hashing script'
	passwd_hash = raw_input (colored(('ente your password:'),'yellow'))
	hashing_method(passwd_hash)
	
if __name__=='__main__':
	main()

k=input (colored(("press close to exit"),'red'))


