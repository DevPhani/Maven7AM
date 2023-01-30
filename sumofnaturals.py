# sum of naturals number
n=int(input('enter a value : '))
if n<0:
    print()
else:
    sum=0
    while n>=0:
        sum+=n
        n-=1
    print('the sum of given number is ', sum)