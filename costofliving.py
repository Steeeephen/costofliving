import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://www.numbeo.com/cost-of-living/prices_by_city.jsp?displayCurrency=EUR&itemId=101&itemId=100&itemId=228&itemId=224&itemId=60&itemId=66&itemId=64&itemId=62&itemId=110&itemId=118&itemId=121&itemId=14&itemId=19&itemId=17&itemId=15&itemId=11&itemId=16&itemId=113&itemId=9&itemId=12&itemId=8&itemId=119&itemId=111&itemId=112&itemId=115&itemId=116&itemId=13&itemId=27&itemId=26&itemId=29&itemId=28&itemId=114&itemId=6&itemId=4&itemId=5&itemId=3&itemId=2&itemId=1&itemId=7&itemId=105&itemId=106&itemId=44&itemId=40&itemId=42&itemId=24&itemId=20&itemId=18&itemId=109&itemId=108&itemId=107&itemId=206&itemId=25&itemId=32&itemId=30&itemId=33").text

soup = BeautifulSoup(page, 'html.parser')


dict_ = {}
for i in soup.find_all('tbody')[0].find_all('tr'):
	x = i.find_all('td')
	place = x[1].text
	list_ = []
	for j in x[2:]:
		list_.append(float(j.text))
	dict_[place] = list_
df = pd.DataFrame(dict_)

indices = []
for i in soup.find_all('th'):
	indices.append(i.text)

df.set_index([pd.Series(indices[2:])],inplace = True)

print(df.shape)