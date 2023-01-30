lower=int(input('Enter lower range number'))
higher=int(input('Enter highest Range Number'))
for i in range(lower,higher+1):
    if i%2!=2:
        print(i)
