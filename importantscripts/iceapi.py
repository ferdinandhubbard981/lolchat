import requests
import sys
import json


def ServerExist(baseUrl, gameTeamId):
	
	URL = baseUrl + "servers/"
	
	response = requests.get(URL).json()
	
		
	for server in response:
		if(server["name"] == gameTeamId and server["running"]):
			return "server: " + str(server["id"]) + " running on port: " + str(server["port"])
	return ""


def StartServer(baseUrl, gameTeamId):
	URL = baseUrl + "servers/"
	response = requests.get(URL).json()
	for server in response:
		if (server["running"] == False):
			URL = baseUrl + "servers/" + str(server["id"]) + "/start"
			response = requests.post(URL)
			if ("500" in str(response)):
			    return "Error: internal error iceapi"
			response = response.json()

			if (response["message"] !=  "Server started."):
				return "Error: internal error"
			URL = baseUrl + "servers/" + str(server["id"]) + "/conf"
			keyval = {"key": "registername", "value": gameTeamId}
			response = requests.post(URL, data = keyval).json()
			if ("updated" in response["message"] == False):
				return "Error: internal error"
			return "server: " + str(server["id"]) + " running on port: " + str(server["port"])
				
			
	return "Error: No servers available, please try again later"

if __name__ == "__main__":
	baseUrl = "http://localhost:8080/"
	#gameTeamId = str(sys.argv[1:][0])
	gameTeamId = "epicgamertest"
	message = ServerExist(baseUrl, gameTeamId)
	if (message == ""):
		message = StartServer(baseUrl, gameTeamId)

		print(message)
	else:
	    print(message)
		
