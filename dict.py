#1. Delete a list of keys from a dictionary 
#sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"} 
# Keys to remove 
#keys = ["name", "salary"]
sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"} 
keys = ["name", "salary"]
for i in keys:
    sample_dict.pop(i)
print(sample_dict)

#output:
{'age': 25, 'city': 'New york'}

#2. Count the frequency of each character in a given string using a dictionary.
v="python programming"
res={}
for x in v:
    res[x]=v.count(x)
print(res)

#output:
{'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, ' ': 1, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1} 

#3. Swap keys and values in a dictionary. 
res={11:'a',12:'b',13:'c',14:'d'}
rev={}
for i,j in res.items():
    rev[j]=i
print(rev)

#output:
{'a': 11, 'b': 12, 'c': 13, 'd': 14}

#4. Write a program to sum all the values in a dictionary. 
v={'a':20,'b':25,'c':30,'d':35,'e':40}
sum=0
for x in v:
    sum+=v[x]
print(sum)

#output:
150

#5. Create a nested dictionary for student details (name, roll, marks). 
res={"student-1":{'name':"sai",'roll number':61,'marks':90},
     "student-2":{'name':"pooja",'roll number':62,'marks':95},
     "student-3":{'name':"bhavani",'roll number':63,'marks':97}}
print(res)

#output:
{'student-1': {'name': 'sai', 'roll number': 61, 'marks': 90}, 'student-2': {'name': 'pooja', 'roll number': 62, 'marks': 95}, 'student-3': {'name': 'bhavani', 'roll number': 63, 'marks': 97}}

#6. Convert a dictionary to a list of tuples. 
v={"a":10,"b":15,"c":20,"d":25,"e":30,"f":35}
for x in v.items():
    print(x)

#output:
('a', 10)
('b', 15)
('c', 20)
('d', 25)
('e', 30)
('f', 35)

#7. Write a program to store names as keys and their lengths as values. 
s=["Sai","Keerthi","Poojitha","Bhavani"]
res={}
for i in s:
    res[i]=len(i)
print(res)

#output:
{'Sai': 3, 'Keerthi': 7, 'Poojitha': 8, 'Bhavani': 7}

#8. Create a dictionary for numbers 1 to 5, where the value is "even" if the number is even, and "odd" if the number is odd 
#Expected Output: 
#{1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}
k={}
for x in range(1,6):
    if x%2==0:
        k[x]="even"
    else:
        k[x]="odd"
print(k)

#output:
{1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

#9. Create Reverse Word Dictionary 
#Given list of words: words = ["cat", "dog", "bat"] 
#Create a dictionary with words as keys and their reversed strings as values 
#Expected Output: 
#{'cat': 'tac', 'dog': 'god', 'bat': 'tab'}
words = ["cat", "dog", "bat"] 
v={}
for x in words:
    res=""
    for i in x:
        res=i+res
    v[x]=res 
print(v)   