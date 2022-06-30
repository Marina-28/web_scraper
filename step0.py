import requests


url = input("input the URL\n")
r = requests.get(url)
if r.status_code == 200:
    jdict = r.json()
    if 'content' in jdict.keys():
        print(jdict['content'])
    else:
        print("Invalid quote resource!")
else:
    print("Invalid quote resource!")