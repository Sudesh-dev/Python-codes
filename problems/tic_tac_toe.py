# check if the game is won by Abhinav or Anjali or if it is a tie.
def ttt(b):
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2]:
            return b[i][0]
    for i in range(3):
        if b[0][i] == b[1][i] == b[2][i]:
            return b[0][i]
    if b[0][0] == b[1][1] == b[2][2]:
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0]:
        return b[0][2]
        
m=3
n=3
board=[]
for i in range(m):
    row = input().split()
    board.append(row)

winner = ttt(board)
if winner=="O":
    print("Abhinav Wins")
elif winner=="X":
    print("Anjali Wins")
else:
    print("Tie")

 