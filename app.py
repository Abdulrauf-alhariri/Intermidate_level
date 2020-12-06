import requests
from bs4 import BeautifulSoup

# Beautiful soup is a very popular python package for extracting APIs
respons = requests.get("https://stackoverflow.com/questions")

# As long as you give BeautifulSoup a html text, with a html.parser
# Because you want to parse the text
# You will be able to navigate the content of the page
soup = BeautifulSoup(respons.text, "html.parser")

# After it returns a soup, you can select what you want to find
questions = soup.select(".question-summary")

# You can use select to find what you want/ or select it
# You can use getText to get the informations as text
# Use select_one if you know that you looking after one element

for question in questions:
    print(question.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())
