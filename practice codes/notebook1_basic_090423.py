#!/usr/bin/env python
# coding: utf-8

# In[91]:


sname="manoj nigam"


# In[92]:


print(sname)


# In[93]:


fname="manoj"
lname="nigam"
print(fname+""+lname)


# In[94]:


print(fname+lname)


# In[95]:


print(fname+" "+lname)


# In[96]:


print("my name is: "+fname+" "+lname)


# In[97]:


fname="namita"


# In[98]:


print("my name is: "+fname+" "+lname)


# In[99]:


a,b,c=5,3,"manoj"


# In[100]:


print(a+b)


# In[101]:


print(type(a))


# In[102]:


print(type(c))


# In[103]:


print(isinstance(a,int))


# In[104]:


print(isinstance(c,int))


# In[105]:


d="""manoj nigam is
my name"""


# In[106]:


print(d)


# In[107]:


print(a)
print(b)


# In[108]:


e=3


# In[109]:


print(a>b)


# In[110]:


print(a==b)


# In[111]:


print(bool(e))


# In[112]:


print(a/b)


# In[113]:


print(a//b)


# In[114]:


print('a**b=',a**b)


# In[115]:


print('a>b is',a>b)


# In[116]:


print('a!=b is', a!=b)


# In[117]:


a+=5


# In[118]:


print(a)


# In[119]:


a=19


# In[120]:


print(a<20 and b<20)


# In[121]:


print(a>15 or b>15)


# In[122]:


print(a>15 or b>15) # python code to check or


# In[123]:


my_function():
    print("Hello Python")
    print("my_function()") # wrong code


# In[ ]:


def my_function():
    print("Hello Python")
    


# In[124]:


my_function()


# In[136]:


import array as arr
a=arr.array("I",(3,6,9))


# In[137]:


print(a[0])


# In[ ]:


cars=["merc","bmw","ford"]


# In[138]:


print(cars)


# In[133]:


print(cars[0])


# In[ ]:


famly=["Devansh","Mummy","Pops","Raddy"]


# In[ ]:


famly=["Devansh","Mummy","Pops","Raddy"]


# In[130]:


print(famly[2])


# In[ ]:


obj_myclass=myclass()


# In[ ]:


print(obj_myclass.x)


# In[125]:


class myclass: 
    x=10
    y=20
    def print_myclass(self):
        print(x)
        print(y)


# In[ ]:


Obj1=myclass()


# In[126]:


print(Obj1.x)


# In[127]:


obj1.print_myclass 
#throws error as print(self.x) should hv bn used


# In[ ]:


class resident: 
    name='manoj'
    age='42'
    
    def show(self):
        print('Name:', self.name, 'Age:', self.age)


# In[ ]:


class resident: 
    name='manoj'
    age='42'
    
    def show(self):
        print('Name:', self.name, 'Age:', self.age)


# In[ ]:


obj1=resident()


# In[129]:


print(obj1.name)


# In[128]:


obj1.show()


# In[ ]:


class resident: 
    name='manoj'
    age='42'
    
    def show(self):
        print('Name:', name, 'Age:', age)


# In[ ]:


obj1=resident()


# In[140]:


print(obj1.name)


# In[ ]:


class resident: 
    name='manoj'
    age='42'
    
    def show(self):
        print('Name:', self.name, 'Age:', self.age)


# In[ ]:


obj1=resident()


# In[139]:


obj1.show()


# In[ ]:


class resident: 
    
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age
    
    def show(self):
        print('Name:', self.name, 'Age:', self.age)


# In[ ]:


obj1=resident('manoj','42')


# In[ ]:


obj2=resident('namita','43')


# In[141]:


obj1.show()


# In[142]:


obj2.show()


# In[ ]:


lm1= lambda a:a+10 #lambda function


# In[143]:


print(lm1(20))


# In[ ]:


def fxn_add(a,b):
    print(a+b)


# In[144]:


fxn_add(10,20)


# In[ ]:


#lambda fxn having two arguments 
# Lambda can have any number of arguments, but only 1 expression

x=lambda a,b: a*b


# In[145]:


print(x(10,20))


# In[146]:


#importing mymodule.py python module(python source code 
#with the .py extension)
# mymodule has been converted to py, it shouldnt have errors 
# it has a funtion, myfunction() to print ..(argumetn)...is my best buddy
# it also has a class named resident having show() function
import mymodule


# In[147]:


mymodule.myfunction("Manoj")


# In[148]:


obj1 = mymodule.resident("manoj", "45")


# In[149]:


obj1.show()


# In[ ]:


# exception handling

# try block tests a block of code for errors, 
# except block lets u handle th eroor
# else block execute when no error
# finally block execute regardless of result of try and except


# In[150]:


try:
    print(name)
except:
    print("an exception occured...")
else:
    print("code has no error")
finally:
    print("final destination")


# In[151]:


try:
    name='manoj'
    print(name)
except:
    print("an exception occured...")
else:
    print("code has no error")
finally:
    print("final destination")


# In[155]:


try:
    print(xyz)
except NameError:
    print("Variable xyz is not defined")
except:
    print("something else went wrong.")
else:
    print("code has no error")
finally:
    print("final destination")


# In[160]:


try:
    xyz=10
    print(xyz/0)
except NameError:
    print("Variable xyz is not defined")
except:
    print("something else went wrong.")
else:
    print("code has no error")
finally:
    print("final destination")


# In[ ]:




