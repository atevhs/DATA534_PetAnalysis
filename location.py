import pgeocode
from math import acos, sin, cos, sqrt, atan2
import pandas as pd

def get_lat_lon(x):
    data = dict()
    nomi = pgeocode.Nominatim('us')
    query = nomi.query_postal_code(x)

    data['lat'] = query["latitude"]
    data['lon'] = query["longitude"]

    return data

def get_distance():

    
    try:
        print('Enter your postcode:')
        
        postcode = int(input())
        postcode = str(postcode)

        org = pd.read_csv("Add_Lat_Lon.csv")


        a = get_lat_lon(postcode)
        distance = []
        index = []
        for i in range(len(org['lat'])):
            try:
                dis = acos(sin(a['lat'])*sin(float(org['lat'][i]))+cos(a['lat'])*cos(float(org['lat'][i]))*cos(float(org['lon'][i])-a['lon']))*6371
                distance.append(dis)
            except:
                dis = ""
                distance.append(dis)

            try: 
                if distance[i] < 100:
                    index.append(i)
            except:
                pass
        
        if len(index) == 0:
            print(f'There are no shelters within 100 km')
        else:
            print(f'There are {len(index)} shelters within 100 km')
        
        res = org.loc[index][['id', 'name', 'phone', 'website', 'postcode']]
    
    except:
        print(f'The postcode should be 5 digit number!')
        res = f'Cannot find any shelter without correct postcode'
    
    return res
