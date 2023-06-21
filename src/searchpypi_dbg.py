# import required modules
import requests, sys, webbrowser, bs4

# download search result page
print('Searching...')
res = requests.get('https://google.com/search?q=' 'https://pypi.org/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
print(res) # output
# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(soup))
# Select link elements with the CSS class 'package-snippet'
linkElements = soup.select('.package-snippet')
print(str(linkElements))
print(linkElements.attrs)
# We want at most 5 search results
numOpen = min(5, len(linkElements))

for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElements[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
