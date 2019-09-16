'''
Given an array of integers, determine whether the array can be sorted in ascending order
 using only one of the following operations one time.
1.Swap two elements.
2.Reverse one sub-segment.
Determine whether one, both or neither of the operations will complete the task.
If both work, choose swap. For instance, given an array [2,3,5,4] either swap the 4 and 5, or reverse them to sort the array.
Choose swap.
if it can be swaped print swap indexes with starting 1:
yes
swap 2 3
'''
import copy
def AlmostSorted(arr):
    if arr==sorted(arr):
        print('yes')
    else:
        f=0
        while(1):
            if arr[f]>arr[f+1]:
                break
            f+=1
        l=len(arr)-1
        while(1):
            if arr[l]<arr[l-1]:
                break
            l-=1
        dup=arr.copy()
        swap=dup[f]
        dup[f]=dup[l]
        dup[l]=swap
        #print(f,l)
        if dup==sorted(arr):
            print('yes')
            print('swap',f+1,l+1)
        else:
            dup=[]
            dup.extend(arr[0:f])
            mid=arr[f:l+1]
            dup.extend(mid[::-1])
            dup.extend(arr[l+1:])
            #print(dup)
            if dup==sorted(arr):
                print('yes')
                print('reverse',f+1,l+1)
            else:
                print('no')
i=[2,3,7,6,5,4]
AlmostSorted(i)