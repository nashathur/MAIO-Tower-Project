"""Convert the tower .txt data in source/ to CSV files with headers in data/.

Only the newest delivery of each file is converted, to data/<name>.csv;
later deliveries contain the earlier data (FLUX_CORR_30min was reprocessed
in the 14 Oct delivery but still covers the whole period).

Column names follow the fileformat_headers docs delivered with the data.
Values are copied unchanged (NaN stays NaN). FLUX files already carry
their own header and are copied as they are.

Run: conda run -n college python txt_to_csv.py
"""
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent
SOURCE = ROOT / "source"
DATA = ROOT / "data"

PROFILE = [
    "year", "DOY", "hhmm", "Ubatt", "Ptemp",
    "rh1", "rh2", "rh3", "rh4", "rh5",
    "T1", "T2", "T3", "T4", "T5",
    "U1", "dd1", "U2", "dd2", "U3", "dd3", "U4", "dd4", "U5", "dd5",
]

CNR1RAW = [
    "year", "doy", "hhmm",
    "SWTop", "SWBottom", "LWTop", "LWBottom", "cnr1_T_K",
]

CNR1 = [
    "year", "doy", "hhmm",
    "SWTop_Avg", "SWBottom_Avg", "LWTop_Avg", "LWBottom_Avg",
    "cnr1_T_C_Avg", "cnr1_T_K_Avg", "LWTopC_Avg", "LWBottomC_Avg",
    "Rs_net_Avg", "Rl_net_Avg", "albedo_Avg", "Rn_Avg",
    "LWTopC_Avg_biased", "LWBottomC_Avg_biased",
]

# The doc lists 71 columns but the files have 70; the data matches the doc
# through VBAT (col 54), so the trailing columns are mapped in order and the
# doc's last name, xSTATUS, is left out.
IWS = [
    "year", "mm", "dd", "hh", "minutes", "doy",
    "TC1avg", "TC1std", "TC2avg", "TC2std", "CJavg",
    "xTSTR1", "xTSTR2", "xTSTR3", "xTSTR4",
    "xTSTR5", "xTSTR6", "xTSTR7", "xTSTR8",
    "THUTavg", "RHWavg", "RHTavg",
    "HWSavg", "HWSstd", "HWSmax", "HWDavg", "VWSavg", "VWSstd",
    "NRUavg", "NRUstd", "NRLavg", "NRIUavg", "NRILavg", "NRTavg",
    "NRUcal", "NRLcal", "NRIUcal", "NRILcal", "NRID",
    "BAP", "SSH", "xADW", "xTBRG", "MCH", "TILTX", "TILTY",
    "LON", "LAT", "HMSL", "PACC", "SATS", "spare1", "spare2", "VBAT",
    "IDENTIFIER", "STATUS", "iwsID", "xID",
    "xTC1avg", "xTC2avg", "xCJavg", "xTHUTavg", "xRHWavg", "xRHTavg",
    "xHWSavg", "xHWDavg", "xVWSavg", "xSSH", "xSPARE1", "xVBAT",
]

# Columns 4-27 come from the sonic anemometer, 28-40 from the Young
# propellers; names repeated in the propeller block get a _prop suffix.
TURB = [
    "year", "DOY", "hhmm",
    "uu", "uv", "uw", "uTs", "uTc1", "uH2O",
    "vv", "vw", "vTs", "vTc1", "vH2O",
    "ww", "wTs", "wTc1", "wH2O",
    "std_Ts", "std_Tc1", "std_H2O",
    "u", "v", "w", "Ts", "Tc1", "H2O",
    "u_vect", "dd_vect", "std_dd", "ww_prop", "wu", "wTc2", "uw_prop",
    "uTc2", "TcTc2", "w_prop", "u_prop", "Tc2", "dd",
]

HEADERS = {
    "profile.txt": PROFILE,
    "profile1min.txt": PROFILE,
    "cnr1raw.txt": CNR1RAW,
    "cnr1.txt": CNR1,
    "iws.txt": IWS,
    "turb.txt": TURB,
    "FLUX_30min.txt": None,
    "FLUX_CORR_30min.txt": None,
}


def convert(src: Path, dst: Path, header: list[str] | None) -> int:
    lines = [ln.strip() for ln in src.read_text().splitlines() if ln.strip()]
    if header is not None:
        for i, ln in enumerate(lines, 1):
            n = ln.count(",") + 1
            if n != len(header):
                raise ValueError(f"{src}:{i}: {n} columns, header has {len(header)}")
        lines.insert(0, ",".join(header))
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text("\n".join(lines) + "\n", newline="\n")
    return len(lines) - 1


def delivery_date(folder: Path) -> datetime:
    """Date in a delivery folder name, e.g. Data_Tower_project_1-4_15oct2026."""
    m = re.search(r"(\d{1,2}[a-z]{3}\d{4})", folder.name)
    return datetime.strptime(m.group(1), "%d%b%Y")


def main() -> None:
    latest: dict[str, Path] = {}
    for src in SOURCE.rglob("*.txt"):
        if src.name not in HEADERS:
            raise KeyError(f"no header defined for {src.name}")
        prev = latest.get(src.name)
        if prev is None or delivery_date(src.parent) > delivery_date(prev.parent):
            latest[src.name] = src
    for name, src in sorted(latest.items()):
        dst = DATA / Path(name).with_suffix(".csv")
        rows = convert(src, dst, HEADERS[name])
        print(f"{dst.relative_to(ROOT)}: {rows} rows from {src.parent.name}")


if __name__ == "__main__":
    main()
