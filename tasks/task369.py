def F(d,O):
 for a,b in O:O+=[(x,y)for x,y in[(a+1,b),(a-1,b),(a,b+1),(a,b-1)]if 0<=x<10>y>=0 if d[x][y]==0 if(x,y)not in O]
 return 4-len(O)
p=lambda d,R=range(10):[[[c:=d[i][j],F(d,[(i,j)])][c==0]for j in R]for i in R]