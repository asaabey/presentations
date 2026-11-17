"""Rebuild source-linked urinary excretion charts: python with matplotlib installed."""
from pathlib import Path
import json,csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
ROOT=Path(__file__).resolve().parent
DATA=[]
def add(drug,group,lo,hi,label,url,note='',kind='point',basis='administered oral dose'):
 DATA.append(dict(drug=drug,group=group,low=lo,high=hi,label=label,source=url,note=note,kind=kind,basis=basis))
fda='https://www.accessdata.fda.gov/drugsatfda_docs/label/'
add('Desvenlafaxine','Antidepressants',45,45,'≈45%',fda+'2023/205583s014lbl.pdf','72-hour recovery')
add('Citalopram','Antidepressants',12,23,'12–23%','https://www.geneesmiddeleninformatiebank.nl/smpc/h27644_smpc_en.pdf',kind='range')
add('Escitalopram','Antidepressants',8,8,'≈8%',fda+'2024/021365s041lbl.pdf','Urinary recovery; label separately reports 7% of oral clearance as renal clearance.')
add('Venlafaxine *','Antidepressants',5,5,'≈5%',fda+'2023/020699s118lbl.pdf','Active O-desmethylvenlafaxine: additional 29% unconjugated and 26% conjugated urinary recovery. Parent percentage understates the clinical importance of renal impairment.')
add('Mirtazapine *','Antidepressants',0,5,'≤5%','https://med.nipro.co.jp/servlet/servlet.FileDownload?file=00PRB00000Xd1Kf2AJ','Manufacturer interview form, section VII-7: unchanged urinary recovery ≤5%; total urinary radioactivity about 75%. Clearance falls in renal impairment.',kind='upper')
add('Fluoxetine','Antidepressants',0,2.5,'<2.5%','https://pmc.ncbi.nlm.nih.gov/articles/PMC2014504/','Background value in original human PK study; not that study’s measured urinary endpoint.',kind='upper')
add('Paroxetine','Antidepressants',2,2,'≈2%',fda+'2024/020031s083%2C020710s051lbl.pdf','30-mg oral solution, 10-day recovery')
add('Amitriptyline','Antidepressants',2,2,'≈2%','https://www.medicines.org.uk/emc/product/10849/smpc')
add('Duloxetine *','Antidepressants',0,1,'<1%','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=b33cbab8-1962-cb66-e053-2a95a90a4ae7','Low unchanged recovery does not remove severe renal impairment restrictions.',kind='upper')
add('Bupropion *','Antidepressants',0.5,0.5,'≈0.5%',fda+'2024/020358s068lbl.pdf','Label reports unchanged excretion after discussion of urine/feces recovery; use as an upper-bound urinary approximation, since unchanged urine and feces are not separated.',kind='upper')
add('Sertraline','Antidepressants',None,None,'Not detected',fda+'2023/019839s102%2C020990s059lbl.pdf','Unchanged sertraline not detectable in urine; not asserted to be exactly zero.',kind='qualitative')
add('Paliperidone','Antipsychotics / sedatives',59,59,'≈59%',fda+'2025/021999s040s041lbl.pdf','Single 1-mg immediate-release radiolabeled oral dose; mean 59%, reported range 51–67%.')
add('Risperidone *','Antipsychotics / sedatives',4,30,'4–30%','https://pubmed.ncbi.nlm.nih.gov/7507814/','Parent recovery 4%, 11%, 30% in extensive, intermediate, poor metabolizer subjects. Active 9-hydroxyrisperidone also matters.',kind='range')
add('Olanzapine','Antipsychotics / sedatives',7,7,'≈7%',fda+'2026/21253s067lbl.pdf')
add('Zopiclone','Antipsychotics / sedatives',4,5,'≈4–5%','https://www.pharmascience.com/wp-content/uploads/2023/07/pms-ZOPICLONE-pm-en-approved-2024-04-02-280763.pdf',kind='range')
add('Haloperidol','Antipsychotics / sedatives',0,3,'<3%','https://www.medsafe.govt.nz/profs/datasheet/h/Haldolinj.pdf','Source is injection data sheet.',kind='upper',basis='administered dose; injection data sheet')
add('Quetiapine','Antipsychotics / sedatives',0,1,'<1% upper bound',fda+'2025/020639s074lbl.pdf','Label reports total unchanged excretion <1% without separating urine and feces. Urinary value can only be bounded above.',kind='upper')
add('Aripiprazole','Antipsychotics / sedatives',0,1,'<1%',fda+'2025/211448s000lbl.pdf',kind='upper')
add('Oxazepam','Antipsychotics / sedatives',0,1,'<1%','https://pubmed.ncbi.nlm.nih.gov/7307429/',kind='upper')
add('Zolpidem','Antipsychotics / sedatives',0,0.5,'≤0.5%','https://toyo-cap1.com/images/japanese/iryoukankeisyanominasamahe/zolpidemNPI/zolpidemNPI_if_202409.pdf','Manufacturer interview form: oral 2.5–10 mg; 24-hour urine collection.',kind='upper')
add('Temazepam','Antipsychotics / sedatives',0.2,0.2,'≈0.2%','https://pubmed.ncbi.nlm.nih.gov/2207300/','Two consecutive 24-hour urine collections.')
add('Diazepam','Antipsychotics / sedatives',None,None,'Negligible','https://assets.hpra.ie/products/Human/41449/Licence_PA22697-022-001_28112025162431.pdf','Label describes negligible unchanged urinary excretion; no precise percentage assigned.',kind='qualitative')
add('Lithium','Mood stabilisers / comparators',95,100,'>95%','https://www.medsafe.govt.nz/profs/Datasheet/l/LithicarbFCtab.pdf',kind='lower')
add('Pregabalin','Mood stabilisers / comparators',90,90,'≈90%','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=ebe34db4-816d-4f0a-adbb-826693662754')
add('Baclofen','Mood stabilisers / comparators',71.25,71.25,'≈71% (derived)','https://www.medicines.org.uk/emc/product/2594/smpc','75% urinary recovery within 72 h; 5% of that amount metabolites. Calculation: 75 × 0.95 = 71.25%; rounded for display.')
add('Levetiracetam','Mood stabilisers / comparators',66,66,'≈66%',fda+'2024/207958s024lbl.pdf')
add('Lamotrigine','Mood stabilisers / comparators',0,10,'<10%','https://www.medsafe.govt.nz/profs/datasheet/l/logemtab.pdf',kind='upper')
add('Carbamazepine','Mood stabilisers / comparators',2,3,'2–3%','https://www.novartis.com/ca-en/sites/novartis_ca/files/Tegretol_pm_20250520_en_v2.pdf',kind='range')
add('Valproate','Mood stabilisers / comparators',0,3,'<3%',fda+'2025/019680s056lbl.pdf',kind='upper')
add('Digoxin [IV]','Different denominator',50,70,'50–70% of IV dose',fda+'2025/021648s013lbl.pdf',kind='range',basis='intravenous dose')
add('Gabapentin','Different denominator',100,100,'≈100% of absorbed drug',fda+'2025/020235s079%2C020882s060%2C021129s059lbl.pdf','Systemically available drug is eliminated unchanged by kidneys; not 100% of the swallowed dose. Oral bioavailability is dose dependent. 100% is a route-of-elimination summary, not measured oral urinary recovery.',basis='absorbed drug; inferred route fraction')
add('Metformin','Different denominator',90,90,'≈90% of absorbed drug / 24 h',fda+'2026/021748s031lbl.pdf','Not 90% of the swallowed dose; recovery interval is first 24 h.',basis='absorbed drug, first 24 hours')
# Bupropion's label does not resolve the urinary numerator; retain in source data,
# but show no point estimate on the strict common-denominator graph.
for d in DATA:
 if d['drug']=='Bupropion *':d.update(low=None,high=None,label='≤0.5% upper bound',kind='qualitative')
