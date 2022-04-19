import requests, os
from urllib.parse import urlparse, urljoin
#parse a generic URL
BaseUrl = urlparse("https://dev.reltio.com/reltio/tenants/7Kx3iOL9OriI2Kv")
#get input from user
envi = input('Enter Environment')
tenantid = input("Enter tenant")
token = input('Enter token' )
#Take BaseUrl and insert user values to make api_url
api_url = "{}://{}.reltio.com/reltio/tenants/{}".format(BaseUrl.scheme, envi, tenantid)
#define headers for request
headers = {'Authorization':'Bearer' + token,}
#define response
response = requests.get(api_url, headers = headers)
print(response.json())
