'''
Given a set of distinct integers, print the size of a maximal subset of S
where the sum of any 2 numbers in S' is not evenly divisible by k.
For example, the array S=[19,10,12,10,24,25,22] and k=4. One of the arrays that can be created is S'=[10,12,25].
Another is S'=[19,22,24]. After testing all permutations, the maximum length solution array has 3 elements.
'''
def nonDivisibleSubset(s, k):
    result=[]
    for i in range(k):
        result.append(0)
    count=0
    pairs=[]
    for i in range(1,k//2+1):
        pairs.append([i,k-i])
    for i in s:
        result[i%k]+=1
    if result[0]>0:count=1
    for i in pairs:
        if i[0]!=i[1]:
            if result[i[0]]>result[i[1]]:
                count+=result[i[0]]
            else:count+=result[i[1]]
        else:
            count+=1
    return count
i=[1,7,2,4]
k=3
print(nonDivisibleSubset(i,k))