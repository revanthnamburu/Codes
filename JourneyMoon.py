''''The member states of the UN are planning to send 2 people to the moon.
 They want them to be from different countries. You will be given a list of pairs of astronaut ID's.
  Each pair is made of astronauts from the same country.
  Determine how many pairs of astronauts from different countries they can choose from.'''
import math
def check_sum(arr,index,bool):
    if arr[index]:
        i=0
        loop=[arr[index][0]]
        while(i<len(loop)):
            for j in arr[loop[i]]:
                if j not in loop:
                    loop.append(j)
            bool[loop[i]]=False
            i=i+1
        return len(loop)
def journeyToMoon(n, astronaut):
    arr=[]
    num=[list() for i in range(n)]
    for i,j in astronaut:
        if i not in num[i]:num[i].append(i)
        if j not in num[i]:num[i].append(j)
        if i not in num[j]:num[j].append(i)
        if j not in num[j]:num[j].append(j)
    result=[]
    print(num)
    bool=[True]*n
    for i in range(n):
        if bool[i]:
            if num[i]:
                result.append(check_sum(num,i,bool))
    print(result)
    ans=math.factorial(n)//(math.factorial(n-2)*2)
    for i in result:
        ans-=math.factorial(i)//(math.factorial(i-2)*2)
    return ans
n=10
ast=[[0,2],[1,8],[1,4],[2,8],[2,6],[3,5],[6,9]]
journeyToMoon(n,ast)