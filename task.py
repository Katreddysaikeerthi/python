#1.From the list nums = [10, 25, 30, 45, 50, 60], create a set of numbers where the number is divisible by 5 but not divisible by 10 using set                 comprehension.
nums=[10,25,30,45,50,60]
res={x for x in nums if x%5==0 and x%10!=0}
print(res)

#output:
# {25, 45}

#2.Write a program to sum the digits of all numbers in a list.
#    Example: [12, 34, 5] ➞ 1+2 + 3+4 + 5 = 15
a={12,34,5}
h=0
for num in a:
    for i in str(num):
        h+=int(i)
print(h)

#output:
# 15

#3.Create a new list by repeating elements of a list n times.
#   Example: [1, 2, 3], n = 2 ➞ [1, 2, 3, 1, 2, 3]
a=[1,2,3]
n=2
res=a*n
print(res)

#output:
#  [1, 2, 3, 1, 2, 3]

#4.Write a function to count frequency of each element in a list (return as dictionary).
def fun(a):
    res={}
    for i in a:
        if i in res:
            res[i]+=1
        else:
            res[i]=1
    return res
print(fun([1,2,5,9,25,32,2,3,3,3,5,9]))

#output:
#  {1: 1, 2: 2, 5: 2, 9: 2, 25: 1, 32: 1, 3: 3}

#5.Write a function to count how many prime numbers exist in a given range.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def count_primes(start, end):
    return sum(1 for i in range(start, end + 1) if is_prime(i))

print(count_primes(1, 10)) 

#output:
#   4

#6.Write a function to calculate the sum of digits of a number until a single-digit result is obtained.
#  Example: 9875 ➞ 9+8+7+5=29 ➞ 2+9=11 ➞ 1+1=2
def sum_to_single_digit(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

print(sum_to_single_digit(9875))