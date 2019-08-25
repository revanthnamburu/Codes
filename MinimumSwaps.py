'''You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n]without any duplicates.
You are allowed to swap any two elements.
You need to find the minimum number of swaps required to sort the array in ascending order.

For example, given the array arr=[1,3,5,2,4,6,7] we perform 3 swaps:'''
def minimumSwaps(arr):
    var=arr[0]
    i=0
    result=0
    while(i<=len(arr)-2):
        if arr[i]==i+1: #ignoring if the position is correct
            i+=1
        else:           #else we do swapping and continue
            temp=arr[i]
            arr[i]=arr[temp-1]
            arr[temp-1]=temp
            result+=1
    print(result)
    return arr



inp=[1,3,5,2,4,6,7]
print(minimumSwaps(inp))