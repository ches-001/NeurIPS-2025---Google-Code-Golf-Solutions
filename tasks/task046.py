def p(r):
 t=[-1]+[t for(t,a)in enumerate(zip(*r))if sum(a)<1]+[len(r[0])];a=[[n[t[a]+1:t[a+1]]for n in r]for a in range(len(t)-1)if t[a]+1<t[a+1]];n=a[:1]
 for u in a[1:]:t=n[-1];t=next((a for(a,t)in enumerate(t)if t if t[-1]==5),0);r=next((a for(a,t)in enumerate(u)if t if t[0]==5),0);r=t-r;t=[[0]*len(u[0])]*3;n+=[(t+u+t)[3-r:6-r]]
 t=[next((t for a in t for t in a if t if t!=5),0)for t in a];r=[[[[t,a][t==5]for t in t]for t in t]for(t,a)in zip(n,t)];return[sum(t,[])for t in zip(*r)]