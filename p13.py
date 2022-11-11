x=input("Enter the string")
char=x[0]
x=x.replace(char,'$')
x=char+x[1:]
print(x)
