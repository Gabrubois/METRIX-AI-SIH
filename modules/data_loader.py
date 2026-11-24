import numpy as np, pandas as pd
from config import REQUIRED, DATA
def generate_synthetic(n_instr=300, tests=4, seed=42):
    """SYNTHETIC demo metrology data. Inspector labels are simulated, NOT real inspection data."""
    r=np.random.default_rng(seed); rows=[]
    types={"Platform Scale":("Weighing",[300,500,1000]),"Counter Scale":("Weighing",[15,30,60]),
           "Weighbridge":("Weighing",[30000,60000]),"Dispensing Pump":("Measuring",[5,20]),
           "Measuring Tape":("Measuring",[5,30]),"Liquid Measure":("Measuring",[1,5,10])}
    names=list(types)
    for i in range(n_instr):
        t=names[r.integers(len(names))]; cat,caps=types[t]; cap=float(r.choice(caps))
        wear=r.beta(1.5,4)
        usage=float(np.clip(wear*60+r.normal(30,15),1,120))
        hours=float(max(10,usage*r.uniform(20,60)+wear*500))
        fails=int(r.poisson(wear*5)); maint=max(0,int(r.poisson(2+usage/40)-wear*2))
        perm=cap*0.001; last=pd.Timestamp("2026-01-01")-pd.Timedelta(days=int(r.integers(30,700)))
        for k in range(tests):
            ref=cap*r.uniform(0.1,1); dev=r.normal(0,perm*(0.3+2.2*wear))+perm*wear*r.choice([-1,1])
            vd=last+pd.Timedelta(days=int(180*(k+1)+r.integers(-30,30)))
            nc=(abs(dev)>perm and r.random()<0.85) or r.random()<0.02
            rows.append(dict(instrument_id=f"INS{i:04d}",instrument_type=t,instrument_category=cat,instrument_capacity=cap,
              reference_value=ref,measured_value=ref+dev,calibration_deviation=dev,percentage_error=abs(dev)/abs(ref)*100,
              permissible_error=perm,verification_date=vd,last_calibration_date=last,usage_frequency=round(usage,1),
              operating_hours=round(hours,1),previous_failure_count=fails,maintenance_count=maint,
              inspector_status="Non-Compliant" if nc else "Compliant",data_source="SYNTHETIC"))
    return pd.DataFrame(rows)
def save_synthetic():
    d=generate_synthetic(); d.to_csv(DATA/"synthetic/synthetic_instrument_records.csv",index=False)
    d[["instrument_id","inspector_status","data_source"]].to_csv(DATA/"synthetic/synthetic_inspector_records.csv",index=False); return d
def validate_columns(df): return [c for c in REQUIRED if c not in df.columns]
def load_csv(f): return pd.read_csv(f)
def try_kaggle(slug):
    """Needs Kaggle credentials (~/.kaggle/kaggle.json). Returns path or None; never fakes success."""
    try:
        import kagglehub; return kagglehub.dataset_download(slug)
    except Exception as e: print("Kaggle download failed:",e); return None
