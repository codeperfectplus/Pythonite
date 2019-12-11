import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
prices_list = []
model_name = []
page_no = 1
for pages in [1,2,3,4,5,6,7,8,9,10,11]:
    url='https://www.flipkart.com/search?q=samsung+mobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_0_6&otracker1=AS_Query_HistoryAutoSuggest_0_6&as-pos=0&as-type=HISTORY&as-searchtext=mobile&page={}'.format(page_no)
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
#-----Geting price lists of multiple pages------------------------
    for price in soup.find_all('div',class_='_1vC4OE _2rQ-NK'):
        price_list.append(price.text)
#-----Geting model name of each price tag of lists----------------
    for model in soup.find_all('div',class_='_3wU53n'):
        model_name.append(model.text)
    page_no+=1