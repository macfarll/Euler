def OnesDigit(n):
#take only numbers in the 1s place
    digit=n%10
    if digit == 0:
        return ''
    elif digit == 1:
        return 'One'
    elif digit == 2:
        return 'Two'
    elif digit == 3:
        return 'Three'
    elif digit == 4:
        return 'Four'
    elif digit == 5:
        return 'Five'
    elif digit == 6:
        return 'Six'
    elif digit == 7:
        return 'Seven'
    elif digit == 8:
        return 'Eight'
    elif digit == 9:
        return 'Nine'
    else:
        print 'Error in OnesDigit()'
def TensDigit(nn):
#take only numbers in the 10s place
    n=nn%100
    if n<10:
        return OnesDigit(n)
    elif n>=20 and n<30:
        return 'Twenty'+OnesDigit(n)
    elif n>=30 and n<40:
        return 'Thirty'+OnesDigit(n)
    elif n>=40 and n<50:
        return 'Forty'+OnesDigit(n)
    elif n>=50 and n<60:
        return 'Fifty'+OnesDigit(n)
    elif n>=60 and n<70:
        return 'Sixty'+OnesDigit(n)
    elif n>=70 and n<80:
        return 'Seventy'+OnesDigit(n)
    elif n>=80 and n<90:
        return 'Eighty'+OnesDigit(n)
    elif n>=90:
        return 'Ninety'+OnesDigit(n)
    elif n==10:
        return 'Ten'
    elif n==11:
        return 'Eleven'
    elif n==12:
        return 'Twelve'
    elif n==13:
        return 'Thirteen'
    elif n==18:
        return 'Eighteen'
    elif n==15:
        return 'Fifteen'
    elif n in [14,16,17,19]:
        return OnesDigit(n-10)+'teen'
    else:
        print 'Error in TensDigit()'
def HundredsDigit(nnn):
    if nnn<100:
        return TensDigit(nnn)
#hundreds prefix is the number in the 100s place... 1 in 123, 5 in 541
    hundred_prefix=(nnn-(nnn%100))/100
    hundreds_name=OnesDigit(hundred_prefix)+'Hundred'
    if nnn%100>0:
        hundreds_name+='And'+TensDigit(nnn)
    return hundreds_name
def NumberNamer(nnnn):
    if nnnn==1000:
        return 'OneThousand'
    else:
        return HundredsDigit(nnnn)

str_len=0
for i in range(1,1001):
#    use print statement to see what NumberNamer() outputs
    print i,NumberNamer(i), len(NumberNamer(i))
    str_len += len(NumberNamer(i))
print str_len

