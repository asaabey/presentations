"""Generate original editable teaching diagrams and 2400 × 1350 PNG previews.
Run with Python and cairosvg installed. Dosing visual remains a review draft.
"""
from pathlib import Path
from html import escape
import json
import cairosvg
ROOT=Path(__file__).resolve().parent
N='#17324d'; T='#138b87'; A='#bc7815'; R='#bb4148'; M='#536779'
parts=[]
def text(x,y,s,size=26,color=N,anchor='start',weight=400):
 parts.append(f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(s)}</text>')
def box(x,y,w,h,fill='#edf6f5',stroke='none'):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
def line(x,y,xx,yy,color=T,arrow=True):
 parts.append(f'<path d="M{x},{y} L{xx},{yy}" stroke="{color}" stroke-width="4" fill="none"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
def card(x,y,w,h,lines,fill='#edf6f5',color=N):
 box(x,y,w,h,fill)
 for i,s in enumerate(lines):text(x+w/2,y+h/2+(i-(len(lines)-1)/2)*34+9,s,26,color,'middle',600)
def start(title,sub):
 parts.clear();text(60,76,title,42,weight=700);text(60,119,sub,23,M)
def save(name,footer):
 text(60,850,footer,18,M)
 svg='<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900"><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="3" markerHeight="3" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="context-stroke"/></marker></defs><rect width="1600" height="900" fill="white"/><g font-family="DejaVu Sans, sans-serif">'+''.join(parts)+'</g></svg>'
 (ROOT/'source'/f'{name}.svg').write_text(svg)
 cairosvg.svg2png(bytestring=svg.encode(),write_to=str(ROOT/'preview'/f'{name}.png'),output_width=2400,output_height=1350)
def kidney(x,y):
 parts.append(f'<path d="M{x+85},{y+20} C{x-25},{y-35} {x-70},{y+160} {x+40},{y+190} C{x+145},{y+205} {x+135},{y+115} {x+82},{y+110} C{x+35},{y+104} {x+36},{y+65} {x+85},{y+60} Z" fill="#d4eeeb" stroke="{T}" stroke-width="5"/>')
def dots(x,y,count):
 for i in range(count):parts.append(f'<circle cx="{x+(i%5)*27}" cy="{y+(i//5)*30}" r="8" fill="{A}"/>')
start('Three different questions for every drug','Clearance, accumulation and kidney injury describe different processes.')
for x,title in [(60,'Clearance'),(565,'Accumulation'),(1070,'Nephrotoxicity')]:
 box(x,170,470,555,'#f5f8fa');text(x+30,220,title,32,weight=700)
kidney(235,285);dots(100,320,3);line(185,360,225,360);line(325,480,325,540);text(295,580,'Urine',25)
text(90,655,'How much drug leaves',26);text(90,692,'through the kidney?',26)
box(610,300,380,160,'#fcefdc');dots(650,340,15);text(800,510,'Drug / metabolites in blood',23,anchor='middle');text(595,655,'Reduced clearance can',26);text(595,692,'increase exposure and toxicity.',26)
kidney(1235,285);line(1140,355,1210,355,R);dots(1110,350,1);text(1350,420,'!',66,R,weight=700);text(1100,655,'Does the drug cause',26);text(1100,692,'kidney tissue injury?',26)
text(800,785,'Accumulation can cause toxicity without directly damaging the kidney.',28,N,'middle',600)
save('clearance-accumulation-injury','Original schematic • Source: lesson.json, slide 2 • Not a quantitative model')
start('Lithium: water handling and chronic injury','The collecting-duct effect and chronic structural injury are distinct teaching points.')
box(60,175,490,555,'#f5f8fa');text(90,220,'Simplified nephron',29,weight=600)
parts.append(f'<circle cx="180" cy="315" r="48" fill="#d4eeeb" stroke="{T}" stroke-width="5"/><path d="M225 315 C360 240 380 390 290 400 L290 555 Q290 625 360 625 Q415 625 415 555 L415 350 L485 350 L485 660" fill="none" stroke="{T}" stroke-width="17"/>')
text(90,700,'Schematic; anatomy not to scale',21,M);line(510,440,610,440)
card(635,195,900,90,['Collecting-duct cell: lithium enters through ENaC'])
line(1085,290,1085,330)
card(635,345,900,100,['Reduced response to ADH','Less water reabsorbed'])
line(1085,450,1085,495)
card(635,510,900,85,['More urine → polyuria / nephrogenic DI'],'#fcefdc')
card(635,645,900,120,['Separate chronic effect','Tubulointerstitial injury over years to decades'],'#fbecee',R)
save('lithium-nephron','Source: Davis et al., BMC Nephrology 2018 • doi:10.1186/s12882-018-1101-4 • Original schematic')
start('Medicines that move lithium levels','Direction of possible change; arrows do not represent effect size.')
card(610,345,380,130,['Lithium','serum concentration'])
for y,label in [(195,'Thiazide diuretics'),(345,'ACE inhibitors / ARBs'),(495,'NSAIDs, including COX-2')]:
 card(60,y,450,100,[label],'#fcefdc');line(520,y+50,600,410,A);text(550,y+30,'↑',34,A)
card(1090,240,450,110,['SGLT2 inhibitors','May lower lithium'],'#edf6f5');line(1000,400,1080,300);text(1035,330,'↓',36,T)
card(1090,485,450,110,['Amlodipine','Usually minimal effect'],'#f5f8fa');line(1000,430,1080,520,M,False)
card(120,690,1360,95,['Starting, stopping or changing an interacting medicine: arrange lithium monitoring.'])
save('lithium-interactions','Sources: Medsafe, Drug Interactions with Lithium (2017); SGLT2 inhibitors and lithium (2023) • Original schematic')
start('Gabapentinoids: dose ranges fall with CrCl','REVIEW DRAFT • Existing lesson values; formulation-specific Australian PI verification pending.')
lesson=json.loads((ROOT.parents[1]/'lesson.json').read_text());rows=next(s for s in lesson['steps'] if s['id']=='gaba-dosing')['table']['rows']
text(65,200,'CrCl (mL/min)',25,weight=600)
for x,title,maxval,vals in [(350,'Pregabalin',600,[(150,600),(75,300),(25,150),(25,75)]),(960,'Gabapentin',3600,[(900,3600),(400,1400),(200,700),(100,300)])]:
 text(x,200,title,30,weight=700);text(x,235,'Total daily dose (mg/day)',22,M)
 for i,((lo,hi),row) in enumerate(zip(vals,rows)):
  y=310+i*95
  if x==350:text(65,y+8,row[0],29)
  line(x,y,x+450,y,'#dce5eb',False)
  line(x+450*lo/maxval,y,x+450*hi/maxval,y,T,False)
  for v in [lo,hi]:parts.append(f'<circle cx="{x+450*v/maxval}" cy="{y}" r="7" fill="{T}"/>')
  text(x,y+38,f'{lo}–{hi} mg/day',23)
 text(x,710,f'Independent scale: 0–{maxval} mg/day',20,M)
box(60,750,1480,66,'#fcefdc');text(85,778,'Haemodialysis supplement after each session (lesson values):',21);text(85,805,'Pregabalin 25–150 mg  •  Gabapentin 125–350 mg  •  Confirm the complete dialysis regimen.',21)
save('gabapentinoid-dosing','Source: lesson.json, slide 14 • Draft transcription, not independently verified dosing guidance')
start('Stacking QT risk in dialysis','Medicine effects and electrolyte shifts can converge on cardiac electrical risk.')
for y,labels in [(190,['Escitalopram']),(330,['Quetiapine']),(470,['Ondansetron'])]:
 card(60,y,430,95,labels);line(505,y+48,760,420)
card(60,625,620,120,['Low potassium / low magnesium','Around dialysis'],'#fcefdc');line(690,660,800,490,A)
card(800,315,670,200,['QT prolongation','Potential ventricular arrhythmia'],'#fbecee',R)
line(1135,530,1135,625,R);card(800,645,670,115,['Review ECG, electrolytes','and the medication combination'])
save('qt-stacking','Source: lesson.json, slide 17 • Qualitative schematic; no numerical risk score or diagnostic ECG')
start('Calcineurin inhibitors: one mechanism, two dangers','Tacrolimus and ciclosporin • CYP3A4 metabolism • Narrow therapeutic range')
for y,labels in [(230,[['Inhibitor','added'],['↓ metabolism'],['↑ CNI','exposure'],['Toxicity','risk']]),(470,[['Inducer','added'],['↑ metabolism'],['↓ CNI','exposure'],['Rejection','risk']])]:
 for i,ls in enumerate(labels):
  x=60+i*385;card(x,y,325,135,ls,'#fbecee' if i==3 else '#edf6f5',R if i==3 else N)
  if i<3:line(x+335,y+67,x+375,y+67)
text(70,405,'Stopping the inhibitor can lower CNI exposure.',24,A)
text(70,645,'Stopping the inducer can raise CNI exposure.',24,A)
card(60,700,1480,90,['Coordinate starting and stopping with the transplant team; agree a monitoring plan.'])
save('cni-interactions','Source: BC Transplant, Clinical Guidelines for Transplant Medications • Original mechanism schematic')
print('Created six SVGs and six PNG previews.')
