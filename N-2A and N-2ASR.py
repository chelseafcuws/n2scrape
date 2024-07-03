import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

param = {
    'company': '',
    'CIK': '',
    'type': 'N-2/A',
    'owner': 'include',
    'count': '100',
    'action': 'getcurrent'
}
header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'en-US,en;q=0.9',
    'Cache-Control':'max-age=0',
    'Cookie':'nmstat=ed939d7a-41eb-16a7-af59-f15eeb6d9de7; _gid=GA1.2.1304728100.1719816861; _gat=1; _gat_GSA_ENOR0=1; _gat_GSA_ENOR1=1; _gat_UA-30394047-1=1; ak_bmsc=E039CBCEFBE290E8A8427E0A4DB92AAE~000000000000000000000000000000~YAAQXp42F1U5hVWQAQAAj2kfchjUaL8w8OUmhhDKa25GUWHTo8gjpcR7mqFjG9k0chCMbLU5bXTXqovZb48UGHkHqkOlvaPkB3MeOKntsN07vzTmQ9sa9bvYl/VYVEjdiZ27frAbdBqcmOmNFti0gKbjVhuy7Acst9xppKoskyLyQYAYQIwEVlUUH7Vd2UDExQ0ffr4IQ2sRTYpyR77tMwDtp+JLR1lnhzd6dLnxhRt6xBXTPklhcrKn+sn9kBPHfzfTrQSTJrIF6U5xEd5JfSd4l63Mjy8yqh8FWbOF+in6lUztY6QVLMQTnNVYEXY6+GbKccjU6z3HySCSWyj94ErBodrb3z0SFdowJlc6MPecflJTNGXjZ0E0qrSzW6PL7YtUa5SnWeKCfsDoT/APFWfw5bv+GyVPJSZY2O5EFVoXQQATUxIzo9QJaupHEyns7G6qPrp7Cs704I8=; bm_sv=415238C250220228CB743F6E5174222A~YAAQCNYsF7UwJ3CQAQAAGxYgchiyQNHVkWvxrg82XLs/OoPBZSK4zGm9YS9JwjET4wG7Jo3aJHzAD8VDDLHMsAXFb9Rs+bWcREU/L9ri/oElDz3Qka0gPta03B3rox5SLde1XITkcKWy7Uzjdds0XGkk88Lh2WjMb6pqa8Ege/jKpflJnjTwr6vFZME/VhXYyHxSZhR2GHhKi6+xluxPy278Oj5J9rrXR2bCuyPXUzOKMsCX3fuSRCJVH0En~1; _ga_300V1CHKH1=GS1.1.1719901579.22.1.1719901624.0.0.0; _ga=GA1.1.606435860.1716805487; _ga_CSLL4ZEK4L=GS1.1.1719901581.22.1.1719901624.0.0.0; _4c_=%7B%22_4c_s_%22%3A%22dZJdT8IwFIb%2FCjnXbGm7tbTcGUyMF2o0flwSaTvWoIx0k6lk%2F91zYIAQ3c3Sp885fXfWDbSlX8KYj7gxjKtMCc2GsPBfNYw3EIOj1xrGYIR1RfFqE1nkRZJLyRNjVZ5w7txopri3zMMQPqmXUNpoMeK54d0Q3HLfI3rn6zBfHj0jOMNjRYZeWDW9SGl4LhkTwohTlwi5%2B5YO%2FtyP7aHVbkMIzHOibgmqq3h26v%2BqXfXqBmzlPB7PTcp1ypKixhzNN5KMMaCmlfuwzbT5WpHW%2BtmgdgvccH4drJ%2B2wTUl1ctMHWnpw7zEIYBWOVGKBjwVEhdtWLqqPS%2Fs6aFQGXJnsWprT8WTMlbvfsAFyRX%2BU3jZVlDc6Asf41bDVR0aSlp7m86rdQ%2FwHuxYsmPPgagbPE4ekN%2F%2BIveTu5seXV1Mn64vKQxTeSa1YimOVmkmcz2Crp8s3jetmZCcGZxc8wZj%2FGhGT9d1Pw%3D%3D%22%7D',
    'Priority':'u=0, i',
    'Sec-Ch-Ua':'"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'none',
    'Sec-Fetch-User':'?1',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
resp = requests.get('https://www.sec.gov/cgi-bin/browse-edgar', params=param, headers=header)
soup = BeautifulSoup(resp.content, 'html.parser')
df = pd.read_html(StringIO(str(soup.find_all('table')[-2])))[0]
param = {
    'company': '',
    'CIK': '',
    'type': 'N-2ASR',
    'owner': 'include',
    'count': '100',
    'action': 'getcurrent'
}
resp = requests.get('https://www.sec.gov/cgi-bin/browse-edgar', params=param, headers=header)
soup = BeautifulSoup(resp.content, 'html.parser')
df2 = pd.read_html(StringIO(str(soup.find_all('table')[-2])))[0]

Fund = []
CIK = []
for i in json.loads(df[df['Form'].isna()].to_json(orient='records')):
    Fund.append(i['Description'].split(' (')[0].strip())
    CIK.append(i['Description'].split(' (')[1].replace(')',''))
df = df[df['Form'].notna()].copy()
df['CIK'] = CIK
df['Fund'] = Fund
df['Accession number'] = df['Description'].str.split(':').str[1].str.strip().str.split().str[0]
df['Act'] = df['Description'].str.split(':').str[2].str.strip().str.split().str[0]
df = df[['CIK', 'Fund', 'Form', 'Act', 'Filing Date', 'Accession number']]

df2 = pd.DataFrame()
Fund = []
CIK = []
try:
    for i in json.loads(df2[df2['Form'].isna()].to_json(orient='records')):
        Fund.append(i['Description'].split(' (')[0].strip())
        CIK.append(i['Description'].split(' (')[1].replace(')',''))
    df2 = df2[df2['Form'].notna()].copy()
    df2['CIK'] = CIK
    df2['Fund'] = Fund
    df2['Accession number'] = df2['Description'].str.split(':').str[1].str.strip().str.split().str[0]
    df2['Act'] = df2['Description'].str.split(':').str[2].str.strip().str.split().str[0]
    df2 = df2[['CIK', 'Fund', 'Form', 'Act', 'Filing Date', 'Accession number']]
except:pass

df3 = pd.concat([df, df2])
df3['Filing Date'] = pd.to_datetime(df['Filing Date'])
df3['Filing Date'] = df3['Filing Date'].dt.strftime('%m/%d/%Y')

df3.to_excel('N-2A and N-2ASR.xlsx', index=False)