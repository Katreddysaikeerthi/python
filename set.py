#1.Create a set with elements from 1 to 5. Add elements 6 and 7 to the set in one line.
s={1,2,3,4,5}
s.update({6,7})
print(s)

#output:
#     {1, 2, 3, 4, 5, 6, 7}

#2.Given two sets: Find elements that are present in A or B but not both (symmetric difference).
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
v=A.symmetric_difference(B)
print(v)

#output:
#     {1, 2, 3, 6, 7, 8}

#3.Remove an element from a set, but avoid error if element doesn't exist.
# Find maximum and minimum element from a set {5, 8, 12, 3, 15, 7}.
s={5,8,12,3,15,7}
s.discard(11)
print(s)
print("maximum",max(s))
print("minimum",min(s))

#output:
#     {3, 5, 7, 8, 12, 15}
#     maximum 15
#     minimum 3

#4.Create a set with the values: 10, 20, 30, 40. Then add the value 50 to the set.
s={10,20,30,40}
s.add(50)
print(s)

#output:
#     {40, 10, 50, 20, 30}

#5.Remove an element 30 from a set {10, 20, 30, 40, 50} using a set method.

v={10,20,30,40,50}
v.remove(30)
print(v)

#output:
#     {50, 20, 40, 10}

#6.Check whether the number 25 exists in the set {15, 20, 25, 30, 35}.
s={15,20,25,30,35}
print(25 in s)

#output:
#     True

#7.Find the union of two sets:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
s1=A.union(B)   
print(s1)

#output:
#     {1, 2, 3, 4, 5, 6}

#8.Find the intersection of two sets:
A = {10,20,30,40}
B = {30,40,50,60}
s1=A.intersection(B)
print(s1)
