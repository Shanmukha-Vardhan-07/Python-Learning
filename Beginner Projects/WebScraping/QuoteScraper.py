import requests
from bs4 import BeautifulSoup
import csv

URL="https://quotes.toscrape.com/"

def get_page(url):
    try:
        response=requests.get(url,timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error",e)
        return None
    
def scrape_quote(html):
    soup=BeautifulSoup(html,"html.parser")
    
    quotes_data=[]

    quotes=soup.find_all("div",class_="quote")

    for quote in quotes:
        text=quote.find("span",class_="text").text
        author=quote.find("small",class_="author").text

        quotes_data.append([text,author])

    return quotes_data
    
def save_to_csv(data,filename="quotes.csv"):
    with open(filename,"w",newline="",encoding="utf-8") as file:
        writer=csv.writer(file)

        writer.writerow(['Quote','Author'])

        writer.writerows(data)

        print(f"Data Saved to {filename}")

def main():
    print("Downloading file")

    html=get_page(URL)

    if html is None:
        return
    
    print("Executing Quotes:")

    quotes=scrape_quote(html)

    print(f"Found {len(quotes)} quotes")

    for i,(quote,author) in enumerate(quotes,start=1):
        print(f"{i}.{quote}")
        print(f"-{author}")

    save_to_csv(quotes)

    print("Project Completed successfully")

if __name__=="__main__":
    main()
