import requests
from bs4 import BeautifulSoup
import collections

def bfs(start):
    visited = set()
    queue = collections.deque([start])

    while queue:
        url = queue.popleft()
        print(url)

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            for link in soup.find_all('a'):
                href = link.get('href')

                if href and href.startswith('http') and href not in visited:
                    visited.add(href)
                    queue.append(href)
        except Exception as e:
            print(f"Failed to open {url}: {e}")

bfs('https://wikipedia.org')