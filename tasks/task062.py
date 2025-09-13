def p(d,w=0,N=10,R=range(10)):
 if V:=[i for i in R if {*d[i]}=={0,2}]:
  a=V[0];W=[[0]*N]
  if any(d[a-1]):d=d[:a]+ d[:a][::-1];P=len(d)-N;d=d[:N];d=d+W*(abs(min(0,P)))
  elif any(d[a+1]):d=d[a+1:][::-1]+ d[a+1:];P=len(d)-N;d=d[max(0,P):];d=W*abs(min(0,P))+d
 d=[*map(list,zip(*d))];return[[c or 3 for c in r]for r in d]if w else p(d,w+1)