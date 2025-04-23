limit =2000000
prime_sum =0
for num in range(2,limit):
    is_prime = True
if num<2:
        is_prime = False
elif num in range(2,3):
    is_prime = True
elif num % 2 == 0 or num%3==0:
    is_prime =False
else:
    i=5
while i*i<=num:
    if num % i==0 or num%(i+2)==0:
        is_prime =False 
        break
    i+=6
    if is_prime :
        prime_sum+=num
        print("sum of all primes below the million :",prime_sum)