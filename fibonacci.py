def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

n_terms = int(input("The nterms is : " ))

# check if the number of terms is valid
if n_terms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n_terms):
       print(fibonacci(i))
