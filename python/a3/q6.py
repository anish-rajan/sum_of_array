def fibonacci(n,prev=1,count=0,next=0):
  if count==n:
      return next
  else:
      next=prev+next
      prev=next-prev
      print next
      count=count+1
      return fibonacci(n,prev,count,next)
n=input("enter a number")
fibonacci(n)
