l1=[1,2,3,4,5,6]
#using for loop
sum=0
for j in l1:
    sum+=j


#using while loop
j=0
sum1=0
while(j<len(l1)):
    sum1+=l1[j]
    j+=1

#using recursive function
def sum_of_list(l1):
    i=0
    if i<(len(l1)-1):
        return l1[i]+sum_of_list(l1[i+1:])
    else:
        return l1[len(l1)-1]
print sum
print sum1
print sum_of_list(l1)
