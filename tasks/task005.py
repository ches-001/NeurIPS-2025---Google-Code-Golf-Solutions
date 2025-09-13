def p(d):
 Q=max;P=min;A=abs;N=len(d);R=range(N);m={};[[(v:=d[r][c],(exec("m[v]=[[r],[c]]")if v not in m else(m[v][0].append(r), m[v][1].append(c))))for c in R if d[r][c]]for r in R];m={k:m[k]for k in sorted(m,key=lambda k:len(m[k][0]))[-1:]};k=[*m][0];z=[*zip(*m[k])];D=lambda p,q:((p[0]-q[0])**2+(p[1]-q[1])**2)**(1/2);x=set();C=lambda g:Q(0,P(g,N-1))
 for r in R:
  for c in R:
   v=d[r][c]
   if v and v not in m:
    if r in m[k][0]: s=[j for i,j in z if i==r];e=Q(s);f=P(s);l=c-f;u=c-e;q=0;o=l if A(l)>A(u)else u
    elif c in m[k][1]: s=[i for i,j in z if j==c];e=Q(s);f=P(s);l=r-f;u=r-e;q=l if A(l)>A(u)else u;o=0
    else:s=[(i,j)for i,j in z if A(r-i)==A(c-j)];h=Q(s,key=lambda h:D(h,(r,c)));q=r-h[0];o=c-h[1]
    x.add((q,o,v))
 for i,j,v in x:
  for r,c in z:
   r+=i;c+=j
   while not (r<0 or c<0 or r>=N or c>=N):d[C(r)][C(c)]=v;r+=i;c+=j
 return d