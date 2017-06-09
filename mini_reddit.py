import praw
import requests
    
def listGetter(bleh):
    try:
        submissions = list(bleh.get_hot(limit = 5))

        if(len(submissions)<1):
            print("There doesn't seem to be anything here")
        print("\n")
        wev = 0
        for y in submissions:
            wev+=1
            try:
                print(str(wev)+". "+y.title)
            except UnicodeEncodeError:
                print("UnicodeEncodeError, ignore this post")
                #extend submissions by one by setting it to a sublist of wherever it is now to 1 plus its previous length?    
        return 1
    except requests.exceptions.HTTPError:
        print("That subreddit is private or has been banned.")
        return 0    
    except praw.errors.RedirectException:        
        print("That subreddit doesn't exist.")
        return 0	
def whichOne(bleh):
    try:
        num = int(input("Pick which post you want to view, by number. \n>> "))
    except ValueError:
        print("Not a valid number, chief.")
        return
    return list(bleh.get_hot(limit=5))[num-1]
    
def opener(ThePost):
    import webbrowser
    if(ThePost.permalink==ThePost.url):
        webbrowser.open(ThePost.permalink)
    else:
        webbrowser.open(ThePost.permalink)
        webbrowser.open(ThePost.url)

if __name__ == "__main__":

    bot = praw.Reddit(user_agent = "myBot 1.0 by /u/thelazarbeam")

    TheSubreddit = bot.get_subreddit(input("Pick a subreddit to display the hottest five posts from. >> " ))

    if listGetter(TheSubreddit)==0:
        exit()

    thePost = whichOne(TheSubreddit)
    
    opener(thePost)