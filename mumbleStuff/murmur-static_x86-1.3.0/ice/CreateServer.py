import mice


def CreateServers(numOfNewServers):
	for num in range(numOfNewServers):
		mice.m.newServer()
	print("There are now " + str(len(mice.m.getAllServers())) + " servers.")

def DeleteServers(numOfServersToDelete):
	numOfServers = len(mice.m.getAllServers())
	if (numOfServersToDelete > numOfServers):
		numOfServersToDelete = numOfServers
	for num in range(numOfServersToDelete):
		server = mice.m.getServer(numOfServers - num)
		try:
			server.stop()
		except:
			pass
		server.delete()
	print("There are now " + str(len(mice.m.getAllServers())) + " servers.")
