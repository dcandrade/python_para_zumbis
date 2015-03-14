import urllib.request
import json

def save_image(friend)
	size = '/picture?width=200&heigth=200'
	url = 'https://graph.facebook.com'+friend['id'] + size
	image = urllib.request.urlopen(url).read()
	f = open(friend['name']+ '.jpg', 'wb')
	f.write(image)
	f.close()
	print(friend['name']+'.jpg impresso')

#get token https://developers.facebook.com/tools/explorer
url = 'https://graph.facebook.com/me/friends?access_token=<token>'
data = json.loads(resp.decode('utf-8'))

for friend in data['data']:
	save_image(friend)
