import requests

url = input("Input the URL\n")
r = requests.get(url)
if r.status_code == 200:
    with open('source.html', 'wb') as my_file:
        my_file.write(r.content)
    print('Content saved.')
else:
    print(f'The URL returned {r.status_code}')
