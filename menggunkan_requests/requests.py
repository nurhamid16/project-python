import requests  

api_url = 'https://api.exchangerate-api.com/v4/latest/IDR'
response = requests.get(api_url)

if rslt.status_code == requests.codes.ok :
    hasil = r
