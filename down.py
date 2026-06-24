import os
down="https://docs.oracle.com/javase/specs/jvms/se7/html/jvms-6.html"
files="down.html"
finds="6.5.&nbsp;Instructions"
select1="Forms"
select2="Operand Stack"
print("\033c\033[47;31m\nfile: "+files)
os.system("curl "+down+" -o "+files)
f1=open(files,"r")
a=f1.read()
f1.close()
b=a.find("<body")
if b<0:
    b=a.find("<BODY")
a=a[b:]
bodys=a.split("<")
c=""
for body in bodys:
    t=body.split(">")
    if len(t)>1:
        c=c+t[1]

b=c.find(finds)
if b<0:
    print("error:")
else:
    d=len(finds)+b
    c=c[d:]
v=""
s=c.split(select2)
for m in s:
    n=m.split(select1)
    if len(n)>1:
        v=v+n[1]
t=v.split("\n")
l=""
for m in t:
    m=m.strip()
    if m!="":
        l=l+"\n"+m 
l=l.replace(" = ",",")   
l=l.replace(" (",",")
l=l.replace(")","")
f1=open(files,"w")
f1.write(l)
f1.close()
