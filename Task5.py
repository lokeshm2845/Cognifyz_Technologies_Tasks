import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com/"  
    print(f"Fetching data from {url}...")
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        quotes = soup.find_all('div', class_='quote')
        
        if not quotes:
            print("No quotes found. The website structure might have changed.")
            return

        print("\n----- TOP QUOTES -----")
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            print(f"💬 {text}  -  {author}")
            print("-" * 40)
            
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scrape_quotes()