from urllib.request import urlopen

url  = "https://djmag.com/top100djs"

response = urlopen(url)
data = response.read()
text = data.decode("utf-8")
print(text)


from urllib.request import urlopen

url  = "https://djmag.com/top100djs"


def get_webpage(url):
    response = urlopen(url)
    data = response.read()
    text = data.decode("utf-8")
    return text

text = get_webpage(url)
print(text)


