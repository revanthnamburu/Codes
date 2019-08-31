#Given a number and number of changes you can make the number to change it to a palindrom.
#Using those you need to return the largestPalindome.
#If not possible you need to return  -1

def LargestPalindrome(s,n,num):
    inp=num
    wr,i=0,0
    flag=0
    while(i<s//2):
        if inp[i]!=inp[s-1-i] and flag!=1:
            wr+=1
        i+=1
    rev=inp[::-1]
    if rev!=inp:
        i=0
        if wr<n:
            for i in range(s//2):
                if inp[i]!=inp[s-1-i] and i!=0 and n>1:
                    f=inp[0:i]
                    mi=inp[i+1:s-i-1]
                    l=inp[s-i:s]
                    inp=f+"9"+mi+"9"+l
                    n-=2
                else:
                    if i==0 and inp[i]!=inp[s-i-1] and n>1:
                        mi=inp[i+1:s-i-1]
                        inp="9"+mi+"9"
                        n-=2
                i+=1
        for i,each in enumerate(inp):
            if inp[i]!=inp[s-i-1] and n>0:
                if int(inp[i])>int(inp[s-i-1]):
                    f=inp[0:s-i-1]
                    l=inp[s-i:]
                    inp=f+inp[i]+l
                    n-=1
                else:
                    f=inp[0:i]
                    l=inp[i+1:]
                    inp=f+inp[s-i-1]+l
                    n-=1
    else:
        for i in range(s//2):
            if i==0 and inp[i]!="9" and n>1:
                mi=inp[1:s-1]
                inp="9"+mi+"9"
                n-=2
            elif inp[i]!="9" and n>1:
                f=inp[0:i]
                mi=inp[i+1:s-i-1]
                l=inp[s-i:]
                inp=f+"9"+mi+"9"+l
                n-=2
    rev=inp[::-1]
    if inp==rev:
        return inp
    else:
        return "-1"

#i="1111"
#n=6
print(LargestPalindrome(5,3,"12399"))