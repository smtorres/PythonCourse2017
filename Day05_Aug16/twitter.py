#Register an app: https://dev.twitter.com/

#sudo pip install tweepy
import tweepy
import time

#Check the documentation page
#http://docs.tweepy.org/en/v3.2.0/
#Get access to API
auth = tweepy.OAuthHandler('your consumer key', 'your consumer secret')
auth.set_access_token('your access token', 'your access token secret')    
api = tweepy.API(auth)


#See rate limit
api.rate_limit_status()

#Create user objects
batman = api.get_user('BigDataBatman')
krugman = api.get_user('NYTimeskrugman')
mich = 'michtorresp'

#What can I do using this object?
dir(batman)

#Get some of her information
batman.id
batman.name
batman.screen_name
batman.location

#Check her tweets
batman.status
batman.status.text
batman.statuses_count

#Check her followers
batman.followers_count
batman.followers() #creates a list of user objects - only the first 20!
api.followers(batman.id,count=200) #creates a list of user objects - can get up to 200

batman.followers_ids() #creates a list of user ids - up to 5000
api.followers_ids('BigDataBatman')


for follower_id in mich.followers_ids():
	user = api.get_user(follower_id)
	print user.screen_name


bstatuses = api.user_timeline('BigDataBatman',page=1)
[x.text for x in bstatuses]


#How to deal with limits

# Extract tweets
mytweets = []
for status in tweepy.Cursor(api.user_timeline, id='michtorresp').items():
    # process status here
    mytweets.append(status.text)



#Get the first 2 "pages" of follower ids
krugmans_followers=[]

# extend:
# try x=[1,2]
# x.append([3,4])
# x.extend([3,4])

for page in tweepy.Cursor(api.followers_ids, 'NYTimeskrugman').pages(2):
    krugmans_followers.extend(page)
    time.sleep(60)
    
#Get the ids of 6000 followers
krugmans_followers=[]

for item in tweepy.Cursor(api.followers_ids, 'NYTimeskrugman').items(10):
	print item
	krugmans_followers.append(item)
	time.sleep(1)
	


