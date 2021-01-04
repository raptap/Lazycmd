import sys
import os
import time
import socket
import random

#sockets * Bytes
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#end

# Varible
def ping():
	os.system("clear")
	print(" proticols : -n -l ?")
	print("")
	print("ctrl + c to goto Menu")
	ping = input("Targets IP: ")
	os.system("ping " + ping)
	if ping == "?":
		print(" -n is how many times it is going to ping")
		print(" for example -n 1 its only going to ping 1 time")
		print("")
		print(" -l means how many packets you want for example")
		print(" -l 534 it will send that many packets the limit is 65500")
		print("")
		input(" Press Enter ")
		os.system("clear")
		Main()

def dos():
	os.system("python doss.py")
	os.system("exit")

def netc():
	os.system("python3 brutedum.py")
	os.system("exit")


def prox():
	os.system("clear")
	os.system("proxychains firefox")
def pscan():
	pscan = input("Targets IP: ")
	Pop = input("do you want to be anounimous when you pscan Y/N: ")
	if Pop == "N":
		os.system("clear")
		os.system("nmap " + pscan )
	elif Pop == "Y":
		os.system("clear")
		os.system("proxychains nmap " + pscan )
		input("         ENTER TO QUIT     ")
		print("")
		print("")
		print("")
		Main()
	elif Pop == "y":
		os.system("clear")
		os.system("proxychains nmap " + pscan )
		input("         ENTER TO QUIT     ")
		print("")
		print("")
		print("")
		Main()
	elif Pop == "n":
		os.system("clear")
		os.system("nmap " + pscan )
		input("         ENTER TO QUIT     ")
		print("")
		print("")
		print("")
		Main()

def inj():
	os.system("clear")
	os.system("figlet INJECTION")
	inj = input("Network to attack: ")
	os.system("sqlmap " + inj )
	input("      ENTER TO QUIT     : ")
	os.system("Clear")
	Main()
	
def wp():
	os.system("clear")
	wp = input("Enter Targets URL: ")
	os.system("clear")
	os.system("wpscan --url " + wp )
	Main() 

def se():
	os.system("clear")
	os.system("sudo setoolkit")

def fan():
	os.system("clear")
	os.system("python3 fan.py")
	os.system("exit")

def cmd():
	os.system("clear")
	os.system("figlet   CMD")
	print("back for Menu")
	print("")
	print("")
	print("")
	print("")
	print("")
	JEK = input("> ")
	if JEK == "back":
			os.system("clear")
			Main()
	else:
		os.system(JEK)
		cmd()

def website():
	os.system("clear")
	os.system("figlet Smart Lookup ")
	print("1) website ")
	print("2) google ")
	smartl = input("choose: ")
	if smartl == "1":
		website = input(" Enter website: ")
		os.system("firefox " + website )
	elif smartl == "2":
		os.system("firefox www.google.com") 


