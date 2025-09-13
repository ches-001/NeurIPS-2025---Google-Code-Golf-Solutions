def F(d,O):
 for a,b in O:O+=[(x,y)for x,y in[(a+1,b),(a-1,b),(a,b+1),(a,b-1)]if 0<=x<10>y>=0 if d[x][y]if(x,y)not in O]
 A,B=zip(*O);return[r[min(B):max(B)+1]for r in d[min(A):max(A)+1]]
p=lambda d,R=range(10):max([F(d,[(i,j)])for i in R for j in R if d[i][j]],key=lambda w:str(w).count('2'))