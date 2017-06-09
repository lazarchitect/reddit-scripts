#opens links to as many front page posts as you want
import praw #we need our tools
import webbrowser #to display our post
r = praw.Reddit("dfdf") #instantiate a PRAW script

num = int(input("how many posts would you like to see")) #get user input in integer form

Gen = r.get_front_page(limit = num+1) #Using praw, create a generator of the posts on the front page, in object form. 
#We only need as many as the user wants.

PostList = list(Gen) #create an iterable list of that generator

for eachPost in range(num): # go through the number of posts the user wants...
	thePost = PostList[eachPost] #getting the post we want...
	theURL = thePost.url #and the URL of each of them....
	webbrowser.open(theURL) #and opening that page!