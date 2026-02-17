import json
from turtle import title
import requests
from bs4 import BeautifulSoup

def main():
    website = requests.get("https://thehimalayantimes.com/")

    raw_text = website.text
    raw_soup = BeautifulSoup(raw_text, "html.parser")

    titles = raw_soup.find_all("h3", class_ = "alith_post_title")[:10]
    
    for title in titles:
        link = title.find("a")
        if link and title.text.strip():

            article_link = link.get("href")
            article_title = title.text

            print (article_title.strip())
            print(article_link)
            print()
            print()
      

    
    # print(title)



if __name__ == "__main__":
    main()