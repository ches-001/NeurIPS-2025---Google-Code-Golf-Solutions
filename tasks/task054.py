def p(b,h=range):
	H=b[0][0];E,K=set(),[]
	for A in h(30):
		for B in h(30):
			if b[A][B]!=H and(A,B)not in E:
				C,J=[],[(A,B)];E.add((A,B))
				while J:
					D,I=J.pop(0);C.append((D,I))
					for F in[-1,0,1]:
						for G in[-1,0,1]:
							if F or G:
								A,B=D+F,I+G
								if 0<=A<30 and 0<=B<30 and b[A][B]!=H and(A,B)not in E:E.add((A,B));J.append((A,B))
				K.append(C)
	E=min((A for A in K if len(A)>1),key=len);A,B=zip(*E);D,I=(min(A)+max(A))//2,(min(B)+max(B))//2;L={(A-D,B-I):b[A][B]for(A,B)in E}
	for(A,B)in[(A,B)for C in h(900)if b[(A:=C//30)][(B:=C%30)]==b[D][I]]:
		for((F,G),M)in L.items():
			if(F*2,G*2)in L:
				for C in h(1,17):
					if b[(D:=A+F*C)][(C:=B+G*C)]==H:break
					b[D][C]=M
			elif b[(D:=A+F)][(C:=B+G)]!=H:b[D][C]=M
	for(D,C)in E:b[D][C]=H
	return b