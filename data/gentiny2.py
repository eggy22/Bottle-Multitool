import requests


url = input("~/URL# ")

tiny = 'http://tinyurl.com/api-create.php?url=' + url
info = requests.get(tiny)

print("~/Link# " + info.text)
