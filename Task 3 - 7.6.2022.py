#!/usr/bin/env python
# coding: utf-8

# ### W/o Pandas

# In[200]:


import pandas as pd

with open(r'C:\Users\saad.khan\Desktop\Tasks\Day 4\valuesTest.txt') as f:
    x = f.readlines()

x #list of string values



DOB = []
sibs = []
countries = []

for a in x:
    DOB.append(a.split(',')[0])

for b in x:
    sibs.append(b.split(',')[1])
    
for c in x:
    countries.append(c.split(',')[2:])
    
#lists hold values for each column 


# Removing {,},\n from the country column
for c in countries[1:]:
    c[0] = c[0][1:]
    c[-1] = c[-1][:-1]

for c in countries[1:-1]:
    c[-1] = c[-1][:-1]

countries[0][0] = countries[0][0][:-1]

#Lists to Series
c = pd.Series(countries[1:])
d = pd.Series(DOB[1:])
s = pd.Series(sibs[1:])

#Series to Dataframe

df = pd.DataFrame

df = pd.concat([d.rename('DOB') , s.rename('siblings'), c.rename('countries')], axis=1)

#dtype conversions
df['DOB'] = pd.to_datetime(df['DOB'])
df['siblings'] = pd.to_numeric(df['siblings'])


# Adding a Month column for the query
df['Month'] = df['DOB'].dt.month
df


# A helper function to return the no. of countries visited as a Series

def count_countries(Series):
    """A function to return the countries visited in each cell as a Series"""
    
    count = []
    
    for row in Series:
        s = ",".join(row)
        x = len(s.split(','))
        #list -> string -> elements counted
        count.append(x)
        #count -> Series
    return pd.Series(count)
        
#New column to hold the no. of countries visited
df['cCount'] = count_countries(df['countries'])


#Adding a column to store the difference b/w dates as days
df['Days'] = (pd.datetime.now() - df['DOB']).dt.days


#Querying data
df = df.query('siblings > 5 & cCount >2 & Days > 11204 & Month in [1,12]' )
df

#Removing list brackets and introducing {} ones
df['countries'] = df['countries'].transform(lambda x: ','.join(x))
df['countries'] = '{' + df['countries'].astype(str) + '}'
print(df.head(5))

#Writing to CSV
test.to_csv('final_output.csv',index=False)


# In[ ]:




