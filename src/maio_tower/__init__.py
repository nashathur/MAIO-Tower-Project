"""Data access for the MAIO tower project.

Datasets available with load(name), one per CSV in data/ (latest delivery):

    name             interval  time zone  period (2026)        contents
    profile          30 min    CEST       15 Sep - 12 Oct      profile mast: Vaisala T1-T5, rh1-rh5, wind U1-U5/dd1-dd5 at 8, 4, 2, 1, 0.5 m
    profile1min      1 min     CEST       8 Sep - 12 Oct       same columns as profile; values invalid before 15 Sep 14:01
    iws              30 min    UTC        15 Sep - 12 Oct      iWS station: THUTavg, RHTavg, RHWavg, wind, BAP, CNR4 radiation (NR*)
    cnr1             30 min    CEST       15 Sep - 12 Oct      CNR1 radiometer: SW/LW in/out, body temperature, albedo, Rn
    cnr1raw          10 s      CEST       8 Sep - 12 Oct       CNR1 raw SW/LW and body temperature; invalid before 15 Sep 14:01
    turb             30 min    CEST       15 Sep - 12 Oct      sonic (u, v, w, Ts), thermocouples Tc1/Tc2, propellers, covariances
    FLUX_30min       30 min    CEST       15 Sep - 12 Oct      sonic, thermocouples Tc/Tc2, Young propellers, covariances
    FLUX_CORR_30min  30 min    CEST       15 Sep - 12 Oct      FLUX_30min after coordinate rotation

All loggers stamp a 30-min average at the end of its interval. Column meanings
and known data problems are listed in README.md.
"""

from pathlib import Path

import pandas as pd

__version__ = "0.1.0"

_PACKAGE_DIR = Path(__file__).resolve().parent

# A wheel install carries the CSVs inside the package; an editable install
# reads them from data/ at the repository root.
if (_PACKAGE_DIR / "data").is_dir():
    DATA_DIR = _PACKAGE_DIR / "data"
else:
    DATA_DIR = _PACKAGE_DIR.parents[1] / "data"

DATASETS = sorted(p.stem for p in DATA_DIR.glob("*.csv"))


def load(name, **kwargs):
    """Read data/<name>.csv into a DataFrame, e.g. load("profile").

    name is one of DATASETS: profile, profile1min, iws, cnr1, cnr1raw, turb,
    FLUX_30min, FLUX_CORR_30min (see the module docstring for contents).

    Extra keyword arguments are passed to pandas.read_csv.
    """
    path = DATA_DIR / f"{name}.csv"
    if not path.is_file():
        raise FileNotFoundError(f"No dataset {name!r} in {DATA_DIR}; available: {DATASETS}")
    return pd.read_csv(path, **kwargs)
