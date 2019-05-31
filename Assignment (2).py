#!/usr/bin/env python
# coding: utf-8

# # The ABC company has hired you as an intern on the coding team that creates e-commerce applications.  
# You must write a script that asks the user for a value. The value must be used as a whole number in a calculation, even if the user enters a decimal value. 
# 
# You need to write the code to meet the requirements.

# In[2]:


items = float(input("Enter The No of Items Present in the Cart : "))
print(items)


# In[3]:


Items = int(items)
print("Thankyou For Purchasing", Items, "items From ABC")


# # You are creating a Python program that shows a congratulation message to employees on their service anniversary.
# You need to calculate the number of years of service and print a congratulatory message.

# In[4]:


first_year = int(input("Enter your first year: "))


# In[5]:


last_year = int(input("Enter your last year: "))


# In[6]:


diff = last_year - first_year
print("Congratulation on your ",diff, " years of service")


# # Write a Python program to convert temperatures  from fahrenheit to celsius, 
# #step 1: take "fahrenheit Temperature" from user in integer data type
# #step 2: apply formula that is       (  C = (5/9) * (fahrenheit_temperature - 32)  )
# #step 3: print step 2. 

# In[7]:


fah = int(input("Enter temperature in Fahrenheit: "))


# In[8]:


cel = (5/9)* (fah-32)


# In[9]:


print("Temperature in Celsius is ",cel)


# <h3>assign a vlue to grade by checking the following conditions:: </h3>
# <h3>if % is greater then and equal to 90 and less then 100 grade is A+ </h3>
# <h3>if % is greater then and equal to 80 and less then 90 grade is A </h3>
# <h3>if % is greater then and equal to 70 and less then 80 grade is B </h3>
# <h3>if % is greater then and equal to 60 and less then 70 grade is C </h3>
# <h3>if % is less than 60 grade is FAIL </h3>
# 

# In[10]:


obt_marks = int(input("Enter your obtained marks: "))
total_marks = 700


# In[11]:


per = (obt_marks/total_marks)*100


# In[12]:


if(per >=90 and per<100):
    grade = 'A+'
elif(per >=80 and per<90):
    grade = 'A'
elif(per >=70 and per<80):
    grade = 'B'
elif(per >=60 and per<70):
    grade = 'C'
else:
    grade = 'Fail'


# <h3>Print grade percentage and obtained marks</h3>

# In[13]:


print("Obtained marks = ",obt_marks,"\nPercentage = ",per,"\nGrade = ",grade)


# In[ ]:




