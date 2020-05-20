#!/usr/bin/env python
# Don't Change The Rights , Remember Not Tool Make A Hacker , A Hacker Make Tool ;)
from urllib2 import *
from colorama import init
from termcolor import colored
import hashlib
import urllib
import os
import re
import urllib2,os,sys
from time import sleep
import socket
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
#menu
def menu():
    print (colored( "1. Whois Lookup",'yellow'))
    print (colored( "2. DNS Lookup + Cloudflare Detector",'yellow'))
    print (colored( "3. Domain To ip",'yellow'))
    print (colored( "4. Port Scan",'yellow'))
    print (colored( "5. HTTP Header Grabber",'yellow'))
    print (colored( "6. Honeypot Detector",'yellow'))
    print (colored( "7. Robots.txt Scanner",'yellow'))
    print (colored( "8. Link Grabber",'yellow'))
    print (colored( "9. IP Location Finder",'yellow'))
    print (colored("10. Traceroute",'yellow'))


    
    
def pinta():
    try:
        choice = input('Enter your choice:')
        #Whois Lookup
        if choice == 1:
            domip = raw_input (colored(('Enter Domain or IP Address:'),'yellow'))
            who = "http://api.hackertarget.com/whois/?q=" + domip
            pwho = urlopen(who).read()
            print (colored((pwho),'green'))
            menu()
            pinta()
        #DNS Lookup + Cloudflare Detector
        if choice == 2:
            domain = raw_input (colored(('Enter Domain:'),'yellow'))
            ns = "http://api.hackertarget.com/dnslookup/?q=" + domain
            pns = urlopen(ns).read()
            print (pns)
            if 'cloudflare' in pns:
                print (colored("Cloudflare Detected!",'green'))
            else:
                print (colored("Not Protected By cloudflare",'red'))
            menu()
            pinta()
        #domain to ip
        if choice == 3:
            domain = raw_input (colored(('Enter Domain:'),'yellow'))
            print (colored(socket.gethostbyname(domain),'green'))
            menu()
            pinta()
        #Port Scan
        if choice == 4:
            domip = raw_input (colored(('Enter Domain or IP Address:'),'yellow'))
            port = "http://api.hackertarget.com/nmap/?q=" + domip
            pport = urlopen(port).read()
            print (colored((pport),'green'))
            menu()
            pinta()
        #HTTP Header Grabber
        if choice == 5:
            domip = raw_input (colored(('Enter Domain or IP Address:'),'yellow'))
            header = "http://api.hackertarget.com/httpheaders/?q=" + domip
            pheader = urlopen(header).read()
            print (colored((pheader),'green'))
            menu()
            pinta()
        #Honeypot Detector
        if choice == 6:
            ip = raw_input('Enter IP Address:')
            honey = "https://api.shodan.io/labs/honeyscore/" + ip + "?key=C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by"
            phoney = urlopen(honey).read()
            if '0.0' in phoney:
                print "Honeypot Probabilty: 0%"
            if '0.1' in phoney:
                print "Honeypot Probabilty: 10%"
            if '0.2' in phoney:
                print "Honeypot Probabilty: 20%"
            if '0.3' in phoney:
                print "Honeypot Probabilty: 30%"
            if '0.4' in phoney:
                print "Honeypot Probabilty: 40%"
            if '0.5' in phoney:
                print "Honeypot Probabilty: 50%"
            if '0.6' in phoney:
                print "Honeypot Probabilty: 60%"
            if '0.7' in phoney:
                print "Honeypot Probabilty: 70%"
            if '0.8' in phoney:
                print "Honeypot Probabilty: 80%"
            if '0.9' in phoney:
                print "Honeypot Probabilty: 90%"
            if '1.0' in phoney:
                print "Honeypot Probabilty: 100%"
            menu()
            pinta()
        #Robots.txt Scanner
        if choice == 7:
            domain = raw_input (colored(('Enter Domain:'),'yellow'))
            if 'http://' in domain or 'https://' in domain:
                pass
            else:
                domain = 'http://' + domain
            robot = domain + "/robots.txt"
            probot = urlopen(robot).read()
            print (colored((probot),'green'))
            menu()
            pinta()
        #Link Grabber
        if choice == 8:
            page = raw_input (colored(('Enter URL:'),'yellow'))
            if 'http://' in page or 'https://' in page:
                pass
            else:
                page = 'http://' + page
            crawl = "https://api.hackertarget.com/pagelinks/?q=" + page
            pcrawl = urlopen(crawl).read()
            print (colored((pcrawl),'green'))
            menu()
            pinta()
        #IP Location Finder
        if choice == 9:
            ip = raw_input (colored(('Enter IP Address:'),'yellow'))
            geo = "http://ipinfo.io/" + ip + "/geo"
            pgeo = urlopen(geo).read()
            print (colored((pgeo),'green'))
            menu()
            pinta()
        #Traceroute
        if choice == 10:
            domip = raw_input (colored(('Enter Domain or IP Address:'),'yellow'))
            trace = "https://api.hackertarget.com/mtr/?q=" + domip
            ptrace = urlopen(trace).read()
            print (colored((ptrace),'green'))
            menu()
            pinta()
        else:
            print (colored('[-] Invalid option!','red'))
            menu()
            pinta()
    except:
        print (colored('Something went wrong!','red'))
        menu()
        pinta()
menu()
pinta()


k=input("press close to exit")


