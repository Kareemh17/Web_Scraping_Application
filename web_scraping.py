import requests
import pandas as pd
from bs4 import BeautifulSoup as soup
import webhoseio # news API
from pinance import Pinance # Stock API
webhoseio.config(token="8d786df0-7885-4818-a4d2-0562b9507f1f")
keywords = ['$','clinical','trial','phase','investment','position','price','buy','sell']
# my_url = 'http://topforeignstocks.com/stock-lists/the-complete-list-of-biotech-stocks-trading-on-nasdaq/' # List of biotech companies (outdated source)
# uClient = requests.get(my_url) #downloads webpage
# page_html = uClient.text
# page_soup = soup(page_html, "html.parser")
# bio_tech_companies = page_soup.findAll("td",{"class":"column-2"}) # specific to name
# bio_tech_companies_symbol = page_soup.findAll("td",{"class":"column-3"}) # specific to symbol
NASDAQ_File = pd.read_csv('NASDAQ_Company_List.csv')
Industry = NASDAQ_File['Industry']
Symbol = NASDAQ_File['Symbol']
Name = NASDAQ_File['Name']
for i in range(len(Industry)):
    if 'Biotechnology' in str(Industry[i]) or 'Pharmaceuticals' in str(Industry[i]):
        query = str(Name[i]) # gets name of biotech company
        query_symbol = str(Symbol[i]) # gets symbol of biotech company
        stock = Pinance(query_symbol)
        stock.get_quotes()
        try: # necessary if stock.get_quotes returns an empty or incomplete dictionary
            if stock.quotes_data['tradeable'] == True:
                stock_price =((stock.quotes_data['regularMarketPrice']))
                if stock_price < 35.00:
                    query_params = {
                    "q": "language:english site_type:news "
                    "title: {0}".format(query),
                    "sort": "crawled",
                    }
                    output = webhoseio.query("filterWebContent", query_params)
                    count = 0 # used to limit number of articles printed on a certain company
                    for i in range(len(output['posts'])):
                        while count < 5:
                            if any(n in keywords for n in output['posts'][i]['title'].lower()):
                                print(output['posts'][i]['title'])
                                print(output['posts'][i]['thread']['site_full'])
                                count +=1
        except:
            print("Empty Dictionary")


#uClient.close()