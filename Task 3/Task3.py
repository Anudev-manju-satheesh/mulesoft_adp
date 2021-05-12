#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector as mc


# In[2]:


global db
global cursor
db = mc.connect(host = 'localhost',user='root',passwd = 'root',database = 'formula_one')
cursor = db.cursor()
def sql_cmd_show(command):
    cursor.execute(command)
    for i in cursor:
        print(i)
def sql_cmd(command):
    cursor.execute(command)


# In[3]:


sql_cmd_show('show tables')


# In[4]:


sql_cmd_show('select * from car_details')


# In[5]:


sql_cmd_show("insert into car_details(number,Name,Team) values(63,'Russel','Williams')" )


# In[6]:


sql_cmd_show('select * from car_details')


# In[7]:


sql_cmd("delete from car_details where name='Russel'")
sql_cmd_show('select * from car_details')


# In[ ]:




