def primesieve(n):
    prime=[True for i in range(n+1)]
    currentnumber=2
    while(currentnumber*currentnumber<=n):
        if(prime[currentnumber]==True):
            for i in range(currentnumber**2,n+1,currentnumber):
                prime[i]=False
        currentnumber+=1
    prime[0]=False
    prime[1]=False
    for p in range(n+1):
        len2=len(str(p))
        if prime[p] and len2==2:
            print(p)
n=int(input(" Enter a two digit number "))
primesieve(n)