import json,os
from urllib.request import*
def post(p,b):return json.load(urlopen(os.environ['MAKEFUN_ENV_URL']+p,b))
V=[0,100,320,330,500,900,0]
J=[-33,-31,-18,-14,14,18,31,33]
D=[-17,-15,15,17]
R=[-16,-1,1,16]
W=D+R
T=b"<<<<>AA2>97<<<<F>>AHAAFKUUUU<<<<#(--(2<>->AC-<CF->CF-<AC(2<<#(--27777><<7AAA7<AA7>>A7<>A7<<<2777<<<>9<<<9<<<9<<<9<<<9<<<>AAA<<<<27797<><7>>><<>>9<>>7<>>7<<<2779FKA<FF<<72222--(-((#-((#-((#-((#"
CM=[15]*128;CM[4]=12;CM[0]=13;CM[7]=14;CM[116]=3;CM[112]=7;CM[119]=11
ST=[];TT={};HI=set();ND=[0];M=1e5
K=lambda x:abs((x&7)-3)+abs((x>>4)-3)
def A(s,c):
 for t in(s-15*c,s-17*c):
  if not t&0x88 and B[t]==c:return 1
 for O,v in((J,2),(W,6)):
  for d in O:
   t=s+d
   if not t&0x88 and B[t]==v*c:return 1
 for O,vs in((D,(3,5)),(R,(4,5))):
  for d in O:
   t=s+d
   while not t&0x88:
    z=B[t]
    if z:
     if abs(z)in vs and z*c>0:return 1
     break
    t+=d
def g():
 ms=[];lr=7*(S>0)
 def ap(f,t):ms.append(f|t<<7|5*(t>>4==lr)<<14)
 for f,z in enumerate(B):
  if z*S<=0:continue
  a=abs(z)
  if a==1:
   d=16*S;t=f+d
   if not t&0x88 and not B[t]:
    ap(f,t)
    if f>>4==1+(S<0)*5 and not B[t+d]:ms.append(f|t+d<<7)
   for dd in(d-1,d+1):
    t=f+dd
    if not t&0x88 and B[t]*S<0:ap(f,t)
  elif a in(2,6):
   for d in(J,W)[a==6]:
    t=f+d
    if not t&0x88 and B[t]*S<=0:ms.append(f|t<<7)
   if a==6:
    for dt,bit in((2,1),(-2,2)):
     if C>>(S<0)*2&bit and not(B[f+dt]or B[f+dt//2]or(dt<0 and B[f-3]))and not(A(f,-S)or A(f+dt//2,-S)or A(f+dt,-S)):ms.append(f|f+dt<<7)
  else:
   for d in(D,R,W)[a-3]:
    t=f+d
    while not t&0x88:
     z=B[t]
     if z:z*S<0 and ms.append(f|t<<7);break
     ms.append(f|t<<7);t+=d
 return ms
def m(mv):
 global C,S
 f=mv&127;t=(mv>>7)&127;pr=mv>>14;z=B[f];v=B[t]
 ST.append((mv,v,C))
 B[t]=(pr or abs(z))*S;B[f]=0
 if abs(z)==1 and not v and(f-t)&7:B[t-16*S]=0
 if abs(z)==6:
  Y[S]=t
  if abs(t-f)==2:
   rf=t+1-(t<f)*3;rt=2*t-rf-(t<f)
   B[rt]=B[rf];B[rf]=0
 C&=CM[f]&CM[t];S=-S
def u():
 global C,S
 mv,v,C=ST.pop()
 f=mv&127;t=(mv>>7)&127;pr=mv>>14;S=-S;z=B[t]
 B[f]=S if pr else z;B[t]=v
 if abs(z)==1 and not v and(f-t)&7:B[t-16*S]=-S
 if abs(z)==6:
  Y[S]=f
  if abs(t-f)==2:
   rf=t+1-(t<f)*3;rt=2*t-rf-(t<f)
   B[rf]=B[rt];B[rt]=0
def e():
 s=0;q=0
 for i,z in enumerate(B):
  if z:
   a=abs(z);f=i&7;s+=(V[a]+T[(a-1)*32+(i>>4^7*(z<0))*4+min(f,7-f)]*2-120)*z//a
   q+=a==5
   if a==1 and(i-Y[z])*z in(15,16,17,31,32,33):s+=20*z
 if not q:s+=15*(K(Y[-1])-K(Y[1]))
 return s*S+10
def s(a,b,d):
 ND[0]+=1
 if ND[0]>8e4:1/0
 k=(tuple(B),S,C)if d>0 else 0;z=k and TT.get(k);ttm=z and z[3]
 if k in HI:return 0
 if z and z[0]>=d and(z[1]==0 or z[2]>=b and z[1]==1 or z[2]<=a and z[1]==-1):return z[2]
 ck=A(Y[S],-S)
 if d>0 and ck:d+=1
 bs=-M;bm=0
 if d<=0:
  if len(ST)>40:return e()
  if not ck:
   bs=e()
   if bs>=b:return b
   if bs>a:a=bs
 ms=g()
 ms.sort(key=lambda mv:V[B[(mv>>7)&127]*-S]*10+(mv>>14)*900+99999*(mv==ttm),reverse=True)
 n=0;ao=a
 for mv in ms:
  if d<=0 and not ck and not(B[(mv>>7)&127]or mv>>14):continue
  m(mv)
  if A(Y[-S],S):u();continue
  n+=1;sc=-s(-b,-a,d-1);u()
  if sc>bs:bs=sc;bm=mv
  if sc>a:a=sc
  if a>=b:break
 if not n:return-M+len(ST)if ck else 0 if d>0 else bs
 if d>0 and abs(bs)<90000:TT[k]=(d,(bs>=b)-(bs<=ao),bs,bm)
 return bs
def c(u):return ord(u[0])+16*int(u[1])-113|ord(u[2])+16*int(u[3])-113<<7|('pnbrq'.index(u[4])+1 if len(u)>4 else 0)<<14
def b(moves,legal):
 global B,S,C,Y
 B=[0]*128;S=1;C=15;Y={1:4,-1:116};HI.clear();TT.clear()
 for i,v in enumerate([4,2,3,5,6,3,2,4]):B[i]=v;B[i+112]=-v;B[i+16]=1;B[i+96]=-1
 for v in moves:m(c(v));HI.add((tuple(B),S,C))
 ST.clear()
 rms=[(w,c(w))for w in legal]
 ND[0]=0;pv=0;bu=rms[0][0]
 for d in range(12):
  try:
   a=-M;bs=-M
   rms.sort(key=lambda r:r[1]!=pv)
   for w,mv in rms:
    m(mv);sc=-s(-M,-a,d);u()
    if sc>bs:bs=sc;bu=w;pv=mv
    if sc>a:a=sc
  except:break
 return bu
while(G:=post('/game',b'{}'))['status']=='your_move':
 while G['status']=='your_move':
  L=G['legal_moves']
  try:mv=b(G['moves'],L)
  except:mv=L[0]
  G=post('/move',json.dumps({'game':G['game'],'move':mv}).encode())
