p=lambda d,E=enumerate:next([[c*(w>0)for w in e[j+1:r.index(c,j+1)]]for e in d[i+1:C.index(c,i+1)]]for i,r in E(d)for j,C in E(zip(*d))if(c:=r[j]))
