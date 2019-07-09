#!/usr/bin/env python
# coding: utf-8

# # Markdown Basics
# ## Markdown Basics
# ### Markdown Basics
# #### Markdown Basics
# 

# ### Relational Operators
# - ==
# - !=
# - Greater(>)
# - less than(<)
# - less than or equal to(<=)
# - Gtreater than or equal to(>=)

# # #Logical Operators
# used to combine more than single condition
# and or not

# In[ ]:


i=100
a1=(i>15) and (i<75)
a2=(i<15) and (i<150)


# In[122]:


## to check a given number even or Odd
n = int(input("Enter a number")
if n%2 == 0:
    print("Even")
else:
   print("Odd")


# In[123]:


#to check a given number is perfectly multiple of 3 or not
n = int(input("Enter a number"))
if n%3 == 0 and n%5 == 0:
    print("yes")
    el
    print("no")


# In[2]:


# Find the large number from the given 3 numbers
a1 = int(input("Enter number 1"))
a2 = int(input("Enter number 2"))
a3 = int(input("Enter number 3"))

if a1>a2 and a1>a3:
    print(a1,"is the largest number")
elif a2>a1 and a2>a3:
    print(a2,"is the largest  number")
elif a3>a1 and a3>a2:
    print(a3,"is the largest number")


# In[8]:


# Check if a year is leap year or not
a = int(input("Enter a number"))
if a%4==0 and a%100!=0 & a%400==0:
    print("leap year")
else:
    print("not a leap year")


# # Iterative Statements

# In[10]:


# Need print"Gitam" for 5 times
print("Gitam")
print("Gitam")
print("Gitam")
print("Gitam")
print("Gitam")


# In[12]:


x = 0
while x < 5:
    print("Gitam")
    x = x + 1


# In[1]:


# print N natural number using while loop
n = int(input("Enter number"))
i = 1
while i <= n :
    print(i,end = " ")
    i = i+1


# In[14]:


# Read a number -- n
# Add only numbers between 1 to n
n = int(input("Enter a number"))
i = 1
sum = 0
while i <= n:
     if i % 2 == 0:
       sum = sum+i
     i = i + 1
print(sum)    


# In[16]:


# reverse of a number
n = int(input('Enter a number'))
while n != 0:
    r = n % 10
    print(r,end = " ")
    n = n //10


# # function programming
# - simple
# - Essay read
# - lengthy program divides intlo sub programs

# In[ ]:


def nameofthefunction(<parameters>)
 statements
 return


# In[31]:


def addEvenDigits(n):
    sum=0
    while n!=0:
      r=n%10
      if r%2==0:
          sum=sum+r
      n=n//10
    print(sum)
    return
addEvenDigits(1234)


# In[10]:


# read a number
# print the largest digit

def printlarge(n):
    large=0
    while n!=0:
        r=n%10
        if large<r:
            large=r
        n=n//10
    return large
printlarge(19528)


# In[1]:


# read a number Input
# Output reverse of a number

def reversenumber(n):
    rev=0
    while n!=0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
reversenumber(123)


# In[9]:


#palidrome or not

def ispalidrome(n):
    rev=0
    buffer=n
    while n!=0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if buffer == rev:
        return "yes"
    else:
        return "no"
    
print(ispalidrome(125))
print(ispalidrome(121))


# In[10]:


#Function to print N natural numbers with for loop
def printNNaturalNumbers(n):
    for x in range(1,n+1):
        print(x,end=" ")
    return
printNNaturalNumbers(10)


# In[12]:


#Function to print number between two limits
def printSeries(lb,ub):
    for x in range(lb,ub+1):
        print(x,end=" ")
    return
printSeries(11,25)


# In[13]:


#Function to print alternate numbers
def alternateNumbers(lb,ub):
    for x in range(lb,ub+1,4):
        print(x,end=" ")
    return
alternateNumbers(100,150)
    


# In[14]:


#Function to print the series in reverse
def reverserange(start,end):
    for x in range(end,start-1,-1):
        print(x,end =" ")
    return
reverserange(1,10)


# In[ ]:


#algorithm
#simple input and output
#Flowchart
#python code


# In[3]:


# Given number is Prime or not
def isPrime(n):
    flag=True
    for i in range(2,n//2+1):
        if n%i==0:
            flag=false
            return flag 
        return flag
isPrime(11)


# In[3]:


# Function to find prime numbers count from 1 to N
def PrimeCount(n):
    cnt=0
    for a in range(2,n+1):
        k=0
        for i in range(2,a//2+1):
            if a%i==0:
                k=k+1
        if(k<=0):
            cnt=cnt+1
    return cnt
PrimeCount(10)


# In[9]:


#Individual digit factorial sum is same as original number
def factorial(n):
    fact=1
    for i in range(2,n+1):
        fact*=i
    return fact
def digitFactSum(n):
    sum=0
    buffer=n
    while n!=0:
        r=n%10
        sum+=factorial(r)
        n=n//10
    if sum==buffer:
        return "Yes"
    else:
        return "No"
    return
print(digitFactSum(145))
print(digitFactSum(123))


# In[16]:


#Function to return the count of palindrome numbers
def isPalindrome(n):
    rev=0
    buffer=n
    while n!=0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==buffer:
        return True
    else:
        return False
    return
def countPalindrome(lb,ub):
    cnt=0
    while lb!=ub:
        #Implement
        if isPalindrome(lb)==True:
            cnt=cnt+1
        lb=lb+1
    return cnt
countPalindrome(1,10)


# In[26]:


# Function to generate the perfect numbers to a given number
def factorslist(n):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum=sum+i
            
    return sum
def isPerfect(n):
    if factorslist(n)==n:
        return True
    return False
def generatePerfect(lb,ub):
    for x in range(lb,ub+1):
        if isPerfect(x):
            print(x,end =" ")
    print()
    return
generatePerfect(1,10)
generatePerfect(1,1000)
            


# # Programming with strings

# In[1]:


s1 = 'python'
print(s1[0])
print(s1[1])
print(s1[5])
print(s1[len(s1)-1])


# In[2]:


s1='python'
print(s1[1:-1])
print(s1[len(s1)//2])
print(s1[-1::-1])
print(s1[::2])
print(s1[::-2])


# In[12]:


def reverseString(str):
    return str[-1::-1]
reverseString("programming")


# In[16]:


def isPalindrome(str):
    if str==str[::-1]:
        return True
    else:
        return False
    return
print(isPalindrome('python'))
print(isPalindrome('ganag'))


# In[6]:


# Function to print upper case and lower case alphabets
#ACII
#A to Z: 65-90
#a to z:97-122
#0 to 9:48 to 57
#space: 32

def printUpper(x):
    for i in range(len(x)):
        if ord(x[i]) >=65 and ord(x[i]) <=90:
            print(x[i],end=" ")
    return
printUpper("PyThon")


# In[7]:


#Function to print "python" if the count of #upper and lower case is same
#print programming if not same

def findCount(str):
    return
    cntUpper=0
    cntLower=0
    for x in range(len(str)):
        if ord(str[x]) >=65 and ord(str][x]) <=90:
            cntUpper=cntUpper+1
            elif ord(str[x]) >=97 and ord(str[x]) <=122:
                cntLowe=cntLower+1
        if cntUpper=cntLower:
            return "Samecount"
        else:
            return "Programming"
        return
print(findcount('python'))


# In[2]:


#Function to return the sum of digits of given string

def sumofDigits(str):
    sum=0
    for x in range(len(str)):
        if ord(str[x]) >=48 and ord(str[x]) <=57:
            if (ord(str[x])-48)%2 == 0:
                sum=sum+(ord(str[x])-10)
    return sum
sumofDigits('Applicat77ions89')


# In[3]:


print("Hello Gitam","Hyderabad ",end ="")
print("welcome ",end ="")
print("ECE")


# In[5]:


n1=100
a=b=c=20
a1,b1,c1=111,222,333
print(n1)
print(a,b,c)
print(a1,b1,c1)


# In[6]:


n1=1
print(n1)
print(n1, n1)
print(n1, n1, n1)


# In[7]:


a=100;
s1="python"
s2='p'
s3=19.1
print(a,s1,s2,s3)
print(type(a),type(s1),type(s2),type(s3))


# In[8]:


s1="100"
print(type(s1))
a=int(s1)
print(type(a))
f=1.5
a1=int(f)
print(type(a1))
print(a1)


# In[9]:


# length of a string
a1=1234
print(len(str(a1)))


# In[10]:


#Reading a value-input function
s1=input("enter your name")
print(s1)
print(type(s1))


# In[11]:


# want a number as input
n1= int(input("enter a number"))
print(n1,type(n1))


# # Operators
# operator is a symbols used to perform specific operations

# In[13]:


n1=1234
print(n1+10)
print(n1-10)
print(n1*10)
print(n1/10)
print(n1%10)
print(n1//10)
print(n1**10)


# In[16]:


#Precedence of the Arth operators .parenthesis .power .division .multiplication .addition .sub

x=1+2**3/4+5
print(x)


# In[1]:


# Sum of Even number Series
n=int(input("enter n "))
i=1
sum=0
while i<=n:
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)


# ### Day Objectives
# - python Data Structures
#  > Lists
#  >tuples
#  >Dictionaries
#  -Basic program sets on Data Structure
#  -Advanced Problem set
#  -Contact Application(Dictionary object)
#  
#  
#  Data Structures:
#  
#  -To store,search and sort the data

# ### Python Data Structures
# #### Lists
# - Its is of common data structures supports by Python,the list items are separated by comma Operator and enclosed on square brackets
#     -Examples:
#          - list1-[1,6,2,18,9]
#          - list2-["Gitam",10,12,15,5,"Hyderabad"]

# In[2]:


lst = [1,8,16,9,2]
print(lst)
print(lst[0])
print(lst[1])
print(lst[-1])
print(lst[-2])
print(lst[1:])
print(lst[1:4])


# In[9]:


# Update the list item values using Index
li = ["Gitam","Python",1989,2002]
print(li)
li[2] = 2019
print(li)


# In[10]:


#delete the specific item in the list
print(li)
del li[2]
print(li)


# In[14]:


# Basic list operator
lst1=[1,9,6,18,1]
print(len(lst1))
print(lst1*2)
print(len(lst1))
print(9 in lst1)
print(15 in lst1)
# Access the list items using iteration
for x in range(len(lst1)):
    print(lst1[x],end=' ')


# In[20]:


# Function of the list
lst1
print(min(lst1))
print(max(lst1))
print(sum(lst1))
print(sum(lst1)//len(lst1))
print(sum(lst1[1::2])/len(lst1[1::2]))


# In[31]:


lst1
lst1.append(24)
lst1
lst1.insert(2,56)
lst1
lst1.count(18)
lst1.index(56)
lst1.sort()
lst1
lst1.pop()
lst1
lst1.pop(1)
lst2=(123,23,45)
lst1.extend(lst2)
lst.reverse()
lst1.remove(123)
lst1


# In[30]:


li=[1,9,8,2,6,3]
print(li[-1:0:-2])


# In[33]:


# Function to find the second large item from the list
# Input :[1,19,6,2,8,18,3]
# Outputr: 18
def secondLarge(li):
    li.sort()
    return li[-2]
li=[1,19,6,2,8,18,3]
secondLarge(li)


# In[34]:


def secondLarge(li):
    li.sort()
    return li[-2]
def genericLarge(li,n):
    li.sort()
    return li[-n]
li=[1,19,6,2,8,18,3]
genericLarge(li,4)


# In[35]:


# Function to print least item from the list
def secondleast(li):
    li.sort()
    return li[1]
def genericLeast(li,n):
    li.sort()
    return li[n-1]
li=[1,19,6,2,8,18,3]
genericLeast(li,4)


# In[1]:


###Linear Search
- Linear search algorithm can be applied on duplicate and unique list
- Unique List: The all item of the list is appeared only one
-Duplicate List:The item of the list can be appeared more than once
    
    


# In[3]:


# Function to search the data in the list
# Search is found then return the index if not return
def linearSearch(li,tarItem):
    for x in range(len(li)):
        if li[x]==tarItem:
            return x
        return -1
li=[1,19,6,2,8,198,3]
linearSearch(li,225)


# In[7]:


# Function
# Input: [1,5,9,6,5,15,1,2,5]
# Output: 148

def linearSearch2(li,tarItem):
    for x in range(len(li)):
        if li[x]==tarItem:
            print(x,end=" ")
    return
li=[1,5,9,6,5,15,1,2,5]
linearSearch2(li,5)


# In[15]:


# Function
# i/p : list
("#o/p: sequence of numbers")
#test case
#[1,5,9,6,5,15,1,2,5]

def linearSearch3(li,tarItem):
    # Implement the logic
    for x in range(len(li)):
        if li[x] == tarItem:
            j=0
            while j!=x+1:
                print("!",end=" ")
                j=j+1
            print(end=" ")        
    return
li=[1,5,9,6,5,15,1,2,5]
linearSearch3(li,5)


# In[16]:


# Function
# Input
# Output: formatted
#test case:
#[12,45,9,18,15,36]--60
#a list item which is perfectly multiple of 3 and 5
def linearSearch4(li):
    sum=0
    for x in range(len(li)):
        if li[x] % 3 == 0 and li[x] % 5 == 0:
            sum +=li[x]
    return sum
li=[12,2,45,9,18,15,36]
linearSearch4(li)


# In[6]:


# Function
# Input: list
# Output: formatted
# test case :
#[1,2,3,4,5]  -- [1,3,8,15,5]
#[6,5,2,8,3] --[6,12,40,4,2]

#1.print first and last as it is because first number does not have previous and last doesnot have next number
#need to multiply the previous and next number

def linearSearch5(li):
    for x in range(len(li)):
        if x == 0 or x ==len(li) - 1:
            print(li[x],end=" ")
        else:
            print(li[x-1]*li[x+1],end=" ")
    return
li=[1,2,3,4,5]
linearSearch5(li)


# In[16]:


# Function
# Input : list
# Output : Formatted Output
# Test case
#[1,6,9,4,16,19,22] --1 9 19 22

def linearSearch6(li):
    for x in range(len(li)):
        if x==0 or x ==len(li) -1:
            print(li[x],end=" ")
        elif li[x-1]%2==0 and li[x+1]%2==0:
            print(li[x],end=" ")
    return
li=[1,6,9,4,16,19,22]
linearSearch6(li)


# In[19]:


# Function for conversion numbers from the list
# Input - number
# Output - list
#14569 - [1,4,5,6,9]
#1990 - [1,9,9,0]

def numberListConversion(n):
    li=[]
    while n!=0:
        r=n%10
        li.append(r)
        n=n//10
    li.reverse()
    return li
numberListConversion(14569)


# In[22]:


#function to count the occurence of a character im a string
# "Python Programming",p-->2
# "Python Programming",m-->2
def countCharOccurances(s,c):
    cnt=0
    for ch in s:
        if ch == c:
            cnt += 1
    return cnt
countCharOccurances("Python Programming",'m')
            


# In[23]:


# Function to convert string to list
#test case
# "1 2 3 4 5" --[1,2,3,4,5]
def stringToListConversion(s):
    li=s.split()
    numberslist=[]
    for i in li:
        numberslist.append(int(i))
    return numberslist
s= "1 2 3 4 5 6"
stringToListConversion(s)


# # Sorting Algorithms: 
# - All the sorting algorithms makes the list into ascending order
# - Bubble Sort
# - Selection Sort
# - Insertion Sort

# In[25]:


# Bubble sort
#-this algorithm compares the adj elements,if the first element is greater
#- than second element then its required to swap the elements


# In[27]:


# Function to represent the Bubble sort
def bubbleSort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    return li
li=[19,1,25,6,18,3]
bubbleSort(li)


# In[ ]:




