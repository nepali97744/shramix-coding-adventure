import json

import requests
from bs4 import BeautifulSoup

def main():
    website = requests.get("https://thehimalayantimes.com/")

    raw_text = website.text
    raw_soup = BeautifulSoup(raw_text, "html.parser")

    titles = raw_soup.find_all("h3", class_ = "alith_post_title")[:5]
    
    for title in titles:
        link = title.find("a")
        if link and title.text.strip():

            article_link = link.get("href")
            
            article_title = title.text.strip()
            article_title_soup = requests.get(article_link, "html.parser")
            article_soup = BeautifulSoup(article_title_soup.text, "html.parser")

            print (article_title)
            print(article_link)
            
            articles = article_soup.find_all("div", class_ = "dropcap column-1 animate-box")
            
            
            for article in articles:
                article_text_all = article.find_all("p")
                if article_text_all:
                    for article1 in article_text_all:
                        print (article1.text)
                    

                
                
                print()
                print()
      

    
    # print(title)



if __name__ == "__main__":
    main()