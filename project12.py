#function to produce the nth triangle number
def Trilate(n):
    val = (n*(n+1))/2 #more effecient formula from literature, replaced iterative calculation
    return val

#function to calculate the number of divisors for a number
def NumDivisors(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count

#function to more effeciently compute divisors
def ComputeDivisors(n):
    if n%2==0: #if input is even, divide by two two remove divisors that would be lost during calculation for triangle number 
        factors=NumDivisors(n/2)
    else:
        factors=NumDivisors(n)
    return factors


#iterate through triangle numbers until NumDivisors returns more than 500
max_div_count=0
nth_triangle=1
while max_div_count<=500:
    n_factors=ComputeDivisors(nth_triangle)
    n_plus_one_factors=ComputeDivisors(nth_triangle+1)
    attempt=n_factors*n_plus_one_factors
    if attempt>max_div_count:
        max_div_count=attempt 
        result=Trilate(nth_triangle) #save the triangle number needed to produce number of divisors
        print "New greatest number of divisors: ", attempt
    nth_triangle+=1
print "The corresponding triangle number: ", result    
