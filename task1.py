#1.Create a dictionary from two lists:
#a.	keys = ['id', 'name', 'age']
#b.	values = [101, 'John', 25]
keys=['id','name','age']
values=[101,'John',25]
res=dict(zip(keys,values))
print(res)
#output:
{'id': 101, 'name': 'John', 'age': 25}

#2.Create a dictionary to store student name and age.
res=[{'Name':'sai','Age':21},{'Name':'pooji','Age':22}]
print(res)
#output:
[{'Name': 'sai', 'Age': 21}, {'Name': 'pooji', 'Age': 22}]

#3.Create an empty dictionary and add key-value pairs one by one.
v={}
v['name']=input("enter your name:")
v['age']=int(input("enter your age:"))
v['city']=input("enter your city:")
v['pin']=int(input('enter your pin:'))
print(v)
#output:
#enter your name:saikeerthi
#enter your age:21
#enter your city:Hyderabad
#enter your pin:24
{'name': 'saikeerthi', 'age': 21, 'city': 'Hyderabad', 'pin': 24}

#4.Get the value of key "salary" from this dictionary:
#EX: employee = {'name': 'John', 'age': 30, 'salary': 50000}
employee={'name':'John','age':30,'salary':50000}
print(employee['salary'])

#output:
50000

#5.Remove the last inserted key-value pair from the dictionary using an appropriate method
res={'name':'sai','age':21,'city':'hyderabad','pin':24}
res.popitem()
print(res)

#output:
{'name': 'sai', 'age': 21, 'city': 'hyderabad'}

#6.	Define packing and unpacking in Python. Also, provide one example for both packing and unpacking.
#PACKING:Packing means putting multiple variable values into a single variable (list,tuple or set).
#Example:
k="Saikeerthi",24,"Hyderabad"
print(k)
#output:
('Saikeerthi', 24, 'Hyderabad')
#UNPACKING:Unpacking means extracting those individual values back from that packed variable.
#Example:
k=("Saikeerthi",24,"Hyderabad")
a,b,c=k
print(a)
print(b)
print(c)