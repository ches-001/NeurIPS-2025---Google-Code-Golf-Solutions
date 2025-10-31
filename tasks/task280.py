def p(d,R=range):
 Q=R(1,len(d)-1)
 for _ in[0]*4:
  d=[*map(list,zip(*d[::-1]))]
  for i in Q:
   for j in Q:
    if(r:=d[i])[j-1:j+1]==[0,2]:
     h=r[:0 in r[j+1:]and r.index(0,j+1)or 55].count(3)
     for a in R(i-h,i+h+1):d[a][:j]=[d[a][j]]*j
 return d