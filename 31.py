a=int(input("國文:"))
b=int(input("英文:"))
c=int(input("微積分:"))
d=int(input("體育:"))
e=int(input("程式設計:"))
f=list()
f1=f.append(a)
f2=f.append(b)
f3=f.append(c)
f4=f.append(d)
f5=f.append(e)
g=sum(f)/5
g=float(g)
print("平均分數:%.2f" %(g))
m=max(f)
s=min(f)
print("最高分科目:"+str(m)+"分")
print("最低分科目:"+str(s)+"分")