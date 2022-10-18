#rulare python3 lab1.py
import requests

#ex1
url = 'https://sprc.dfilip.xyz/lab1/task1/check'

param = {"nume" : "Stan Sabina", "grupa" : "341C3"}
secret = {"secret": "SPRCisNice"}
secret2 = {"secret2" : "SPRCisBest"}

x = requests.post(url, params=param, data=secret, headers=secret2)

print(x.json())

#ex2
url2 = 'https://sprc.dfilip.xyz/lab1/task2'

jsonp = {'username':'sprc', 'password':'admin', 'nume':'Stan Sabina'}

y = requests.post(url2, json=jsonp)

print(y.json())

#ex3
login_url = 'https://sprc.dfilip.xyz/lab1/task3/login'
get_url = 'https://sprc.dfilip.xyz/lab1/task3/check'

jsonp = {'username':'sprc', 'password':'admin', 'nume':'Stan Sabina'}


s = requests.Session()
y = s.post(login_url, json=jsonp)
r = s.get(get_url)

print(r.json())
