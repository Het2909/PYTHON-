num=int(input("Enter a number: "))
is_prime=True
for i in range(2,num):
    if num%i==0:
        is_prime=False
        break
        

if is_prime:
    print(num,"is prime")
else:
    print(num,"is composite")