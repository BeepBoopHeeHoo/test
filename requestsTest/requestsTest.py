import requests

dictionary = {'testuser', 'testpass'}
r = requests.get('file:///D:/Projects/urllibTest/testWebsite.html')
print(r)
