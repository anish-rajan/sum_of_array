def fibonacci(n):
  #in fibonacci difference of terms are in ap
  if n==1:
    return 1
  if n ==2:
    return 2
  else:
    return fibonacci(n-1)+fibonacci(n-2)
    
     
n=input("enter a number")
fibonacci(n)
