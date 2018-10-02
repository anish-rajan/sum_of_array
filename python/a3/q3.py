a=input()
c=input()
y=1
#using for loop
for i in range(c):
    y=y*a

#using while loop

i=0
y1=1
while(i<c):
    y1=y1*a
    i+=1

#using funtion

def power(a,c,i=0):
    if i<c:
        i+=1
        return a*power(a,c,i)
    else:
        return 1

print y
print y1
print power(a,c)
