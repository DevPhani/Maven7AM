a=int(input('Enter a value :'))
b=int(input('Enter b value :'))
c=int(input('Enter c value :'))
sum =a+b+c
print("Sum of three numbers : " ,sum)
if(a>b and a>c):
      print('A is big value  ')
else: 
    if(b>a and b>c):
        print('B is big value')
    else:
         if(c>a and c>b):
            print(' C is big value')
         else:
              if(a==b==c):
                print('All are equal')