#function to divide by two, used on odd numbers
def OddLoop(n):
    return n/2

#function to multiply by three, then add one. Used on even numbers
def EvenLoop(n):
    return 3*n+1

#function to call even or odd loop as necessary
def CollatzIteration(n):
    if n%2==0:
        return OddLoop(n)
    else:
        return EvenLoop(n) 

#function to return numbers of terms in Collatz sequence
def ReturnCollatzSeq(n):
    current_term=n
    chain_length=1 #initialized at 1 because input is a term
    while current_term != 1:
        next_term=CollatzIteration(current_term)
        chain_length+=1 #add one for new term in chain
        current_term=next_term
    return chain_length

max_length=0
best_input=0
#iterate through the first 1,000,000 natural numbers
for i in range(2,1000000):
    if i%50000==0:
        print "On iteration ", i
    attempt=ReturnCollatzSeq(i)
    if attempt>max_length:
        max_length=attempt
        best_input=i
        print "Current best result is: ",attempt
print "Final maximum is: ",max_length
print "Input value: ", best_input
