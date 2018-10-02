def gcd(x,y):
    if(y!=0):
        return gcd(y,x%y)
    else:
        return x
x=input()
y=input()
print gcd(x,y)
