from urllib.request import FancyURLopener

url = "https://djmag.com/top100djs"

class AppURLopener(FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
response = opener.open(url)

data = response.read()
text = data.decode("utf-8")
print(text)

with open('html_text.txt', 'w') as f:
    f.write(text)