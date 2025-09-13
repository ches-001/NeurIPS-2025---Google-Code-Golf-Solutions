def p(d):
 I=sum(d,[]).index(2)//len(d[0]);s=I+sum(d[I])//2;k=0
 while s>0:d[k][0:s]=[1+2*(k<I)+(k==I)]*s;s-=1;k+=1
 return d