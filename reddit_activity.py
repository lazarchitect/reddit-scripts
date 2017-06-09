import praw
from time import sleep

bot = praw.Reddit(user_agent = "redditBot by /u/thelazarbeam")

subDict = {}

redditorName = input("Pick a redditor to see the top subreddits where they are most active by number of comments plus number of submitted posts.\n>> ")
howMany = int(input("How many subreddits to display?\n>> "))

print("\nokay... processing...")

redditor = bot.get_redditor(redditorName)

for x in (list(redditor.get_submitted(limit = 500)))+(list(redditor.get_comments(limit = 500))):
	#get the name of the subreddit that comment object x or post object x came from.
	#If a subDict entry for it exists, add 1 to that entry's value.
	#if not, create a entry and initialize it to 1.
	subName = str(x.subreddit)
	
	if subName in subDict:
		subDict[subName]+=1
	else:
		subDict[subName] = 1
		print("Gathering subreddit data...")
		sleep(.2)
		
#create a list of the values in subDict. sort it. then for each value in the list, each subreddit that corresponds to that value is printed

valueList = [subDict[x] for x in subDict]

valueList.sort(reverse=True);#sort it. too lazy to write one.

finalListofSubreddits = []

for y in valueList:#iterate through the numbers.
		for z in subDict:#iterate through the dictionary.
			if(subDict[z] == y and z not in finalListofSubreddits):#if the number at this dictionary spot is the same as the number...
				finalListofSubreddits.append(z)#add it to the final list

counter=0				
for asdf in finalListofSubreddits:
	print(asdf+": "+str(subDict[asdf]))
	counter+=1
	if(counter>howMany):
		break