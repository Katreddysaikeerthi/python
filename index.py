#1. nums =[5,12,17,24,35,40,55]
 #                       create a tuple containing only numbers that are divisible by 5 using comprehension.

nums=[5,12,17,24,35,40,55]
res=tuple(x for x in nums if x%5==0)
print(res)

#  output:
#   (5,35,40,55)


# 2. Given a string:"HelloWorld" 
#                       Create a tuple of all uppercase letters present in the string using comprehension.?

str="HelloWorld"
res=tuple(x for x in str if x.isupper())
print(res)

#  output:
#    ('H', 'W')


# 3. marks = [55, 72, 48, 90, 67]
 #           Create a tuple where each element is "Pass" if marks are >= 50 else "Fail" using comprehension.?

marks=[55,72,48,90,67]
res=tuple("Pass" if x>=50 else "Fail" for x in marks)
print(res)

#  output:
#   ('Pass', 'Pass', 'Fail', 'Pass', 'Pass')


# 4. Given a sentence: "Python is powerful and easy to learn"
#            Create a tuple of words that have more than 4 characters using comprehension.

v="Python is powerful and easy to learn" .split()
res=tuple(x for x in v if len(x)>4)
print(res)

#  output:
#   ('Python', 'powerful', 'learn')


# 5. students = [("Alice", 85), ("Bob", 45), ("Charlie", 60), ("David", 30)]
#              Create a tuple containing names of students who scored 50 or more using comprehension

students=[("Alice",85),("Bob",45),("Charle",60),("David",30)]
res=tuple(students[x] for x in range(len(students)) if students[x][1]>=50)
print(res)

#  output:
#   (('Alice', 85), ('Charle', 60))        