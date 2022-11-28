def prime(n):
     d=0
     for i in range(2,n):
          if n%i==0:
               d=1
               break
     if d==1:
         return "not a prime"
     else:
         return "a prime"
# comment
def factorial(n):
    d=1
    for i in range(1,n+1):
        d=d*i
    return d
     
     