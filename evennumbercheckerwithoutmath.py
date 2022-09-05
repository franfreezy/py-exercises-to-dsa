# this program checks if a number is even without using multiplication, modulus or division 

x= int(input('input number:'))

def is_even(x):
    y=str(x)
    ones_place= (y[-1])
    ones_digit= int(ones_place)
    
    even_no= [2, 4, 6, 8, 0]
    if ones_digit in even_no:
        print(x ,'is even')
    else :
        print(x ,'is odd')   
is_even(x)    

    