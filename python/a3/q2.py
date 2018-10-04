l1=[1,2,3,4,5]
#Sum using for loop
sum=0
for i in l1:
    sum=sum+i


#Sum using while loop
i=0
sum1=0
while(i<len(l1)):
    sum1+=l1[i]
    i+=1

#using reursion 
def sum_of_list(l1):
    i=0
    if i<(len(l1)-1):
        return l1[i]+sum_of_list(l1[i+1:])
    else:
        return l1[len(l1)-1]
print sum
print sum1
print sum_of_list(l1)
