""" Python script to create a link for the http://keikun17.github.io/sc2games-chart-client project.
	Takes a battle.net profile link and extracts the server, player ID and username from it, and creates a chart-client link """

import sys

def parseBNetProfile(profileLink):
	parts = profileLink.split("//")
	if (len(parts) < 2):
		moreParts = parts[0].split(".")
	else:
		moreParts = parts[1].split(".")
	if "www" in moreParts:
		moreParts = moreParts[1:]
	server = moreParts[0]
	evenMoreParts = moreParts[2].split("/")
	profileNum = evenMoreParts[4]
	username = evenMoreParts[6]
	return [server, profileNum, username]



def buildGraphLink(profileLink):
	data = parseBNetProfile(profileLink)
	link = 'http://keikun17.github.io/sc2games-chart-client/?region=' + data[0] + '&player_id=' + data[1] + '&player_name=' + data[2]
	return link

def main(battleNetProfileLink):
	print buildGraphLink(battleNetProfileLink)	


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "You should provide the battle.net link profile to the program e.g:"
		print "http://eu.battle.net/sc2/en/profile/3283647/1/Splash/"
		sys.exit()
	main(sys.argv[1])
	