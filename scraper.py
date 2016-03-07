import requests

url_base = 'http://sfbay.craigslist.org/search/eby/apa'
params = dict(bedrooms=1 , is_furnished=1)
rsp = requests.get(url_base,params=params)

print(rsp.url)
