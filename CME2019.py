#!/usr/bin/env python
# coding: utf-8

# In[1]:


from seaborn import *
import seaborn as sns
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
from datascience import *
from numpy import *
import numpy as np
import pandas as pd
import datetime


# In[2]:


## csv file for each day
day_1 = Table.read_table('C:/Users/dusti/OneDrive/Desktop/CMEdata/daily-standings-2019-10-07.csv')
day_2 = Table.read_table('C:/Users/dusti/OneDrive/Desktop/CMEdata/daily-standings-2019-10-08.csv')
day_3 = Table.read_table('C:/Users/dusti/OneDrive/Desktop/CMEdata/daily-standings-2019-10-09.csv')
day_4 = Table.read_table('C:/Users/dusti/OneDrive/Desktop/CMEdata/daily-standings-2019-10-10.csv')
day_5 = Table.read_table('C:/Users/dusti/OneDrive/Desktop/CMEdata/daily-standings-2019-10-11.csv')
day_6 = Table.read_table('C:/Users/dusti/OneDrive/Desktop/CMEdata/daily-standings-2019-10-14.csv')
day_7 = Table.read_table('C:/Users/dusti/OneDrive/Desktop/CMEdata/daily-standings-2019-10-15.csv')
day_8 = Table.read_table('C:/Users/dusti/OneDrive/Desktop/CMEdata/daily-standings-2019-10-16.csv')
day_9 = Table.read_table('C:/Users/dusti/OneDrive/Desktop/CMEdata/daily-standings-2019-10-17.csv')
day_10 = Table.read_table('C:/Users/dusti/OneDrive/Desktop/CMEdata/daily-standings-2019-10-18.csv')
day_11 = Table.read_table('C:/Users/dusti/OneDrive/Desktop/CMEdata/daily-standings-2019-10-22.csv')
day_12 = Table.read_table('C:/Users/dusti/OneDrive/Desktop/CMEdata/daily-standings-2019-10-23.csv')
day_13 = Table.read_table('C:/Users/dusti/OneDrive/Desktop/CMEdata/daily-standings-2019-10-24.csv')
day_14 = Table.read_table('C:/Users/dusti/OneDrive/Desktop/CMEdata/daily-standings-2019-10-25.csv')
day_17 = Table.read_table('C:/Users/dusti/OneDrive/Desktop/CMEdata/daily-standings-2019-10-31.csv')


# In[3]:


## reads csv into list of tables
oneday = datetime.timedelta(1)
filename = 'C:/Users/dusti/OneDrive/Desktop/CMEdata/daily-standings-{}.csv'
start_date = datetime.date(2019,10,7)
tables = []
for i in np.arange(25):
    date = start_date +i*oneday
    if date.weekday() in range(5):
        myfile = filename.format(str(date))
        mytable = Table.read_table(myfile)
        tables.append(mytable)


# In[4]:


top10 = tables[-1].column("Account Name")[:10]


# In[23]:


## Scatter plot of Commissions by Final Balance
commissions_balance = day_17.scatter("Total Commissions including Volume Penalties","Final Balance") 
commissions_balance


# In[24]:


## percent return for top 10 teams final placement, change to dayi
percent = day_17.column("Final Balance") - 500000
array = percent/500000
day17withpercentarray = array*100
day17withpercent = day_17.with_column("Percent Return",day17withpercentarray).set_format("Percent Return",NumberFormatter)
day17withpercent.drop("Total Commissions including Volume Penalties","Trading End Balance").show(10)


# In[25]:


##sample day
a = day_14.column("Account Name")[:10]
b = day_14.column("Final Balance")[:10]
c = Table().with_columns("Account Name",a,"Final Balance",b)
c


# In[8]:


top10[0]


# In[9]:


tables[0].where("Account Name",are.equal_to(top10[0])).column("Final Balance")


# In[10]:


##gets balance after every day, for each particular team
def get_balance(team_name,tables):
    balarray = make_array()
    for i in range(len(tables)):
        balance = tables[i].where("Account Name",are.equal_to(team_name)).column("Final Balance")
        balarray = np.append(balarray, balance)
    return (balarray)
get_balance(top10[0],tables)


# In[21]:


final_table = Table()
for name in top10:
    balarray = get_balance(name, tables)
    final_table = final_table.with_column(name, balarray)
final_table.plot()


# In[22]:


final_table


# In[13]:


final_table.hist("University of Colorado Boulder Edge U1", unit = "Balance", bins = np.arange(0,1800000,250000))

