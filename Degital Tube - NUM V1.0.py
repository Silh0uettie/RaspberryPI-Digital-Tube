#!/usr/bin/env python
# coding: utf-8

# In[1]:


import RPi.GPIO as GPIO
import time


# In[2]:


LED_A = 26
LED_B = 19
LED_C = 13
LED_D = 6
LED_E = 5
LED_F = 11
LED_G = 9
LED_DP = 10
DIGIT1 = 12
DIGIT2 = 16
DIGIT3 = 20
DIGIT4 = 21


# In[3]:


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# In[4]:


GPIO.setup(LED_A,GPIO.OUT)
GPIO.setup(LED_B,GPIO.OUT)
GPIO.setup(LED_C,GPIO.OUT)
GPIO.setup(LED_D,GPIO.OUT)
GPIO.setup(LED_E,GPIO.OUT)
GPIO.setup(LED_F,GPIO.OUT)
GPIO.setup(LED_G,GPIO.OUT)
GPIO.setup(LED_DP,GPIO.OUT)
GPIO.setup(DIGIT1,GPIO.OUT)
GPIO.setup(DIGIT2,GPIO.OUT)
GPIO.setup(DIGIT3,GPIO.OUT)
GPIO.setup(DIGIT4,GPIO.OUT)


# In[5]:


def ori(): #define a function to clean up
    GPIO.output(LED_A, False)
    GPIO.output(LED_B, False)
    GPIO.output(LED_C, False)
    GPIO.output(LED_D, False)
    GPIO.output(LED_E, False)
    GPIO.output(LED_F, False)
    GPIO.output(LED_G, False)
    GPIO.output(LED_DP, False)
    GPIO.output(DIGIT1, False)
    GPIO.output(DIGIT2, False)
    GPIO.output(DIGIT3, False)
    GPIO.output(DIGIT4, False)
ori()


# In[6]:


# define all the numbers
def num0():
    GPIO.output(LED_A, True)
    GPIO.output(LED_B, True)
    GPIO.output(LED_C, True)
    GPIO.output(LED_D, True)
    GPIO.output(LED_E, True)
    GPIO.output(LED_F, True)
    GPIO.output(LED_G, False)
    GPIO.output(LED_DP, False)
def num1():
    GPIO.output(LED_A, False)
    GPIO.output(LED_B, True)
    GPIO.output(LED_C, True)
    GPIO.output(LED_D, False)
    GPIO.output(LED_E, False)
    GPIO.output(LED_F, False)
    GPIO.output(LED_G, False)
    GPIO.output(LED_DP, False)
def num2():
    GPIO.output(LED_A, True)
    GPIO.output(LED_B, True)
    GPIO.output(LED_C, False)
    GPIO.output(LED_D, True)
    GPIO.output(LED_E, True)
    GPIO.output(LED_F, False)
    GPIO.output(LED_G, True)
    GPIO.output(LED_DP, False)
def num3():
    GPIO.output(LED_A, True)
    GPIO.output(LED_B, True)
    GPIO.output(LED_C, True)
    GPIO.output(LED_D, True)
    GPIO.output(LED_E, False)
    GPIO.output(LED_F, False)
    GPIO.output(LED_G, True)
    GPIO.output(LED_DP, False)
def num4():
    GPIO.output(LED_A, False)
    GPIO.output(LED_B, True)
    GPIO.output(LED_C, True)
    GPIO.output(LED_D, False)
    GPIO.output(LED_E, False)
    GPIO.output(LED_F, True)
    GPIO.output(LED_G, True)
    GPIO.output(LED_DP, False)
def num5():
    GPIO.output(LED_A, True)
    GPIO.output(LED_B, False)
    GPIO.output(LED_C, True)
    GPIO.output(LED_D, True)
    GPIO.output(LED_E, False)
    GPIO.output(LED_F, True)
    GPIO.output(LED_G, True)
    GPIO.output(LED_DP, False)
def num6():
    GPIO.output(LED_A, True)
    GPIO.output(LED_B, False)
    GPIO.output(LED_C, True)
    GPIO.output(LED_D, True)
    GPIO.output(LED_E, True)
    GPIO.output(LED_F, True)
    GPIO.output(LED_G, True)
    GPIO.output(LED_DP, False)
def num7():
    GPIO.output(LED_A, True)
    GPIO.output(LED_B, True)
    GPIO.output(LED_C, True)
    GPIO.output(LED_D, False)
    GPIO.output(LED_E, False)
    GPIO.output(LED_F, False)
    GPIO.output(LED_G, False)
    GPIO.output(LED_DP, False)
def num8():
    GPIO.output(LED_A, True)
    GPIO.output(LED_B, True)
    GPIO.output(LED_C, True)
    GPIO.output(LED_D, True)
    GPIO.output(LED_E, True)
    GPIO.output(LED_F, True)
    GPIO.output(LED_G, True)
    GPIO.output(LED_DP, False)
def num9():
    GPIO.output(LED_A, True)
    GPIO.output(LED_B, True)
    GPIO.output(LED_C, True)
    GPIO.output(LED_D, True)
    GPIO.output(LED_E, False)
    GPIO.output(LED_F, True)
    GPIO.output(LED_G, True)
    GPIO.output(LED_DP, False)
def numdp():
    GPIO.output(LED_DP, True)


# In[7]:


# define all the digit pins
def dig1():
    GPIO.output(DIGIT1, False)
    GPIO.output(DIGIT2, True)
    GPIO.output(DIGIT3, True)
    GPIO.output(DIGIT4, True)
