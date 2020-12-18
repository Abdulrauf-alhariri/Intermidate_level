import requests
from bs4 import BeautifulSoup
import webbrowser


class RedditNews:
    def __init__(self, http_respons):
        self.http_respons = http_respons

    def __str__(self):
        return f"{self.http_respons}"

    @classmethod
    def http_respons(cls):
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        respons = requests.get(
            "https://www.reddit.com/api/trending_searches_v1.json", headers=header).json()
        return cls(respons)

    def trend_news(self):
        news_links = []
        respons = self.http_respons
        news_nr = 0
        for data in respons["trending_searches"]:
            news_nr += 1
            try:
                print("News nr ", news_nr, " ", data["results"]["data"]
                      ["children"][0]["data"]["title"])
            except IndexError:
                pass

            for data in respons["trending_searches"]:
                try:
                    news_links.append(
                        "https://www.reddit.com/" + data["results"]["data"]["children"][0]["data"]["permalink"])
                except IndexError:
                    pass

        print("\n")

        access_news = int(
            input("Please enter the indix of the news that you want to open: "))
        webbrowser.open(news_links[access_news - 1])


news = RedditNews.http_respons()
news.trend_news()
