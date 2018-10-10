from bs4 import BeautifulSoup
import requests
string = "Zynerba Pharmaceuticals"
list_1 = string.split()
url="https://news.google.com/search?q=" + list_1[0] + "%20" + list_1[1]+"&hl=en-US&gl=US&ceid=US%3Aen"
print(url)
code=requests.get(url)
print(code.text)
page_soup=BeautifulSoup(code.text,'html.parser')
bio_tech_companies = page_soup.findAll("div",{"class":"ZulkBc qNiaOd"})
for i in range(len(bio_tech_companies)):
    query = str(bio_tech_companies[i].text.strip())
    if '%' or 'clinical' or 'trial' or 'investment' in query:
        print(query)
        print("\n")