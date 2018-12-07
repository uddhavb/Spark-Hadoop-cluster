import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree



df_bus=pd.read_csv('yelp_business.csv')
df_bus_att=pd.read_csv('yelp_business_attributes.csv')
df_checkin=pd.read_csv('yelp_checkin.csv')

df_bus=df_bus.head(2000)
df_bus_att=df_bus_att.head(2000)
df_checkin=df_checkin.head(2000)


#print(df_bus.columns)
#print(df_bus_att.columns)


places=np.unique(np.array(df_bus['city']))
print(places)
place=input('select a place among the following')

if(place in places):
    df_by_places=df_bus.groupby('city')
    for i,j in df_by_places:
        if(i==place):
            #print(j)
            print('The best Restaurant(s) in this area is ')
            best_rest=j
            name_stars=best_rest[best_rest['stars']==best_rest['stars'].max()]
            print(name_stars['name'])

