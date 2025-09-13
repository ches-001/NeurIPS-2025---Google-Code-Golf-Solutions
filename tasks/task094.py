def p(d,E=enumerate,w=0):
 for i,r in E(d):
  for j,_ in E(r):
   if 1<i<13 and 1<j<13 and r[j-2]==r[j+2]==d[i-2][j]==d[i+2][j]==1:d[i]=[[e,6][e==8]for e in r]
 d=[*map(list,zip(*d))];return d if w else p(d,E,w+1)