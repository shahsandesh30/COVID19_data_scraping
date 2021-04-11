import requests
from bs4 import BeautifulSoup
import pandas as pd

web_url='https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
html_code = requests.get(web_url).text

soup = BeautifulSoup(html_code, 'html.parser')

data = []

data_iterator = iter(soup.find_all('td'))

while True:
	try:
		country = next(data_iterator).text
		cases = next(data_iterator).text
		deaths = next(data_iterator).text
		region = next(data_iterator).text

		data.append((
			country,
			int(cases.replace(',','')),
			int(deaths.replace(',','')),
			region
			)) 

	except StopIteration:
			break

col_names = ['Country', 'Cases', 'Deaths', 'Region']
df = pd.DataFrame(data, columns=col_names)
df.to_csv('covid19.csv')