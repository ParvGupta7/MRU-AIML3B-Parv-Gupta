#Fibonacci
def fibonacci(n):
    fib_sequence = []
    a=0
    b=1
    for i in range(n):
        fib_sequence.append(a)
        a=b
        b=a+b
    return fib_sequence

# Factorial
def Factorial(n):
    fact =1
    for i in range(1,n+1):
        fact = fact*i
    return fact

# Sum of Digits
def sum_of_digits(n):
    s = str(n)
    x = 0
    for i in range(len(s)):
        x = x + int(s[i])
    return x

# Check Prime 
def is_prime(n):
    isprime = True
    for i in range(2,n-1):
        if n%i==0:
            isprime = False
            break

        elif (n%i!=0 and i==(n-1)):
            isprime = True
    return isprime

# Reverse a String
def reverse_string(s):
    rev = ''
    for i in range(len(s)-1,-1,-1):
        rev = rev + s[i]
    return rev

# Check Palindrome
def check_palindrome(n):
    temp = n
    sum=0
    is_palindrome = False
    while n!=0:
        rem = n%10
        sum = (sum*10)+rem
        n = n//10
    if temp == sum:
        is_palindrome = True
    return is_palindrome

# Product Table
def print_table(n):
    l=[]
    for i in range(1,11):
        print(n,"x",i,"=",n*i)

#Largest Number in List
def Find_largest(l):
    max = l[0]
    for i in range(len(l)):
        if l[i] >= max:
            max = l[i]
    return max


# Star pattern
def star_pattern(n):
    for i in range(1, n + 1):
        print('*' * i)

# Odd and Even
def odd_even(l):
    odd = []
    even = []
    for i in l:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd

# Count vowels and consonants
def count_vowel(s):
    vowels = 'aeiou'
    vowel_count = 0
    consonant_count=0
    
    for i in s:
        if i in vowels:
            vowel_count +=1
        else:
            consonant_count+=1
    d = {'vowels':vowel_count,'consonants':consonant_count}
    return d

#Number pattern
def number_pattern(n):
    num='1'
    number = int(num)
    for i in range(1,n+1):
        print(num*i)
        number += 1
        num = str(number)
        
#Multiples of a Number
def multiples(num,limit):
    for i in range(num,limit,num):
        print(i)

#Sum of Even and Odd
def sum_even_odd(l):
    even_sum = 0
    odd_sum = 0
    for i in l:
        if i%2==0:
            even_sum+=i
        else:
            odd_sum+=i
    return (even_sum,odd_sum)



        
    



    




    

        









    

    
        








