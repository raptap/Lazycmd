import sys
import os
import time
import socket
import random

def Menu():
	os.system("figlet FAN ATTACK")
	print("")
	print("")
	print("")
	IP = input("Targets IP/URL : ")
	os.system("clear")
	os.system("PORT SCANNING")
	os.system("nmap " + IP )
	time.sleep(3)
	os.system("clear")
	os.system("figlet FANNING")
	pin = os.system("ping " + IP )
	os.system("clear")
	print(" RUNNING SECURITY SCAN")
	time.sleep(2)
	os.system("proxychains wpscan -h -host+ " + IP )
	time.sleep(1)
	print(" FOUNDING MALWARE BOT ")
	print("")
	time.sleep(3)
	os.system("clear")
	os.system("figlet URL/IP  " + IP + " INFECTED")
	time.sleep(5)

Menu()
