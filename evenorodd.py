#prog on even or odd
#n=int(input('Enter a number'))
def check(n):
    if(n<2):
        return(n%2==0)
    return(check(n-2))
n=int(input("Enter any number"))
if(check(n)==True):
    print('Given number is Even')
else:
    print('Given number is Odd')
