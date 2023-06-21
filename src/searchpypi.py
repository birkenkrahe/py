#! python3
# searchpypi.py - opens several search results

# import required modules
import requests, sys, webbrowser, bs4

# Check if argument is provided
if len(sys.argv) < 2:
    print("Please provide a search term")
    sys.exit()

# download search result page
print('Searching...')
res = requests.get('https://pypi.org/search/?q=' + '+'.join(sys.argv[1:]), headers={"User-Agent": "Mozilla/5.0"})
res.raise_for_status()

# Print the response text for debugging
#print(res.text)

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Replace with the correct CSS selector for search results on PyPI
linkElements = soup.select('.package-snippet')  # This might need to be updated

# We want at most 5 search results
numOpen = min(5, len(linkElements))

if numOpen == 0:
    print("No results found")
else:
    for i in range(numOpen):
        try:
            href = linkElements[i].get('href')
            if href:
                urlToOpen = 'https://pypi.org' + href
                print('Opening', urlToOpen)
                webbrowser.open(urlToOpen)
            else:
                print("No href found for result", i)
        except AttributeError as e:
            print("Error processing result", i, ":", str(e))
