row = int(input())
column = int(input())
moves = 8
if row in (1, 8):
    moves -= 3
    if column in (1, 8):
        moves -= 2
elif column in (1, 8):
    moves -= 3
print(moves)
