'''
A string is said to be a child of a another string if it can be formed by deleting 0
or more characters from the other string. Given two strings of equal length,
what's the longest string that can be constructed such that it is a child of both?
For example, ABCD and ABDC have two children with maximum length 3, ABC and ABD.
They can be formed by eliminating either the D or C from both strings.
Note that we will not consider ABCD as a common child because we can't rearrange characters and ABCD!=ABDC.
'''
def CommomChild(s1,s2):
    len_s1=len(s1)
    len_s2=len(s2)
    mat=[]
    for i in range(len_s1+1):
        temp=[]
        for j in range(len_s2+2):
            temp.append(0)
        mat.append(temp)
    for i in range(1,len_s1+1):
        a=i-1
        for j in range(1,len_s2+1):
            b=j-1
            if s2[b]==s1[a]:
                mat[i][j]=mat[i-1][j-1]+1
                continue
            elif s2[b]!=s1[a]:
                mat[i][j]=max(mat[i-1][j],mat[i][j-1])
                continue
    return mat[len_s1][len_s2]

i='ABABC'
j='ABC'
print(CommomChild(i,j))