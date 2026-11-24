import numpy as np, pandas as pd
def build_features(t):
    t=t.copy(); t["abs_dev"]=t.calibration_deviation.abs(); t["viol"]=(t.abs_dev>t.permissible_error).astype(int)
    t["since"]=(t.verification_date-t.last_calibration_date).dt.days
    t=t.sort_values(["instrument_id","verification_date"])
    t["gap"]=t.groupby("instrument_id").verification_date.diff().dt.days
    g=t.groupby("instrument_id")
    f=pd.DataFrame({"mean_abs_deviation":g.abs_dev.mean(),"max_abs_deviation":g.abs_dev.max(),
      "mean_pct_error":g.percentage_error.mean(),"calibration_failure_freq":g.viol.mean(),
      "days_since_calibration":g.since.mean(),"verification_interval":g.gap.mean().fillna(g.since.mean()),
      "usage_intensity":g.operating_hours.first()/g.usage_frequency.first().replace(0,np.nan),
      "maintenance_freq":g.maintenance_count.first(),
      "historical_failure_rate":g.previous_failure_count.first()/g.size(),
      "violation_indicator":g.viol.max()})
    f["usage_frequency"]=g.usage_frequency.first(); f["instrument_category"]=g.instrument_category.first()
    f["instrument_type"]=g.instrument_type.first(); f["data_source"]=g.data_source.first()
    f["confirmed_non_compliant"]=g.inspector_status.apply(lambda s:int((s=="Non-Compliant").mean()>=0.5))
    return f.fillna(0).reset_index()
