def p(d):
 x=max(h:=len(d),w:=len(d[0]))
 if w>h:d=[*zip(*d)]
 A=[(c:=[*map(list,d[i*3:i*3+3])],sum(map(bool,sum(c,[]))))for i in range(x//3)];d=min(A,key=lambda s:[*zip(*A)][1].count(s[1]))[0];return[d,[*zip(*d)]][w>h]