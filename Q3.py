def knight_move(x,y):
    a=[]
    moves=[(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    for move in moves:
        if 0 <= x + move[0] < m and 0 <= y + move[1] < n:
            a.append((x + move[0],y + move[1]))
    return a
test=[[1,1]]
m,n=4,4
for i in test:
    print(f'Valid move of knight in matrix A {m}x{n}: {knight_move(i[0],i[1])}')
