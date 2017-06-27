import sys
import requests
import os
import json
import funcs
from colorama import init
from colorama import Fore, Back, Style

init(autoreset = True)

if (len(sys.argv) > 1):
	if (str.lower(sys.argv[1]) == "add"):
		# Add a server to the Server's list
		if (len(sys.argv) == 4):
			password = input ("CCVShell Password (config.json): ")
			local = input ("Local Directory (for Syncing): ")

			funcs.addServer(sys.argv[2], sys.argv[3], password, local)
		else:
			print("Usage: CCVShell add [NAME] [HTTP ENDPOINT / SERVER URL]")
			print("(Adds a new server to the local configuration)")
	elif(str.lower(sys.argv[1]) == "list"):
		
		if (len(sys.argv) == 2):
			funcs.addLF()

			# List all the servers in the configuration
			servers = (funcs.getAllServers())

			for x in servers:
				information = funcs.getServerInfo(x.replace(".json" , ""))
				print(Fore.WHITE + information.get("Name") + Fore.GREEN  + " (" + information.get("Endpoint") + ")")
		elif (len(sys.argv) == 3):
			funcs.addLF()

			servername = sys.argv[2];
			information = funcs.getServerInfo(servername.replace(".json", ""))

			

