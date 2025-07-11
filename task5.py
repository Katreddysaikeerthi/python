#1. Print All Duplicate Characters in a String
v="saikeerthi"
res=""
a=""
for x in v:
    if x not in a:
        a+=x
    else:
        res+=x
print(res)
#output:ei

#2. Replace Vowels with ‘*’
v="saikeerthi"
res=""
for x in v:
    if x in "AEIOUaeiou":
        res+="*"
    else:
        res+=x
print(res)
#output:s**k**rth*

#3. Convert a Snake_Case String to CamelCase.
v="python_developer"
res=""
for x in range(len(v)):
    if v[x]=="_":
        continue
    elif v[x-1]=="_":
        res+=v[x].upper()
    else:
        res+=v[x]
print(res)
#output:pythonDeveloper

#4. Use reduce() to Find Product of List Elements
from functools import reduce
l=[10,20,30,2,3,4,8,9]
result=reduce(lambda a,b:a*b ,l)
print(result)