def dig2():
    GPIO.output(DIGIT1, True)
    GPIO.output(DIGIT2, False)
    GPIO.output(DIGIT3, True)
    GPIO.output(DIGIT4, True)
def dig3():
    GPIO.output(DIGIT1, True)
    GPIO.output(DIGIT2, True)
    GPIO.output(DIGIT3, False)
    GPIO.output(DIGIT4, True)
def dig4():
    GPIO.output(DIGIT1, True)
    GPIO.output(DIGIT2, True)
    GPIO.output(DIGIT3, True)
    GPIO.output(DIGIT4, False)


# In[8]:


# define a function to show numbers
def num(a):
    if a == "0":
        num0()
    if a == "1":
        num1()
    if a == "2":
        num2()
    if a == "3":
        num3()
    if a == "4":
        num4()
    if a == "5":
        num5()
    if a == "6":
        num6()
    if a == "7":
        num7()
    if a == "8":
        num8()
    if a == "9":
        num9()
    if a == ".":
        numdp()


# In[9]:


# define a function to show 4 digits
def show4(a,b,c,d):
    t = 0.001
    print("Press Ctrl+C to input other numbers.")
    try:
        
        running = 1
        while running == 1:
            
            l = 1
            if l == 1:
                num(str(a))
                dig1()
                time.sleep(t)
                l = 2

            if l == 2:
                num(str(b))
                dig2()
                time.sleep(t)                
                l = 3

            if l == 3:
                num(str(c))
                dig3()
                time.sleep(t)
                l = 4

            if l == 4:
                num(str(d))
                dig4()
                time.sleep(t)
                l = 1
            else:
                pass

    except KeyboardInterrupt:
        ori()


# In[10]:


# define a function to show 4 digits with dp
def show3(a,b,c,d,e):
    t = 0.001
    print("Press Ctrl+C to input other numbers.")
    try:
        
        running = 1
        while running == 1:
            
            l = 1
            if l == 1:
                num(str(a))
                dig1()
                time.sleep(t)
                l = 2

            if l == 2:
                num(str(b))
                dig2()
                time.sleep(t)                
                l = 3

            if l == 3:
                num(str(c))
                dig3()
                time.sleep(t)
                l = 4

            if l == 4:
                num(str(d))
                dig3()
                time.sleep(t)
                l = 5
                
            if l == 5:
                num(str(e))
                dig4()
                time.sleep(t)
                l = 1
            else:
                pass

    except KeyboardInterrupt:
        ori()


# In[11]:


# define a function to show 4 digits with dp
def show2(a,b,c,d,e):
    t = 0.001
    print("Press Ctrl+C to input other numbers.")
    try:
        
        running = 1
        while running == 1:
            
            l = 1
            if l == 1:
                num(str(a))
                dig1()
                time.sleep(t)
                l = 2

            if l == 2:
                num(str(b))
                dig2()
                time.sleep(t)                
                l = 3

            if l == 3:
                num(str(c))
                dig2()
                time.sleep(t)
                l = 4

            if l == 4:
                num(str(d))
                dig3()
                time.sleep(t)
                l = 5
                
            if l == 5:
                num(str(e))
                dig4()
                time.sleep(t)
                l = 1
            else:
                pass

    except KeyboardInterrupt:
        ori()


# In[12]:


# define a function to show 4 digits with dp
def show1(a,b,c,d,e):
    t = 0.001
    print("Press Ctrl+C to input other numbers.")
    try:
        
        running = 1
        while running == 1:
            
            l = 1
            if l == 1:
                num(str(a))
                dig1()
                time.sleep(t)
                l = 2

            if l == 2:
                num(str(b))
                dig1()
                time.sleep(t)                
                l = 3

            if l == 3:
                num(str(c))
                dig2()
                time.sleep(t)
                l = 4

            if l == 4:
                num(str(d))
                dig3()
                time.sleep(t)
                l = 5
                
            if l == 5:
                num(str(e))
                dig4()
                time.sleep(t)
                l = 1
            else:
                pass

    except KeyboardInterrupt:
        ori()


# In[ ]:





# In[13]:


# define a fucntion to print 4 digits numbers
def printnum(n):
    if 1000<= float(n) <10000:
        x = ("%.5f" % n)
        a = str(x)[0]
        b = str(x)[1]
        c = str(x)[2]
        d = str(x)[3]
        show4(a,b,c,d)

    if 100<= float(n) <1000:
        x = ("%.5f" % n)
        a = str(x)[0]
        b = str(x)[1]
        c = str(x)[2]
        d = str(x)[3]
        e = str(x)[4]
        show3(a,b,c,d,e)
        
    if 10<= float(n) <100:
        x = ("%.5f" % n)
        a = str(x)[0]
        b = str(x)[1]
        c = str(x)[2]
        d = str(x)[3]
        e = str(x)[4]
        show2(a,b,c,d,e)
        
    if 0<= float(n) <10:
        x = ("%.5f" % n)
        a = str(x)[0]
        b = str(x)[1]
        c = str(x)[2]
        d = str(x)[3]
        e = str(x)[4]
        show1(a,b,c,d,e)
    else:
        pass


# In[14]:


################################


# In[ ]:


while True:
    try:
        while True:
            a = input("Input your 4-digit number here:")
            if 0 <= float(a) <10000:
                a = float(a)
                printnum(a)
                pass
            else:
                print("Wrong input format!")
                pass
    except:
        print("Wrong input format!")
        pass

