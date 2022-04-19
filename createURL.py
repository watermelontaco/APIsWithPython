import requests

tenant = input("Tenant ")
enviro = input("Environment ")
token = input("Token ")
#define url variable and format the string with the variables
api_url = f"https://{enviro}.reltio.com/reltio/tenants/{tenant}"
headers = {'Authorization':'Bearer' + token,}
response = requests.get(api_url, headers = headers)
print(response.json())
