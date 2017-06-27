import sys
import requests
import os
import json

def addLF():
	print("");

# Creates a directory when it doesn't exist
def createDir (dir):
	try:
		if (os.path.isdir(dir) == False):
			os.mkdir(dir)

		return True
	except Exception as e:
		print (e)
		return False

# Sets server information by saving to the file
def setServerInfo(name, endpoint, password, localdir):

	try:
		filename = "Server\\" + name + ".json"
		content = { "Name" : name, "Endpoint" : endpoint, "Password" : password, "LocalDirectory" : localdir }

		with open(filename, 'w') as outfile:
			json.dump(content, outfile)

		return True

	except Exception as e:
		return False

# Gets the server information from the saved server configurations
def getServerInfo(name):
	try:
		filename = "Server\\" + name + ".json"
		file = open (filename, "r")
		filecontent = (file.read())

		return json.loads(filecontent)		
	except Exception as e:
		return e

# Get all the servers from the saving directory
def getAllServers():
	if (os.path.isdir("Server\\")):
		return os.listdir("Server\\")
	else:
		return []

	
# Verify a specified CCVShell server 
def verifyServer(endpoint, password):
	url = (endpoint + "/" + "CCVShell/Handle.php?p=" + password)
	response = requests.get(url)

	return (response.status_code == 200)

# Add a server to the Servers/ directory
def addServer(name, endpoint, password, localdir):
	print ("Connecting to the server \"" + name + "\" at " + endpoint + "...")

	# Verification of the server password
	verified = verifyServer(endpoint, password)
	
	if (verified):
		#Create the localdirectory and the server directory if they don't exist in the computer
		createDir(localdir)
		createDir("Server\\")

		donesave = setServerInfo(name, endpoint, password, localdir) # Save the server information

		if (donesave) :
			print ("Saved the Server Configuration!")
		else:
			print ("Could not save the configuration please retry!")

	else:
		print ("Invalid credentials (403), Please retry")