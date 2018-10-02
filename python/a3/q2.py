l=[1,2,3,4,5]
#using for loop
sum=0
for i in l:
    sum=sum+i


#using while loop
i=0
sum1=0
while(i<len(l)):
    sum1+=l[i]
    i+=1

#using recursive function
def sum_of_list(l):
    i=0
    if i<(len(l)-1):
        return l[i]+sum_of_list(l[i+1:])
    else:
        return l[len(l)-1]
print sum
print sum1
print sum_of_list(l)
