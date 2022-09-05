from ast import If


print('a program to check for the multiples of numbers')
m=int(input('input a number:'))
n=int(input('input a second number:'))

def multiples (m,n):
    
    
    if m % n == 0:
        return True
    else:
        return False
     

print(multiples(m,n))