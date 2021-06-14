import os
import sys
import requests

def main():
	while True:
		a = input("root@Lazycmd> ")	
		try:
			x, ip = a.split()
			if x == "wpscan":
				wpscan(ip)
			elif x == "sql":
				sql(ip)
			elif x == "hash":
				hash(ip)
			elif x == "pscan":
				pscan(ip)
		except:
			if a == "help":
				help()
			elif a == "tools":
				tools()
			elif a == "text":
				text()
			elif a == "social":
				soc()
			elif a == "anon":
				anon()
			elif a == "":
				main()
			elif a == " ":
				main()
			elif a == "clear":
				Restart()
			elif a == "ddos":
				dos()
			else:
				print("bash: Command Not Found!")
				main()
			




def tools():
		print("========================================================= ")
		print("= (1) bruteforce          >> Opens A brute Force Tool   = ")
		print("= (2) ddos                >> Opens A ddos Attack Tool   = ")
		print("= (3) wpscan {url}        >> wpscans a webpage          = ")
		print("= (4) sql {url}           >> sql injection on a webpage = ")
		print("= (5) hash {dir}          >> Decrypts Hashes            = ")
		print("= (6) social              >> social Engenering tool kit = ")
		print("= (7) pscan {ip}          >> port scan                  = ")
		print("= (9) anon                >> anonimous firefox session  = ")
		print("========================================================= ")
		main()

def help():
		print("======================================== ")
		print("= (1) help    >> help menu             = ")
		print("= (2) tools   >> tool menu             = ")
		print("= (3) clear   >> clears terminal       = ")
		print("= (4) Text    >> Text Editor           = ")
		print("= (5) anon    >> anon firefox session  = ")
		print("======================================== ")
		main()
		
def brute():
	os.system("clear")
	os.system("python3 brutedum.py")
	Restart()

def dos(ip, port):
	os.system("clear")
	os.system("python doss.py")
	Restart()

def wpscan(ip):
	os.system("clear")
	os.system("wpscan --url " + ip)
	Restart()

def sql(ip):
	os.system("clear")
	os.system("sqlmap --forms -u " + ip)
	Restart()



def hash(ip):
	os.system("clear")
	cho = input("Would You Like To Do A --force?? y/n > ")
	if cho == "n":
		hashn = "hashcat -a 3 -m 0 " + ip + " ?a?a?a?a?a?a"
		os.system(hashn)
	else:
		hashn = "hashcat -a 3 -m 0 " + ip + " ?a?a?a?a?a?a --force"
		os.system(hashn)

def text():
	os.system("clear")
	os.system("nano ")
	Restart()

def soc():
	os.system("clear")
	os.system("sudo setoolkit")
	Restart()

def pscan(ip):
	os.system("clear")
	os.system("nmap -vv " + ip)
	Restart()

def anon():
	os.system("clear")
	os.system("proxychains firefox")
	Restart()
	

def banner():
	os.system("figlet Lazycmd")


def Restart():
	os.system("clear")
	banner()
	print("")
	main()




Restart()