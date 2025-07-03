#1. Invert a dictionary with list values (group keys by their values) 
#Input: d = {'a': 1, 'b': 2, 'c': 1, 'd': 3} 
#Output: {1: ['a', 'c'], 2: ['b'], 3: ['d']} 
#(Hint: Use setdefault method) 
d = {'a': 1, 'b': 2, 'c': 1, 'd': 3} 
res={}
for x,y in d.items():
    res.setdefault(y,[]).append(x)
print(res)
#output:
{1: ['a', 'c'], 2: ['b'], 3: ['d']}

#2. Find Max and Min Value in Dictionary 
#Input: d = {'a': 10, 'b': 5, 'c': 15} 
#Output: Max Value → 15 
#        Min Value → 5 
d={'a':10,'b':5,'c':15}
print("Max Value-->",max(d.values()))
print("Min Value-->",min(d.values()))
#output:
#Max Value--> 15
#Min Value--> 5

#3.Create a dictionary using dictionary comprehension for the given list of numbers, 
#where: 
#• Each number is a key. 
#• The value is "prime" if the number is prime. 
#• The value is "notprime" if the number is not prime. 
#Output:   {2: 'prime', 3: 'prime', 4: 'notprime', 5: 'prime', 6: 'notprime'} 
res={x:"Prime" if all (x%y!=0 for y in range(2,x)) else "Not Prime" for x in range(2,7)}
print(res)
#output:
{2: 'Prime', 3: 'Prime', 4: 'Not Prime', 5: 'Prime', 6: 'Not Prime'}

#4. Create a dictionary from a list of words, keys as words, values as word lengths, but only for words   longer than 3 characters 
#List: ["hi", "hello", "world", "is", "great"]
List= ["hi", "hello", "world", "is", "great"]
res={x:len(x) for x in List if len(x)>3}
print(res)
#output:
{'hello': 5, 'world': 5, 'great': 5}

#5. Create a dictionary with uppercase letters as keys and their ASCII values as values use dict comprehension.     
#Input: letters = ['a', 'b', 'c'] 
#Expected Output: {'A': 65, 'B': 66, 'C': 67}
letters=['a','b','c']
res={chr(ord(x)-32):ord(x)-32 for x in letters}
print(res)
#output:
{'A': 65, 'B': 66, 'C': 67}

#6. Explain about setdefault function in dictionary data type ? 
 #The setdefault() function in dictionaries is used to get the value of a specified key, and if the key does not exist, it inserts the key with a specified default value.
#Syntax:
#dict.setdefault(key, default_value)
  
#• key: The key to search for in the dictionary.
#• default_value (optional): The value to insert if the key does not exist. If not provided, defaults to None.

#Example:

#Key exists:
d = {'a': 1, 'b': 2}
result = d.setdefault('a', 100)
print(d)       
#output:
{'a': 1, 'b': 2}   
#Key doesnt exists:
d = {'a': 1, 'b': 2}
result = d.setdefault('c', 300)
print(d)    
#output:
{'a': 1, 'b': 2, 'c': 300}

#7. Difference between d[key] and d.get(key)?
#d[key]
#•  This is the normal way to get a value from a dictionary.but if the key is not there, it gives an error!
# Example 
d = {'a': 10, 'b': 20}
print(d['a'])          #10
print(d['c'])          #keyerror: 'c'

#d.get(key)
#• This is a safe way to get a value.
#• If the key is missing, it just gives None (no error).
#Example:
d = {'a': 10, 'b': 20}
print(d.get('a'))          #10
print(d.get('c'))          #None(no error)
print(d.get('c',100))      #100(custom default)

#8. What is the difference between Shallow Copy and Deep Copy in Python? Explain with examples.
#Shallow copy:It will creates a new object but copies references of nested objects.
#If the nested objects are modified,changes in both original and copied object.
#Example:
import copy
k=[[10,20,30],[40,100,150]]
res=copy.copy(k)
k[0][2]=250
print(res)
print(k)