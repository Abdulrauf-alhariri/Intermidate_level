import wikipedia
import random
import webbrowser


class RandomArticle:

    def random_article(self):
        related_name = input("Enter a related name to the object? ")
        try:
            articles = wikipedia.search(related_name)
            article = random.choice(articles)
        except:
            print("Please enter a vaild name!")
            self.random_article()

        try:
            article_page = wikipedia.page(article)
        except:
            Print("We could not find the page! Please try again.")
            self.random_article()

        print("Title: ", article)
        print("")
        print(wikipedia.summary(article, sentences=2), "\n")

        # An input to see if the user want to read the article
        # If no, let's choice another article for the user
        read_article = input(
            "Do you want to open the article in your browser?(y/n): ").lower()
        print("\n")

        if read_article == "y":
            webbrowser.open(article_page.url)

        else:
            if input("Do you want to look for an another article? (y/n): ").lower() == "y":
                self.random_article()
            else:
                print("Thanks for using the app!")


article = RandomArticle()
article.random_article()
