def gcd(x,z):
    if(z==0):
        return x
    else:
        return gcd(z,x%z)
x=input()
y=input()
print gcd(x,y)
