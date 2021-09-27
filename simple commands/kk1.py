print("welkome")
operator = input('operator do ' )
a = float(input('a='))
b = float(input('b='))
# Змінні (додати float or int перед інпут)
if operator == '+': 
    c = (a+b)
    print('answer ' + str(c))
elif operator == '-':
    c = (a-b)
    print ('answer'   + str(c))
elif operator == '*':
    c = (a*b)
    print ('answer'   + str(c))
elif operator == '/':
    c = (a/b)
    print ('answer '   + str(c))
else:
    print(" no name ")


