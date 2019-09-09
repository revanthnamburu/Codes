'''Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants to track her ranking.
The game uses Dense Ranking, so its leaderboard works like this:
----The player with the highest score is ranked number 1 on the leaderboard.
----Players who have equal scores receive the same ranking number,
    and the next player(s) receive the immediately following ranking number.
For example, the four players on the leaderboard have high scores of 100,90,90, and 80.
Those players will have ranks 1,2,2 and 3 respectively.
If Alice's scores are 70,80 and 105 her rankings after each game are 4th,3rd and 1st'''

def climbingLeaderboard(s, a):
    scores=a
    scores_len=len(scores)
    board=list(reversed(sorted(set(s))))
    board_len=len(board)
    i=scores_len-1
    j=0
    result=[]
    while(i>=0):
        if j>=board_len or scores[i]>=board[j]:
            result.append(j+1)
            i-=1
        else:
            j+=1
    result.reverse()
    return result


a=[100,100,50,40,40,20,10]
b=[5,25,50,120]
print(climbingLeaderboard(a,b))
