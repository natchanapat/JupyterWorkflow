#!/usr/bin/env python
# coding: utf-8

# In[2]:


from data import get_fremont_data
import pandas as pd

def test_fremont_data():
    data =get_fremont_data()
    assert all(data.columns == ['West', 'East', 'Fremont Bridge Total'])
    assert isinstance(data.index, pd.DatetimeIndex)
    assert len(np.unique(data.index.time) == 24)

