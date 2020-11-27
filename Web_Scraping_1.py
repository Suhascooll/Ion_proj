from bs4 import BeautifulSoup
import urllib.request


my_url= 'https://www.newegg.com/global/in-en/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=1300354'
# opening the Connection, grabbing the page
uclient= urllib.request.urlopen(my_url)
soup= BeautifulSoup(uclient)
# reading the page
raw_page= uclient.read()
uclient.close()
# html parsing
page_soup = soup(raw_page, "html.parser")
# page_soup.h1
# print(page_soup.h1)
containers = soup.find_all("div", {'class':'item-container'})
print(len(containers))
# print(containers[0])
for container in containers:
    Item_brand=container.div.div.a.img['title']
    item_title= container.div
    print(item_title)
# print(containers[0].a)
    print(Item_brand)






from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as UReq

A_page='https://www.amazon.in/s?k=kurta+for+men+latest+design&crid=10LLJD4UBTKN1&sprefix=ku%2Caps%2C920&ref=nb_sb_ss_i_7_2'
m_page=UReq(A_page)
r_page=m_page.read()
m_page.close()
m_parse=Soup(r_page, 'html.parser')
span_list=m_parse.find('span',{'class':'rush-component s-latency-cf-section'})
print(span_list.div)