#!/usr/bin/env python
# coding: utf-8

# In[4]:


# create string 
   
s="Vivek Kumar Srivastava"


# In[5]:


s


# In[9]:


#create reverse string

s="Vivek Kumar Srivastava"
k=len(s) 
l=s[k::-1]  
print (l)  


# In[ ]:





# In[10]:


# remove char from string 

def remove(s, n):
      first = s[:n] 
      last = s[n+1:]
      return first + last
print(remove('Vivek Kumar Srivastava', 0))


# In[ ]:





# In[11]:


# insert string in the middle of the string

n = input("Enter the string : ")
pos=len(n)//2
print(pos)
print(n[:pos]+' Kumar '+n[pos:])


# In[ ]:





# In[12]:


# print the input in upper case and lower case

n = input("Enter the string : ")
print(n.upper())
print(n.lower())


# In[ ]:




