'''
A special substring is any substring of a string which meets one of those criteria.
 Given a string, determine how many special substrings can be formed from it.

For example, given the string s=aabaa  we have the following special substrings: .
{ a , a , b , a , a , aa, aba , aa , aabaa}
'''
def SpecialString(inp):
    result,var,val=0,inp[0],0
    temp=[[var,1]]
    for i in range(1,len(inp)):     #counting a list variables continously
        if inp[i]==temp[val][0]:
            temp[val][1]+=1
        else:
            val+=1
            temp.append([inp[i],1])
                                    #here temp contains temp=[['a',2],['b',1],['a',2]]
    if len(temp)==1:                #all elements are unique
        return temp[0][1]*(temp[0][1]+1)//2
    if len(temp)==2:                #only two types of elemnts exists
        a,b=temp[0][1],temp[1][1]
        return a*(a+1)//2+b*(b+1)//2
    for i in range(len(temp)-2):
        result+=temp[i][1]*(temp[i][1]+1)//2
        if temp[i][0]==temp[i+2][0] and temp[i+1][1]==1:
            result+=min(temp[i][1],temp[i+2][1])
    a,b=temp[-1][1],temp[-2][1]
    result+=a*(a+1)//2+b*(b+1)//2
    return result
i='aabaa'
print(SpecialString(i))