def fib(n,prev=1,count=0,next=0):
  #in fibonacci difference of terms are in ap
  if count==n:
      return next
  else:
      next=prev+next
      prev=next-prev
      print next
      count=count+1
      return fib(n,prev,count,next)
n=input("enter a number")
fib(n)
