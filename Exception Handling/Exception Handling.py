
# coding: utf-8

# In[4]:


'''
Q.1- Name and handle the exception occured in the following program: 
a=3

 if a<4:

    a=a/(a-3)

     print(a)

'''
a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except:
    print("Cannot divide by zero")

'''
OUTPUT:
Cannot divide by zero
'''


# In[6]:


'''

Q.2- Name and handle the exception occurred in the following program: 

l=[1,2,3]

print(l[3])

'''
#The Exception occurring in this program is "Index Error"


l=[1,2,3]
try:
    print(l[3])
except:
    print("Index out of range")
    
'''
OUTPUT:
Index out of range
'''


# In[7]:


'''
Q.3- What will be the output of the following code:
# Program to depict Raising Exception
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise  # To determine whether the exception was raised or not
'''

try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise # To determine whether the exception was raised or not
    
'''
OUTPUT:
An exception
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-7-df632ee8c4f2> in <module>()
     10 
     11 try:
---> 12     raise NameError("Hi there")  # Raise Error
     13 except NameError:
     14     print("An exception")

NameError: Hi there

'''


# In[9]:


'''
Q.4- What will be the output of the following code:
 # Function which returns a/b
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print "a/b result in 0"
    else:
        print c
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
'''

def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
AbyB(2.0,3.0)
AbyB(3.0,3.0)

'''
OUTPUT:
-5.0
a/b result in 0
'''


# In[ ]:


'''
Q.5 Write a program to show and handle following exceptions:
1. Import Error
2. Value Error
3. Index Error
'''

#Import Error

try:
    import gw_utility.Book
except:
    print("cannot import file")

#ValueError

try:
    a=int(input("Enter an integer value:"))
    print("Correct Input")
except:
    print("Exception:", TypeError)



#IndexError

l=[1,2,3]
try:
    print(l[3])
except:
    print("Index Error")

 

