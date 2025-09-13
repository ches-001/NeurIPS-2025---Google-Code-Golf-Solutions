def p(d):
 w=[r:=d[0],[*zip(*d)][0]][b:=len({*r})<2]
 for c in w:w=eval(str(w).replace(f'{c}, {c}',f'{c}'))
 return[[w],[*zip(*[w])]][b]