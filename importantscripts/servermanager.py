import mice
import time

def main(serversandid):
	serversandid = UpdateList(serversandid)
	serversandid = CheckList(serversandid)
	for server in serversandid:
		print(server["server"])
		print("minutes: " + str(server["minutes"]))
	print("length: " + str(len(serversandid)))
	return serversandid
		
def UpdateList(serversandid):
	tempList = []
	servers = mice.m.getBootedServers()
	for server in servers:
		if (len(server.getUsers()) == 0):
			tempList.append(server)
	for server in tempList:
		contains = False
		for oldserver in serversandid:
			if (server == oldserver["server"]):
				contains  = True
		if (contains == False):
			serversandid.append({"server": server, "minutes": 0})

	x = 0
	for oldserver in serversandid:
		x += 1
		contains = False
		for newserver in tempList:
			if (oldserver["server"] == newserver):
				contains = True
		if (contains == False):
			serversandid.remove(oldserver)
	return serversandid		
			
def CheckList(serversandid):
	for server in serversandid:
		server["minutes"] += 1
		if(server["minutes"] > 30):
			server["server"].stop()
			serversandid.remove(server)
	
	return serversandid





if __name__ == "__main__":
	serversandid = [{"server": 0, "minutes": 0}]
	while(True):
		try:
			mice.m.getserver(1).delete()
		except:
			pass
	
		serversandid = main(serversandid)
		try:
			time.sleep(10)
		except KeyboardInterrupt as error:
			time.sleep(0.5)
			
		
	



