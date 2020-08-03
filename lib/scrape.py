import requests
from bs4 import BeautifulSoup

URL = 'https://news.ycombinator.com/news'


def _get_news(url):
    res = requests.get(url)
    return BeautifulSoup(res.text, 'html.parser')


def _filter_links_by_vote(news, threshold):
    popular_news = [{
        'title': link.getText(),
        'url': link.get('href', None),
        'score': score
    } for link, score in news if score > threshold]

    return sorted(popular_news, key=lambda new: new.get('score'), reverse=True)


def _map_sub_text_to_points(subtexts):
    def get_points(subtext):
        scores = subtext.select('.score')
        return int(scores[0].getText().replace(' points', '')) if len(scores) else 0

    return map(get_points, subtexts)


def get_popular_news(threshold):
    soup = _get_news(URL)
    links = soup.select('.storylink')
    subtexts = soup.select('.subtext')
    points = _map_sub_text_to_points(subtexts)

    return _filter_links_by_vote(zip(links, points), threshold)


if __name__ == '__main__':
    print(get_popular_news(100))
