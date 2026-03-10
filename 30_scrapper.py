from datetime import datetime

import requests
from bs4 import BeautifulSoup
import time

def main():
    
    with requests.Session() as session:
    
        now = datetime.now()
        time_string = now.strftime("%d/%m/%Y Time: %H:%M")




        #website = requests.get("https://thehimalayantimes.com/")

        
        #raw_soup = BeautifulSoup(website.text, "html.parser")

        #titles = raw_soup.find_all("h3", class_ = "alith_post_title")[:2]

        titles = website_to_scrape("https://thehimalayantimes.com/")
        write_to_file(session, time_string, titles)
    

def website_to_scrape(website):
    raw_data = requests.get(website)
    website_soup = BeautifulSoup(raw_data.text, "html.parser")
    titles = website_soup.find_all("h3", class_ = "alith_post_title" )
    return (titles)

    



def write_to_file(session, time_string,titles):
        with open("30_scrapper.txt", "w", encoding= "utf-8") as f:
            f.write(time_string + "\n")
            f.write("\n" * 5)
            for title in titles:
                link = title.find("a")
                if link and title.text.strip():

                    article_link = link.get("href")
                    
                    article_title = title.text.strip()
                    article_title_soup = requests.get(article_link)
                    article_soup = BeautifulSoup(article_title_soup.text, "html.parser")

                    
                    
                    f.write(article_title + "\n")
                    f.write(article_link + "\n")

                    # print (article_title)
                    # print(article_link)
                    
                    articles = article_soup.find_all("div", class_ = "dropcap column-1 animate-box")
                        
                        
                    for article in articles:
                        article_text_all = article.find_all("p")
                        if article_text_all:
                            for article1 in article_text_all:
                                f.write(article1.text + "\n")
                            f.write("-" * 100 + "\n\n\n\n")
                    #time.sleep(1)

            print("scrape successfull.")
                    

                    
               
        

        
    # print(title)



if __name__ == "__main__":
    main()