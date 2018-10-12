'''ASSESSMENT - 1

You are given a string S . Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X,c)  in the string.

input:-
  1222311
output:-
  (1, 1) (3, 2) (1, 3) (2, 1)


'''

Inp=input("Enter the input value : ")
L=''
while len(Inp)!=0:
    c=0
    for n in range(len(Inp)+1):
        if(n==len(Inp)):
            L=L+'('+str(c)+','+Inp[0]+') '
            Inp=''
            break
        if Inp[0]==Inp[c]:
            c+=1
            continue
        else:
            L=L+'('+str(c)+','+Inp[0]+') '
            Inp=Inp[c:len(Inp)]
            break
print(L)

    
