import requests
import sys
import json

def requestSummonerData(summonerName, APIKey, region):
	
	URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKey
	#print (URL)
	response = requests.get(URL)
	return response.json()

def requestCurrentGame(ID, APIKey, region):
	URL= "https://" + region + ".api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + ID + "?api_key=" + APIKey
	#print (URL)
	response = requests.get(URL)
	return response.json()


def main(region, APIKey, summonerName):	
	summonerData = requestSummonerData(summonerName, APIKey, region)
	try:
		ID = summonerData['id']
	except KeyError as err:
		errorCode = str(summonerData["status"]["status_code"])
		if(errorCode ==  "404"):
			return("Error: No summoner was found in this region by that name")
		elif(errorCode == "429"):
	 		return("Error: Try again in a couple of minutes")
		else:
			return("Error: We are experiencing technical issues with the riot api, please come back later")

	currentGameData = requestCurrentGame(ID, APIKey, region)
	#print(currentGameData)
	try:
		return str((currentGameData["gameId"])) + str((currentGameData["participants"][0]["teamId"]))
	except KeyError as err:
		errorCode = str(currentGameData["status"]["status_code"])
		if(errorCode ==  "404"):
			return("Error: This summoner has not entered a game")
		elif(errerCode == "429"):
			return("Error: Try again in a couple of minutes")
		else:
			return("Error: We are experiencing technical issues with the riot api, please come back later")



if __name__ == "__main__":
	summonerName = sys.argv[1:][0].replace(" ", "")
	region = sys.argv[1:][1]
	#summonerName = "fpxtian2019"
	#region = "euw1"
	APIKey = "RGAPI-113a30ed-a315-4025-ae15-188c5975a329"
	print(main(region, APIKey, summonerName))
