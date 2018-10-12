'''
A valid postal code  have to fullfil both below requirements:

 must be a number in the range from 100000  to 999999  inclusive.
 must not contain more than one alternating repetitive digit pair.
Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

For example:

121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.


'''

Inp=input("Enter the Postal code : ")

if int(Inp)<100000 or int(Inp)>999999:
    print("Enter the postal code between 100000-999999")
else:
    c=0
    l=''
    for n in range(len(Inp)-2):
        if(Inp[n]==Inp[n+2]):
            c+=1
            if len(l)==0 and Inp[n] not in list(l) :
                l=l+Inp[n] 
            elif Inp[n] not in list(l):
                l=l+', '+Inp[n]
                
    if c==0:
        print("NO digit is an alternating repetitive digit")
    elif c>1:
        print(l , " are alternating repetitive digits")
    else:
        print(l , " is alternating repetitive digits")




        
        
