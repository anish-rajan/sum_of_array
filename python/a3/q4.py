def factorial(m):
    if m==0:
        return 1
    else:
        return m*factorial(m-1)
m=input()
print factorial(m)
