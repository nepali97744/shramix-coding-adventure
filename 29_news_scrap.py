
import requests
from bs4 import BeautifulSoup



def main():
    website = requests.get("https://www.thehimalayantimes.com/")

    formatted = website.text

    soup = BeautifulSoup(formatted, "html.parser")



    titles = soup.find_all("h3", class_ = "alith_post_title")
    for title in titles:
        inner_title = title.find("a")
        

        if inner_title:
            print(inner_title.get("title"))
            print(inner_title.get("href"))
            
            print()



if __name__ == "__main__":
    main()