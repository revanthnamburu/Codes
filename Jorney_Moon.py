''''The member states of the UN are planning to send 2 people to the moon.
 They want them to be from different countries. You will be given a list of pairs of astronaut ID's.
  Each pair is made of astronauts from the same country.
  Determine how many pairs of astronauts from different countries they can choose from.'''
def journeyToMoon(n, astronaut):
    if n==1:
        return 1
    else:
        var_list=[]
        for i in range(len(astronaut)):
            var_list.extend(astronaut[i])
        var_list=list(set(var_list))
        var_list.sort()
        temp_list=[astronaut[0]]
        for i in range(0,len(astronaut)):
            for j in range(len(temp_list)):
                if (astronaut[i][0] in temp_list[j]) or (astronaut[i][1] in temp_list[j]):
                    temp_list[j].extend(astronaut[i])
                    temp_list[j]=list(set(temp_list[j]))
                    break
                else:
                    temp_list.append([astronaut[i][0],astronaut[i][1]])
                    break
        for each in range(n):
            if each not in var_list:
                temp_list.append([each])
        count,result=0,0
        for item in range(len(temp_list)):
            count+=len(temp_list[item])
        for i in range(len(temp_list)):
            for j in range(len(temp_list)):
                if j<=i:
                    continue
                result+=len(temp_list[i])*len(temp_list[j])
        print(temp_list)
        print(result)
n=5
ast=[[0,1],[2,3],[0,4]]
journeyToMoon(n,ast)