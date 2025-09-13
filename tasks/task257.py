p=lambda d,R=range(4):[[d[i][j]or d[i][5+j]or d[5+i][j]or d[5+i][5+j]for j in R]for i in R]

