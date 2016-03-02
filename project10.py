#basic prime checker
primes=list()
primes.append(2)
def Checker(item,list):
    for i in list:
        if item%i==0:
            return False
    else:
        return True
for i in range(2,2000000):
    if Checker(i,primes) == True:
        primes.append(i)
        print i
total=0
for i in primes:
    total +=i
print total

