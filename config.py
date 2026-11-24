from pathlib import Path
ROOT=Path(__file__).parent
DATA=ROOT/"data"
REQUIRED=["instrument_id","instrument_type","instrument_category","instrument_capacity","reference_value","measured_value","calibration_deviation","percentage_error","permissible_error","verification_date","last_calibration_date","usage_frequency","operating_hours","previous_failure_count","maintenance_count","inspector_status","data_source"]
FEATURES=["mean_abs_deviation","max_abs_deviation","mean_pct_error","calibration_failure_freq","days_since_calibration","verification_interval","usage_intensity","maintenance_freq","historical_failure_rate","violation_indicator"]

for _s in ("raw","processed","synthetic","exports"): (DATA/_s).mkdir(parents=True,exist_ok=True)
