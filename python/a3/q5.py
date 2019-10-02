#This is a recursive function that uses the property between 2 numbers to calculate GCD
def gcd(x,z):
    if(z==0):
        return x
    else:
        return gcd(z,x%z)
x=input()
y=input()
print gcd(x,y)
