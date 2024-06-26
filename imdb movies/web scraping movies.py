#!/usr/bin/env python
# coding: utf-8

# # Scraping top 250 movies from IMDb Website

# **Importing the libraries**

# In[2]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time


# #### Getting the urls

# In[5]:


url = "https://www.imdb.com/chart/top/"
driver = webdriver.Chrome()
driver.get(url)


# **Extracting all the details like rank, movie name, release year, ratings and reveiws**

# In[47]:


n = driver.find_elements(By.XPATH, '//li[@class = "ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent"]')

rank_ = []
name = []
year = []
ratings = []
reviews = []

for i in n:
    line = i.text.split("\n\n")
    
    for each in line:
        l = (each.split("\n"))
        
       
        
        
        rank_.append(l[0].split(".")[0])
        name.append(l[0].split(".")[1])
        year.append(l[1])
        ratings.append(l[4])
        reviews.append(l[5].replace("(","").replace(")",""))
        

        
        
    


# **Scraping the movie links**

# In[55]:


# link
movie_links = []
l = driver.find_elements(By.XPATH,'//a[@class = "ipc-lockup-overlay ipc-focusable"]')[0:250]
for i in l:
    movie_links.append(i.get_attribute("href"))




# **Storing all the details inside the dataframe**

# In[66]:


import pandas as pd
df = pd.DataFrame({"RANK":rank_, "MOVIE_NAME":name, "YEAR":year, "RATINGS":ratings,
                   "REVIEWS":reviews, "MOVIE_LINKS":movie_links})


# In[67]:


df


# **Exporting the data into a csv file**

# In[68]:


df.to_csv(r"C:\Users\CW\OneDrive\Desktop\MASAI\ASSIGNMENT\python\web scraping\imdb_moviesdata.csv")


# In[ ]:




