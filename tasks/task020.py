def p(d):
 I,J=[*map(any,d)].index(1)%10,[*map(any,zip(*d))].index(1)%10
 for k in range(25):x,y=k//5,k%5;d[I+x][J+y]=max(d[I+a][J+b]for x,y in[(x,y),(y,x)]for a,b in[(x,y),(4-x,y),(4-x,4-y),(x,4-y)])
 return d