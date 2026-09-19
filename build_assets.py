from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math
ROOT=Path(__file__).resolve().parent
A=ROOT/'assets';A.mkdir(exist_ok=True)
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
mono='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
def f(n,b=False,m=False):return ImageFont.truetype(mono if m else bold if b else font,n)
BG='#0b111b';FG='#eef3fa';MINT='#79ead2';MUTED='#a4afc1';PURPLE='#b0a0f3'
points=[]
for i in range(70):
 y=1-2*(i+.5)/70;r=math.sqrt(1-y*y);a=i*math.pi*(3-math.sqrt(5));points.append((math.cos(a)*r,y,math.sin(a)*r))
edges=[(i,j) for i,p in enumerate(points) for j,q in enumerate(points) if j>i and sum((p[k]-q[k])**2 for k in range(3))<.26]
frames=[]
for frame in range(40):
 im=Image.new('RGB',(1200,360),BG);d=ImageDraw.Draw(im)
 for x in range(770,1200,28):d.line((x,0,x,360),fill='#121d2b')
 for y in range(0,360,28):d.line((770,y,1200,y),fill='#121d2b')
 d.rounded_rectangle((0,0,1199,359),radius=18,outline='#293749',width=2)
 d.rectangle((40,40,65,43),fill=MINT);d.text((80,30),'PRATIK / ENGINEERING LAB',font=f(15,m=True),fill=MINT)
 d.text((38,87),'Pratik Sharma',font=f(64,True),fill=FG)
 d.text((42,173),'AI agents. Python. Reliable backends.',font=f(25),fill=FG)
 d.text((42,227),'I build, test, break, learn — and build again.',font=f(18),fill=MUTED)
 d.line((42,284,716,284),fill='#293749')
 d.text((42,305),'CSE 2028    /    INDIA    /    OPEN TO INTERNSHIPS',font=f(13,m=True),fill=MUTED)
 a=frame/40*2*math.pi;pr=[]
 for x,y,z in points:
  xx=x*math.cos(a)+z*math.sin(a);zz=-x*math.sin(a)+z*math.cos(a)
  pr.append((970+xx*137,175+y*137,zz))
 for i,j in edges:
  p,q=pr[i],pr[j];v=(p[2]+q[2]+2)/4
  d.line((p[0],p[1],q[0],q[1]),fill=(int(30+35*v),int(65+85*v),int(72+70*v)),width=1)
 for i,(x,y,z) in sorted(enumerate(pr),key=lambda t:t[1][2]):
  r=2 if z<0 else 3;d.ellipse((x-r,y-r,x+r,y+r),fill=PURPLE if i%7==0 else MINT)
 frames.append(im)
frames[0].save(A/'banner.png')
frames[0].save(A/'banner.gif',save_all=True,append_images=frames[1:],duration=90,loop=0,optimize=True)
# Local badge strips avoid third-party image services.
def strip(name,items):
 boxes=[];x=0
 for label in items:
  width=int(f(17,m=True).getlength(label))+32;boxes.append((x,width,label));x+=width+12
 im=Image.new('RGB',(x-12,44),BG);d=ImageDraw.Draw(im)
 for pos,w,label in boxes:
  d.rounded_rectangle((pos,1,pos+w-1,42),radius=7,fill='#152130',outline='#324456');d.text((pos+16,11),label,font=f(17,m=True),fill=FG)
 im.save(A/name)
strip('languages.png',['Python','SQL','C','Java (basic)'])
strip('ai.png',['TensorFlow','scikit-learn','Transformers','LLM tool calling'])
strip('backend.png',['FastAPI','SQLite','Streamlit','REST APIs'])
strip('data.png',['Pandas','NumPy','Plotly','Matplotlib','Seaborn'])
def project(name,number,title,subtitle,stats,colour):
 im=Image.new('RGB',(1200,235),BG);d=ImageDraw.Draw(im)
 d.rounded_rectangle((1,1,1198,233),radius=14,outline='#293749',width=2)
 d.text((32,24),number,font=f(13,m=True),fill=colour)
 d.text((30,60),title,font=f(38,True),fill=FG)
 d.text((32,121),subtitle,font=f(18),fill=MUTED)
 d.line((32,163,1168,163),fill='#293749')
 d.text((32,187),stats,font=f(15,m=True),fill=colour)
 d.text((1100,55),'↗',font=f(45),fill=colour)
 im.save(A/name)
project('resolve.png','01 / CUSTOMER RESOLUTION AGENT','RESOLVE AI','Evidence first. Guarded actions. Independently verified outcomes.','27 AUTOMATED TESTS   /   5 LIVE SCENARIOS   /   SIMULATED TRANSACTIONS',MINT)
project('mortal-fi.png','02 / FINANCIAL RECONCILIATION','MORTAL-FI','Match transactions, detect exceptions, and verify permitted resolutions.','103 SYNTHETIC TRANSACTIONS   /   23 EXCEPTIONS   /   AUDIT TRAIL',PURPLE)
print('Generated banner animation, static fallback, project cards and skill strips.')
