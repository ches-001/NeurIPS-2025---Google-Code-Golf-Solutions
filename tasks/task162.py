def p(d,R=range(18)):
 for i in R:
  A,B,C=d[i:i+3]
  for j in R:
   if sum(A[j:(J:=j+3)]+B[j:J]+C[j:J])<1:A[j:J]=B[j:J]=C[j:J]=[1]*3
 return d