(ROOT/'renal-excretion-data.json').write_text(json.dumps(DATA,indent=2,ensure_ascii=False)+'\n')
with (ROOT/'renal-excretion-data.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=DATA[0].keys());w.writeheader();w.writerows(DATA)
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none','text.color':'#17324d','axes.labelcolor':'#17324d','xtick.color':'#536779','ytick.color':'#17324d'})
colors=['#168c88','#4773a4','#8463a4']
def draw(ax,rows,color,title):
 n=len(rows);ax.set_xlim(0,105);ax.set_ylim(n-.4,-1.1)
 ax.set_title(title,loc='left',fontsize=16,fontweight='bold',pad=20)
 ax.set_yticks(range(n),[r['drug'] for r in rows],fontsize=12)
 ax.set_xticks([0,25,50,75,100],[f'{v}%' for v in [0,25,50,75,100]],fontsize=10)
 ax.grid(axis='x',color='#e1e8ed',lw=.8);ax.set_axisbelow(True)
 for sp in ax.spines.values():sp.set_visible(False)
 ax.tick_params(axis='both',length=0,pad=8)
 for y,d in enumerate(rows):
  lo,hi=d['low'],d['high'];kind=d['kind']
  if lo is None:ax.text(2,y,d['label'],va='center',fontsize=11,color='#536779');continue
  if kind=='point':ax.hlines(y,0,hi,color=color,alpha=.2,lw=7);ax.plot(hi,y,'o',color=color,ms=7)
  elif kind=='range':ax.plot([lo,hi],[y,y],color=color,lw=5,solid_capstyle='round');ax.plot([lo,hi],[y,y],'|',color=color,ms=12)
  elif kind=='upper':ax.plot([lo,hi],[y,y],color=color,lw=3);ax.plot(hi,y,'<',mfc='white',mec=color,ms=8)
  elif kind=='lower':ax.plot([lo,hi],[y,y],color=color,lw=3);ax.plot(lo,y,'>',mfc='white',mec=color,ms=8)
  ax.text(max(hi+3,5),y,d['label'],va='center',fontsize=10.5,color=color,clip_on=False)
 ax.set_xlabel('Dose excreted unchanged in urine',fontsize=11,labelpad=12)
fig=plt.figure(figsize=(23,14),facecolor='white')
fig.text(.035,.953,'How much drug leaves through the kidney unchanged?',fontsize=27,fontweight='bold')
fig.text(.035,.920,'Urinary recovery of parent drug (% of administered dose) • Reported values and bounds; mainly oral dosing',fontsize=15,color='#536779')
positions=[(.13,.34,.195,.51),(.46,.34,.195,.51),(.79,.34,.16,.51)]
for i,group in enumerate(['Antidepressants','Antipsychotics / sedatives','Mood stabilisers / comparators']):
 ax=fig.add_axes(positions[i]);draw(ax,[r for r in DATA if r['group']==group],colors[i],group)
fig.text(.035,.253,'READ THE DENOMINATOR',fontsize=12,fontweight='bold',color='#9b6415')
fig.text(.035,.218,'Gabapentin: renal elimination of essentially all absorbed drug; this is not 100% of the swallowed dose.',fontsize=13)
fig.text(.035,.188,'Metformin: ≈90% of absorbed drug recovered renally in 24 h.  Digoxin: 50–70% of an intravenous dose.',fontsize=13)
fig.text(.035,.133,'* Parent-drug percentages do not capture active-metabolite accumulation or all effects of CKD on drug exposure.',fontsize=13,fontweight='bold')
fig.text(.035,.104,'Venlafaxine and risperidone are key examples. Low unchanged excretion does not establish safety or remove dose restrictions.',fontsize=12)
fig.text(.035,.062,'Ranges/bounds are shown as reported; they are not confidence intervals. “Not detected” and “negligible” are not plotted as zero.',fontsize=11,color='#536779')
fig.text(.035,.035,'Sources: product labels and human pharmacokinetic studies • Full per-drug links and study notes: renal-excretion-sources.md • Reviewed 16 Nov 2026',fontsize=10,color='#536779')
for ext in ['svg','png','pdf']:
 dest=ROOT/('preview' if ext=='png' else 'source')/f'renal-excretion-comparison.{ext}'
 fig.savefig(dest,dpi=160,facecolor='white')
plt.close(fig)
# Readable slide exports, one group per 16:9 image.
for i,group in enumerate(['Antidepressants','Antipsychotics / sedatives','Mood stabilisers / comparators']):
 fig=plt.figure(figsize=(16,9),facecolor='white');ax=fig.add_axes([.22,.23,.64,.58]);draw(ax,[r for r in DATA if r['group']==group],colors[i],group)
 fig.text(.055,.93,'Urinary excretion of unchanged drug',fontsize=26,fontweight='bold')
 fig.text(.055,.875,'Percentage of administered dose • Parent drug only; mainly oral dosing',fontsize=15,color='#536779')
 fig.text(.055,.115,'* Active metabolites and altered exposure in CKD require separate consideration.',fontsize=13)
 fig.text(.055,.075,'Low percentages do not establish renal safety. Ranges and bounds are reported values, not confidence intervals.',fontsize=11)
 fig.text(.055,.035,'Sources and study details: renal-excretion-sources.md • Product labels / human PK studies • 16 Nov 2026',fontsize=10,color='#536779')
 stem=['renal-excretion-antidepressants','renal-excretion-antipsychotics-sedatives','renal-excretion-mood-stabilisers-comparators'][i]
 for ext in ['svg','png','pdf']:fig.savefig(ROOT/('preview' if ext=='png' else 'source')/f'{stem}.{ext}',dpi=180,facecolor='white')
 plt.close(fig)
lines=['# Urinary excretion comparison: sources and definitions','','The chart uses **percentage of administered dose recovered as unchanged parent drug in urine**, not percentage of total systemic clearance. Those metrics are not interchangeable when oral bioavailability is incomplete. It does not graph total urinary radioactivity, a dose reduction percentage, dialysis removal or kidney injury risk. This scope covers the named psychiatric agents in the lesson plus common psychiatric/neurological comparators. Transplant and cardiovascular case medicines are outside this first comparison.','','Sources are primary prescribing documents and human PK papers. Values come from different studies, collection intervals, formulations and populations and should be treated as approximate teaching comparisons, not a head-to-head experiment. An inequality is shown as an inequality, not an exact value.','','## Per-drug evidence','']
for i,d in enumerate(DATA,1):lines.extend([f"### {i}. {d['drug'].replace(' *','')}: {d['label']}",f"- Basis: {d['basis']}.",f"- [Primary source]({d['source']}).",f"- {d['note']}" if d['note'] else '- See the pharmacokinetics / excretion section.',''])
lines.extend(['## Interpretation','','Venlafaxine, risperidone and bupropion have relevant active metabolites. Mirtazapine clearance is reduced in renal impairment despite low unchanged urinary recovery. Duloxetine also has restrictions in severe renal impairment despite <1% unchanged urinary recovery. These examples prevent a low parent percentage from becoming a misleading renal safety ranking.','','Baclofen’s plotted value is explicitly calculated from its SmPC: 75% urinary recovery × 95% unchanged = 71.25%, displayed as about 71%. Quetiapine’s <1% is an upper bound because its label does not allocate total unchanged excretion between urine and feces. Bupropion’s unchanged excretion is likewise not resolved by route in the cited label and is shown as text only. Diazepam is described qualitatively in its source.','','Gabapentin, metformin and digoxin have different denominators and are described separately on the overview rather than merged into its bars. Their values and denominator notes remain in the JSON/CSV.','','The SVGs preserve editable text; PNGs are high-resolution previews; PDFs provide vector exports. Rebuild with `python3 assets/visuals/build_renal_excretion.py` in an environment containing matplotlib.'])
(ROOT/'renal-excretion-sources.md').write_text('\n'.join(lines)+'\n')
print(f'Created comparison overview and three slide charts; {len(DATA)} source records.')
# Separate panels retain the differing denominators for these key comparators.
fig=plt.figure(figsize=(16,9),facecolor='white')
fig.text(.055,.93,'Renal elimination: three useful comparators',fontsize=26,fontweight='bold')
fig.text(.055,.87,'Each panel states its denominator; these are not percentages of a common oral dose.',fontsize=14,color='#536779')
for i,(drug,heading,detail) in enumerate([
 ('Gabapentin','Systemically available drug','Essentially all eliminated unchanged by the kidney; route summary, not an oral recovery measurement.'),
 ('Metformin','Absorbed drug, first 24 hours','About 90% recovered via the renal route in 24 hours; unchanged drug.'),
 ('Digoxin [IV]','Intravenous dose','50–70% recovered unchanged in urine after an IV dose in healthy volunteers.')]):
 d=next(r for r in DATA if r['drug']==drug)
 ax=fig.add_axes([.22,.65-i*.21,.62,.12]);draw(ax,[d],'#168c88',heading)
 ax.set_title(heading,loc='left',fontsize=14,pad=5);ax.set_xlabel('');ax.set_ylim(.7,-.7)
 # Replace long point labels with short percentages; denominator is in heading.
 ax.texts[-1].set_text({'Gabapentin':'≈100%','Metformin':'≈90%','Digoxin [IV]':'50–70%'}[drug])
 fig.text(.22,.615-i*.21,detail,fontsize=10,color='#536779')
fig.text(.055,.105,'Gabapentin and metformin are incompletely absorbed: do not interpret these as 100% or 90% of a swallowed dose.',fontsize=12,fontweight='bold')
fig.text(.055,.055,'Sources: Neurontin, Glumetza and digoxin prescribing information • Per-drug links: renal-excretion-sources.md',fontsize=10,color='#536779')
for ext in ['svg','png','pdf']:fig.savefig(ROOT/('preview' if ext=='png' else 'source')/f'renal-excretion-comparators-denominators.{ext}',dpi=180,facecolor='white')
plt.close(fig)
