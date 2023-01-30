num = int(input('Enter multiplication of :'))

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
    for j in range(1,num):
        print(j, 'x', i, '=', j*i)          
