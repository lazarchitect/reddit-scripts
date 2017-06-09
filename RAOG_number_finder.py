import praw

r = praw.Reddit("sdfsdfs")

dick = list(r.get_subreddit("randomactsofgaming").get_hot(limit=2))[1]

booler = 1
options = []


for counter in range(101):
	booler = True
	for x in dick.comments:
		if str(counter) in x.body:
			booler = False
	if booler:		
		options.append(counter)



print(options)		