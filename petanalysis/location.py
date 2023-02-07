import pgeocode
from math import acos, sin, cos, sqrt, atan2, radians
import pandas as pd

def get_lat_lon(x):
    data = dict()
    nomi = pgeocode.Nominatim('us')
    query = nomi.query_postal_code(x)

    data['lat'] = query["latitude"]
    data['lon'] = query["longitude"]

    return data


def get_shelter(postcode = None):
    
    us =  pd.read_csv("petanalysis/US_postcode.csv", dtype = str)

    if postcode == None:
        try:
            print('Enter your postcode:')

            postcode = input()
            int(postcode)

            if len(postcode) != 5:
                return f'The postcode should be 5 digit number!'
            else:
                if sum(us.zip == postcode) == 0:
                    return f'This is not a postcode in the US!'
                
        
        except:
            return f'The postcode should not include character!'
    else:
        try:
            int(postcode)
            postcode = str(postcode) 
            if len(postcode) != 5:
                return f'The postcode should be 5 digit number!'
            else:
                if sum(us.zip == postcode) == 0:
                    return f'This is not a postcode in the US!'
        except:
            return f'The postcode should not include character!'

    org = pd.read_csv("petanalysis/OrganizationData.csv")


    a = get_lat_lon(postcode)
    distance = []
    index = []
    in_dis = []
    lat_li = []
    lon_li = []
    for i in range(len(org['lat'])):
        try:
            lat = float(org['lat'][i])
            lon = float(org['lon'][i])
            dis = acos(sin(radians(a['lat']))*sin(radians(lat)) + cos(radians(a['lat']))*cos(radians(lat))*cos(radians(lon)-radians(a['lon'])))*3959
            distance.append(dis)
            if dis < 10:
                index.append(i)
                in_dis.append(dis)
                lat_li.append(float(org['lat'][i]))
                lon_li.append(float(org['lon'][i]))
            else:
                pass
        except:
            dis = ""
            distance.append(dis)

    if len(index) == 0:
        print(f'There are no shelters within 10 miles')
    else:
        print(f'There are {len(index)} shelters within 10 miles')
        print(f'Following is the information:')

    res = org.loc[index][['id', 'name', 'phone', 'website', 'postcode']]
    
    
    return res