def shhh():
	os.system("clear")
	os.system("figlet .sh")
	sh = input("> ")
	if sh == "?":
		os.system("clear")
		print("        [ sh    commands     ]     ")
		print("config = check ip [need root privalges] ")
		print("prox = proxy generator ")
		print("python = python script ")
		print("pyt = python terminal")
		print("file = read a file ")
		print("back = back to Lazycmd")
		input("Press enter to go back ")
		os.system("clear")
		shhh()	

	elif sh == "file":
			ddd = input("Text File: ")
			names = open(ddd, 'r')
			names_list = []
			for name in names:
				names_list.append(name)
			namess = ""
			for name in names_list:
				namess += f"{name} \n"
			os.system("clear")
			print(namess)
			print("")
			input("     ENTER TO QUIT   ")
			shhh()
	elif sh == "config":
			os.system("clear")
			os.system("sudo su")
			os.system("clear")
			os.system("ifconfig")
			print("")
			input("       ENTER TO QUIT      ")
			shhh()
	elif sh == "python":
			os.system("clear")
			pythonn = input("file name: ")
			os.system("mousepad " + pythonn + ".py")
			os.system("exit")
	elif sh == "prox":
			os.system("clear")
			print("1) socks4")
			print("2) socks5")
			print("3) http ")
			prox = input(" > ")
			if prox == "3":
				os.system("clear")
				print("50.201.51.216:8080")
				print("177.190.177.145:8080")
				print("162.248.164.72:8080")
				print("45.126.88.26:8080")
				print("41.71.24.176:8080")
				print("176.113.82.220:3128")
				print("177.155.215.89:8080")
				print("176.123.164.240:58488")
				print("109.86.182.203:3128")
				print("181.39.22.149:8080")
				print("103.209.65.12:6666")
				print("93.185.96.61:43749")
				print("79.115.245.227:8080")
				print("103.78.80.170:38903")
				print("171.35.173.48:9999")
				print("139.162.21.83:8080")
				print("62.133.130.206:3128")
				print("190.14.225.117:3128")
				print("89.187.177.107:80")
				print("185.189.12.68:8080")
				print("45.63.82.243:3128")
				print("159.203.82.173:3128")
				print("172.104.169.77:8080")
				print("36.67.253.135:40778")
				print("212.227.164.87:80")
				print("175.42.128.240:9999")
				print("195.158.3.198:3128")
				print("180.109.124.207:4216")
				print("61.29.96.146:80")
				print("91.193.253.188:23500")
				print("134.236.150.196:8080")
				print("114.5.24.14:8080")
				print("60.53.196.53:8080")
				print("49.65.135.106:4216")
				print("183.88.195.21:8080")
				print("69.71.67.149:3128")
				print("45.173.196.51:80")
				print("200.89.178.159:8000")
				print("36.74.181.168:3128")
				print("154.113.69.154:8080")
				print("")
				input("     ENTER TO QUIT   ")
				shhh()
			elif prox == "2":
					os.system("clear")
					print("43.224.8.116:6667")
					print("27.116.51.186:6667")
					print("181.129.7.202:6699")
					print("103.21.163.76:6667")
					print("103.241.227.98:6667")
					print("103.216.82.19:6667")
					print("188.166.21.245:4216")
					print("43.224.116.242:1080")
					print("172.107.1.44:1080")
					print("134.209.100.103:12685")
					print("192.169.243.124:54477")
					print("113.160.188.21:1080")
					print("149.202.161.61:9991")
					print("188.166.255.30:1080")
					print("212.49.69.67:9999")
					print("172.107.1.175:1080")
					print("103.216.82.43:6667")
					print("13.250.1.245:1080")
					print("184.185.2.12:4145")
					print("150.129.54.111:6667")
					print("172.107.1.250:1080")
					print("125.135.221.94:54557")
					print("172.107.1.58:1080")
					print("104.248.129.125:8080")
					print("172.107.1.109:1080")
					print("220.78.36.91:1080")
					print("184.185.2.209:4145")
					print("54.171.243.162:1080")
					print("103.216.82.28:6667")
					print("43.224.8.125:6667")
					print("137.74.153.112:1080")
					print("116.202.185.45:1085")
					print("116.202.185.45:1181")
					print("178.165.44.122:1080")
					print("154.72.204.78:8080")
					print("166.62.85.184:12994")
					print("149.129.61.6:1080")
					print("8.210.5.23:8080")
					print("47.242.170.47:8080")
					print("")
					input("   ENTER TO QUIT ")
					shhh()
			elif prox == "1":
					os.system("clear")
					print("168.232.189.243:4145")
					print("118.175.93.103:43219")
					print("119.18.147.125:4145")
					print("202.51.178.126:59341")
					print("113.53.29.88:4145")
					print("210.245.51.19:4145")
					print("119.18.154.194:4145")
					print("89.239.65.140:4153")
					print("168.205.218.79:4145")
					print("202.158.49.138:39172")
					print("202.169.32.138:1080")
					print("148.77.34.194:44070")
					print("200.105.179.250:31247")
					print("185.252.77.220:4153")
					print("101.108.155.30:5678")
					print("177.124.225.106:4145")
					print("114.6.74.102:1080")
					print("103.144.146.226:4145")
					print("202.152.38.74:49420")
					print("210.245.51.14:4145")
					print("41.194.37.106:49867")
					print("152.204.128.190:41201")
					print("92.87.123.126:4145")
					print("85.109.58.210:1080")
					print("186.232.57.17:4153")
					print("187.85.150.148:55983")
					print("46.225.242.179:4145")
					print("109.224.12.170:52015")
					print("89.28.32.203:57391")
					print("202.141.242.3:55544")
					print("86.101.155.37:4153")
					print("46.188.82.11:54136")
					print("109.69.1.234:1080")
					print("84.54.202.216:4145")
					print("43.248.24.122:4145")
					print("89.39.114.41:4153")
					print("185.255.47.50:4145")
					print("101.51.59.37:3629")
					print("101.255.140.101:1081")
					print("110.78.148.221:4145")
					print("")
					input("     ENTER TO QUIT   ")
					shhh()
	elif sh == "pyt":
			os.system("clear")
			os.system("python")

	elif sh == "back":
			os.system("clear")
			Main()
		

	shhh()
#end

#Main
def Main():
	os.system("figlet LAZY  CMD")
	print("")
	print("")
	print("")
	print("")
	cmd = input("> ")
	if cmd == "?":
		print("? = Tool Menu ")
		print("update = update Lazycmd")
		print("ping = Ping tool")
		print("list = make a list for bruteforce")
		print("dos = DDOS tool")
		print("Brute = brute force atack")
		print("prox = anonimous firefox session")
		print("pscan = port scan network")
		print("inj = injection attack")
		print("wp = WPSCANN")
		print("se = socail engenier toolkit")
		print("fan = network virus infector")
		print("cmd = any kali commands")
		print("aw = opens smart lookup")
		print("sh = sh Menu")
		print("")
		input("    Press Enter   : ")
		os.system("clear")
		Main()
	elif cmd == "ping":
			ping()
		
	elif cmd == "Ping":
			ping()

	elif cmd == "dos":
			dos()

	elif cmd == "Dos":
			dos()

	elif cmd == "brute":
			netc()
	elif cmd == "Brute":
			netc()
	elif cmd == "prox":
			prox()
	elif cmd == "Prox":
			prox()
	elif cmd == "pscan":
			pscan()
	elif cmd == "Pscan":
			pscan()
	elif cmd == "inj":
			inj()
	elif cmd == "inj":
			inj()
	elif cmd == "wp":
			wp()
	elif cmd == "Wp":
			wp()
	elif cmd == "se":
			se()
	elif cmd == "Se":
			se()
	elif cmd == "fan":
			fan()
	elif cmd == "Fan":
			fan()
	elif cmd == "cmd":
			cmd()
	elif cmd == "cls":
			os.system("clear")
			Main()
	elif cmd == "aw":
			website()
	elif cmd == "Aw":
			website()
	elif cmd == "sh":
			shhh()
	elif cmd == "list":
			os.system("clear")
			print(" the file will be saved in the software")
			print(" folder and it will be a cmd file")
			print("")
			lname = input("name of file : ")
			os.system("mousepad " + lname + ".txt")
	elif cmd == "update":
			os.system("clear")
			os.system("figlet UPDATING")
			print("")
			os.system("git clone https://github.com/raptap/Lazycmd.git")
			os.system("exit")
	os.system("clear")
	Main()

os.system("clear")
Main()
