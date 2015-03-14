import urllib.request
import json

user = 'user'
url = 'http://graph.facebook.com/' + user + '/picture?type=large'

img = urllib.request.urlopen(url).read()

myFile = user+'.jpg'

f = open(myFile, 'wb')
f.write(img)
f.close()

print(myFile, "gradado no diretório")
