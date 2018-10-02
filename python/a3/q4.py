def factorial(m):
    if m==0 or m==1: #Added 1 to the base case so that the number of times the recursion call takes places decreses by 1.
        return 1
    else:
        return m*factorial(m-1)
m=input()
print factorial(m)
