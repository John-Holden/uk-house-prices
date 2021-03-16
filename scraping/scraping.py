import requests
import re

from geopy.geocoders import Nominatim
from bs4 import BeautifulSoup
from datetime import datetime


# def write_to_list_file(data_to_write):
#     file_name = "rent_lists_%s" % today_date
#     f = open(file_name+".txt", "a")
#     for line in data_to_write:
#         line = line+'\n'
#         f.write(line)

def raw_data():
    geolocator = Nominatim(user_agent="geoapiExercises")
    inital_dict = {}
    postcodes = []
    prcs = []
    initial_search_page = requests.get("https://www.rightmove.co.uk/property-to-rent/find.html?searchType=RENT&locationIdentifier=REGION%5E787&insId=1&radius=0.0")
    initial_soup = BeautifulSoup(initial_search_page.content, 'html.parser')
    # print(soup)
    result_count = initial_soup.find('span', {'class' : 'searchHeader-resultCount'})
    results_num = result_count.text
    results_num = int(results_num.replace(',',''))
    index = 0
    results_num_placeholder = 20
    while index < results_num_placeholder:
        req_url = "https://www.rightmove.co.uk/property-to-rent/find.html?searchType=RENT&locationIdentifier=REGION%5E787&insId=1&radius=0.0&index="+str(index)
        print(req_url)
        index += 24
        search_page = requests.get(req_url)
        soup = BeautifulSoup(search_page.content, 'html.parser')
        addresses = soup.find_all('meta', {'itemprop' : 'streetAddress'})
        for address in addresses:
            address = address['content']
            print(address)
            location = geolocator.geocode(address)

            if location:
                data = location.raw
                loc_data = data['display_name'].split(', ')
                postcode = loc_data[-2]
            else:
                postcode  = address.split(', ')[-1]
            if ' ' in postcode:
                postcode = postcode.split(' ')[0]
            # if re.search(r'[A-Z]+\d', postcode):
            print(postcode)
            postcodes.append(postcode)
        prices = soup.find_all('span', {'class' : 'propertyCard-priceValue'})
        for price in prices:
            prcs.append(price.text)
        # i = 0
        # for address in addrs:
        #     inital_dict[address] = prcs[i]
        #     i += 1
        # print(inital_dict)
        lists = {}
        list_of_lists = set()
        i=0
        for postcode in postcodes:
            if re.search(r'[A-Z]+\d', postcode):
                PC_list = '%s_list' % postcode
                list_of_lists.add(PC_list)
                try:
                    lists[PC_list].append(prcs[i])
                except KeyError:
                    lists[PC_list] = []
                    lists[PC_list].append(prcs[i])
            i += 1
    # make_file_lists(list_of_lists)
    file_name = "rent_lists_%s" % today_date
    f = open(file_name+".txt", "w")
    for postcode_list in list_of_lists:
        f.write(postcode_list+':\n')
        for line in lists[postcode_list]:
            line = line+'\n'
            f.write(line)
        f.write('\n')
        print('%s prices:' % postcode_list)
        for price in lists[postcode_list]:
            print(price)

today_date = datetime.today().strftime('%Y-%m-%d')

raw_data()