#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
from urllib.request import urlretrieve

import pandas as pd

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL, fore_download=False):
    """""Download and cache the fremont data
    Parameters
    --------------
    filename : string (optional)
        location to save the data
    url : string (optional)
        web location of the data
    fore_download ; bool (optional)
        if True, force redownload of data
        
    Returns
    ---------
    data : pandas.DataFrame
        The Fremont bridge data
    """""
    if fore_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv('Fremont.csv', index_col='Date', parse_dates = True)
    data.column = ['Weat', 'East']
    return data

