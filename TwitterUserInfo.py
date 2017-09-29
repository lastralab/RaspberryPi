import urllib
import pprint
import json
from twurl import augment
#twurl is a python file that has imported oauth
#which has the keys for the authorization

print ('====================== Calling Twitter...=========================')
#user timeline:

user = raw_input('Enter username: - ')
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
        {'screen_name': user, 'count': '8'} )
connection = urllib.urlopen(url)
data = connection.read() #body
headers = connection.info().dict #headers

result = json.loads(data)

print ('***********************************BODY:**************************************')
pprint.pprint(result)


