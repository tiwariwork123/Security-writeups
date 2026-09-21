import requests
from bs4 import BeautifulSoup
def scraping(url):   #defined function
   try:
      response=requests.get(url, timeout=10)  
      code=response.status_code    #fetching status code
      if code==200:                #200 means okay
        html=response.text          
        soup=BeautifulSoup(html, 'html.parser')        
        quote=soup.find_all('div',class_="quote")       
        for i,lines in enumerate(quote):
            quotes=lines.find('span',class_="text")
            authors=lines.find('small',class_="author")   
            if quotes is not None and authors is not None :
             print(f"{i}.{quotes.text}--{authors.text}")
            else:
              print("skipped broken entery")
              continue
      else:
         print(code)
         return None
   except requests.exceptions.RequestException:
      print("can't make it ")
        
scraping("https://quotes.toscrape.com")
