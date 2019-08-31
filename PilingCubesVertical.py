#You are given a horizontal numbers each representing a cube side.
#You need to pile them vertically such a way that,upper cube is <= lower cube.
#Given you can take the horizontal cube side from either left most or from right most.
#If it can be piled up vertivally retirn 'YES' or else return 'NO'

#EX:3,2,1,1,5
#you first pick 5 and then palce 3 on it.
#next 2 is place on 3 and 1 is on 2 and so on,So possibel.Return 'YES'

def Piling(n,l):
    temp=max(l)+1
    length=n//2
    if n%2==1:
        length=n//2+1
    for i in range(length):
        if max(l[i],l[n-1-i])<=temp:
            temp=min(l[i],l[n-1-i])
        else:
            return 'No'
    return 'Yes'

print(Piling(6,[3,2,1,1,2,5]))