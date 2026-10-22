"""Data access for the MAIO tower project."""

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

    Extra keyword arguments are passed to pandas.read_csv.
    """
    path = DATA_DIR / f"{name}.csv"
    if not path.is_file():
        raise FileNotFoundError(f"No dataset {name!r} in {DATA_DIR}; available: {DATASETS}")
    return pd.read_csv(path, **kwargs)
