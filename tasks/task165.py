def p(d,E=enumerate):
    V=[c for i,r in E(d[1:-1],1)for j,c in E(r[1:-1],1)if c if all(d[a][b]==c for a,b in[(i-1,j),(i,j+1),(i,j-1)])][0];O=max({*sum(d,[])}-{V})
    return[[[c,O][c==0 and V in C[:i]and O in C[C.index(V):]]for c,C in zip(r,zip(*d))]for i,r in E(d)]