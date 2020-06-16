import json
from sys import argv
from lib.scrape import getPopularNews

THRESHOLD = 100

if __name__ == '__main__':
    threshold = int(argv[1] if len(argv) >= 2 else THRESHOLD)

    news = getPopularNews(threshold)
    print(json.dumps(news))

