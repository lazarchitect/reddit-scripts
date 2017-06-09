#opens links to all comments from the subreddit of my choice
import praw

bot = praw.Reddit(user_agent = "redditBot by /u/thelazarbeam")

redditor = bot.get_redditor("thelazarbeam")

df = input("Pick the subreddit. >> ")

if(df == "quit"):
	exit()

for x in (list(redditor.get_comments(limit = 500))):
	if str(x.subreddit) == df:
		import webbrowser
		webbrowser.open(x.permalink)
		break