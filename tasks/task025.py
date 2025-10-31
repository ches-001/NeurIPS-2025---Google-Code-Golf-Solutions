def p(m,E=enumerate):
 e={r[0]:y for y,r in E(m)if all(r)}
 if not e:return[*zip(*p([*map(list,zip(*m))]))]
 for y,r in E(m):
  for x,v in E(r):
   m[y][x]=0
   if v in e:Y=e[v];m[Y-(y<Y)+(y>Y)][x]=v
 return m