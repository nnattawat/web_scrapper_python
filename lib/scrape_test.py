import json
import unittest
from unittest.mock import patch
from lib.scrape import get_popular_news
from lib.test_data import HTML_TEXT

class TestScrape(unittest.TestCase):
  @patch('lib.scrape.requests.get')
  def test_get_news(self, mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = HTML_TEXT 

    response = get_popular_news(900)
    self.assertEqual(response, [{
      'score': 973,
      'title': 'Time to Upgrade Your Monitor',
      'url': 'https://tonsky.me/blog/monitors/'
    }])


if __name__ == "__main__":
    unittest.main()
