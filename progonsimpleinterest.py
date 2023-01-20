# Write a python program to print simple interest
# here p for principle Amount
#     T for Time
#     R for Rate of interest
P=float(input('Enter principle amount : '))
T=float(input('Enter Time value : '))
R=float(input('Rate of interest : '))

onemonthint=(P * R) /100
print('One month interest : ', onemonthint)
#si=(P * T * R) /100
si=onemonthint * T
print('Simple Interest', si)
