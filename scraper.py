import requests
from bs4 import BeautifulSoup as bs4

url_base = 'http://sfbay.craigslist.org/search/eby/apa'
params = dict(bedrooms=1 , is_furnished=1)

#Create Url with url_base and params
rsp = requests.get(url_base,params=params)
html = bs4(rsp.text,'html.parser')

#print(rsp.url)
#print(rsp.text[:500])
#print(html.prettify()[:1000])
apts = html.find_all('p', attrs={'class':'row'})
#print(len(apts))

this_appt = apts[98]
#print(this_appt.prettify())

size=this_appt.find_all(attrs={'class': 'price'})[0].text
print(size)
