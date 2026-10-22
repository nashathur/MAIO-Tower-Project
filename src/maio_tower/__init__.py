"""Data access for the MAIO tower project."""

import re
from pathlib import Path

import pandas as pd

__version__ = "0.1.0"

_PACKAGE_DIR = Path(__file__).resolve().parent

# A wheel install carries data/ and source/ inside the package; an editable
# install reads them from the repository root.
if (_PACKAGE_DIR / "data").is_dir():
    DATA_DIR = _PACKAGE_DIR / "data"
    SOURCE_DIR = _PACKAGE_DIR / "source"
else:
    DATA_DIR = _PACKAGE_DIR.parents[1] / "data"
    SOURCE_DIR = _PACKAGE_DIR.parents[1] / "source"

DATASETS = sorted(p.stem for p in DATA_DIR.glob("*.csv"))

# Delivery folders are named like Data_Tower_project_1-4_15oct2026; the key is "15oct".
DELIVERIES = {
    re.search(r"_(\d+[a-z]+)\d{4}", d.name).group(1): d
    for d in sorted(SOURCE_DIR.glob("Data_Tower_*"))
    if d.is_dir()
}


def load(name, **kwargs):
    """Read data/<name>.csv into a DataFrame, e.g. load("profile").

    Extra keyword arguments are passed to pandas.read_csv.
    """
    path = DATA_DIR / f"{name}.csv"
    if not path.is_file():
        raise FileNotFoundError(f"No dataset {name!r} in {DATA_DIR}; available: {DATASETS}")
    return pd.read_csv(path, **kwargs)


def load_txt(name, delivery=None, **kwargs):
    """Read the original source/<delivery>/<name>.txt into a DataFrame, e.g. load_txt("profile", "8oct").

    delivery is a key of DELIVERIES; None takes the latest delivery that has the file.
    Files without a header row get the column names of data/<name>.csv.
    Extra keyword arguments are passed to pandas.read_csv.
    """
    if delivery is None:
        candidates = [d for d in DELIVERIES if (DELIVERIES[d] / f"{name}.txt").is_file()]
        if not candidates:
            raise FileNotFoundError(f"No {name}.txt in any delivery in {SOURCE_DIR}")
        delivery = max(candidates, key=lambda d: int(re.match(r"\d+", d).group()))
    if delivery not in DELIVERIES:
        raise KeyError(f"Unknown delivery {delivery!r}; available: {list(DELIVERIES)}")
    path = DELIVERIES[delivery] / f"{name}.txt"
    if not path.is_file():
        raise FileNotFoundError(f"No {name}.txt in delivery {delivery!r}")
    with open(path) as f:
        has_header = not f.readline()[:1].isdigit()
    if not has_header and "names" not in kwargs and (DATA_DIR / f"{name}.csv").is_file():
        kwargs["header"] = None
        kwargs["names"] = pd.read_csv(DATA_DIR / f"{name}.csv", nrows=0).columns
    return pd.read_csv(path, **kwargs)
