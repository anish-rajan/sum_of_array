a=input()
b=input()
y=1
#using for loop
for i in range(b):
    y=y*a

#using while loop

i=0
y1=1
while(i<b):
    y1=y1*a
    i+=1

#using funtion

def power(a,b,i=0):
    if i<b:
        i+=1
        return a*power(a,b,i)
    else:
        return 1

print y
print y1
print power(a,b)
