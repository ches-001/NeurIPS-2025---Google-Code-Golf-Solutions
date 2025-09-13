p=lambda d,E=enumerate:[[(7+(a:=abs(d[0].index(7)-j))%2)*((s:=sum(sum(d,[]))//7-a)>0)*(i<s)for j,_ in E(r)]for i,r in E(d)]
