from urllib.request import urlopen as Ureq
from bs4 import BeautifulSoup as soup
from newsapi import NewsApiClient
# pre-processor
my_url = 'http://topforeignstocks.com/stock-lists/the-complete-list-of-biotech-stocks-trading-on-nasdaq/' # List of biotech companies
uClient = Ureq(my_url) #downloads webpage
page_html = uClient.read()
page_soup = soup(page_html, "html.parser")
# print(page_soup.tbody.td)
bio_tech_companies = page_soup.findAll("td",{"class":"column-2"})
for i in range(1):
    query = str(bio_tech_companies[i].text.strip())
print(query)
newsapi = NewsApiClient(api_key='42eab217e53348febe920e907f524b0f')
top_headlines = newsapi.get_top_headlines(q=str('biotech'),
                                          language='en')
print(top_headlines)
uClient.close()
