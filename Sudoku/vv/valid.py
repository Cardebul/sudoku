def ff(q):
    for i in range(9):
        w=[]
        for j in range(9):
            if q[i][j] in w and q[i][j]!=0:
                return False
            w.append(q[i][j])
    for i in range(9):
        w=[]
        for j in range(9):
            if q[j][i] in w and q[j][i]!=0:
                return False
            w.append(q[i][j])
    for i in range(3,10,3):
        for j in range(3,10,3):
            w=[]
            for x in range(i-3,i):
                for y in range(j-3,j):
                    if q[x][y] in w and q[x][y]!=0:
                        return False
                    w.append(q[x][y])
    return True

    
            