def gcd(x,z):
    if(z!=0):
        return gcd(z,x%z)
    else:
        return x
x=input()
y=input()
print gcd(x,z)
