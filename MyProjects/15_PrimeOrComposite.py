A=int(input("Enter the starting range: "))
B=int(input("Enter the ending range: "))

prime=None
countPrime=0
countComposite=0
for i in range(A,B+1):
    for j in range(2,i):
        if i%j!=0:
            prime=True
        else:
            prime=False
            break
    if prime:
        print(f"{i} is Prime")
        countPrime+=1
    else:
        print(f"{i} is Composite")
        countComposite+=1

print(f"Result : {countPrime} Prime and {countComposite} Composite numbers are in the range")

