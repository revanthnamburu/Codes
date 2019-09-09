'''
You can perform the following operations on the string,a :
Capitalize zero or more of a's lowercase letters.
Delete all of the remaining lowercase letters in a.
Given two strings, a and b,determine if it's possible to make a equal to b as described.
If so, print YES on a new line. Otherwise, print NO.
For example, given a=AbcDE and b=ABDE, in a we can convert b and delete c to match b.
If a=AbcDE and b=ABDE, matching is not possible because letters may only be capitalized or discarded, not changed.
'''

def abbreviation(a, b):
    a_len=len(a)
    b_len=len(b)
    mat=[]
    for i in range(a_len+1):
        temp=[]
        for j in range(b_len+1):
            if j==0 and i==0:
                temp.append(1)
            else:
                temp.append(0)
        mat.append(temp)
    count=0
    for i in range(1,a_len+1):
        k=i-1
        if a[k].isupper() or count:
            count=1
            mat[i][0]=0
        else:
            mat[i][0]=1
    for i in range(1,a_len+1):
        n=i-1
        for j in range(1,b_len+1):
            m=j-1
            if a[n]==b[m]:
                mat[i][j]=mat[i-1][j-1]
                continue
            else:
                if a[n].upper()==b[m]:
                    mat[i][j]=mat[i-1][j-1] or mat[i-1][j]
                    continue
                if a[n].isupper():
                    mat[i][j]=0
                    continue
                else:
                    mat[i][j]=mat[i-1][j]
                    continue
    if mat[a_len][b_len]:
        return 'YES'
    else:
        return 'NO'
i='daBcd'
j='ABC'
print(abbreviation(i,j))