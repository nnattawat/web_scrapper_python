import requests
from bs4 import BeautifulSoup

URL = 'https://news.ycombinator.com/news'


def _getNews(url):
    res = requests.get(url)
    return BeautifulSoup(res.text, 'html.parser')


def _filterLinksByVote(news, threshold):
    popularNews = [{
        'title': link.getText(),
        'url': link.get('href', None),
        'score': score
    } for link, score in news if score > threshold]

    return sorted(popularNews, key=lambda new: new.get('score'), reverse=True)


def _mapSubTextToPoints(subtexts):
    def getPoints(subtext):
        scores = subtext.select('.score')
        return int(scores[0].getText().replace(' points', '')) if len(scores) else 0

    return map(getPoints, subtexts)

def getPopularNews(threshold):
    soup = _getNews(URL)

    links = soup.select('.storylink')
    subtexts = soup.select('.subtext')
    points = _mapSubTextToPoints(subtexts)

    return _filterLinksByVote(zip(links, points), threshold)


if __name__ == '__main__':
    print(getPopularNews(100))
