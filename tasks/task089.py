def p(d,R=range):
 def F(i,j,V):
  if 0<=i<13>j>=0<d[i][j]and(i,j)not in V:V+=[(i,j)];[F(i+1-a//3,j+1-a%3,V)for a in R(9)]
 U=[]
 for k in R(169):
  s=d[I:=k//13][J:=k%13];F(I,J,V:=[])
  if  s not in U and sum(sum(r[J-(J>0):J+2])for r in d[I-(I>0):I+2])>s>1<s<4:U+=[s];U+=[s];[exec('d[x+a-I][b-J+([2*J-y,y][s>2])]=d[x][y]')for k in R(169)if d[a:=k//13][b:=k%13]==s if(a,b)!=(I,J)for x,y in V]
 return d