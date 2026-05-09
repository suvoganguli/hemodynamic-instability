from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

# --------------------------------------------------
# Project paths
# --------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent

DATA_DIR = ROOT_DIR / "data"

RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"

OUTPUT_DIR = ROOT_DIR / "outputs"

FIGURE_DIR = OUTPUT_DIR / "figures"
TABLE_DIR = OUTPUT_DIR / "tables"

REPORT_DIR = ROOT_DIR / "reports"

# --------------------------------------------------
# Dataset paths
# --------------------------------------------------

TRAINING_SET_A = RAW_DIR / "training_setA" / "training_setA"
TRAINING_SET_B = RAW_DIR / "training_setB" / "training_setB"

# --------------------------------------------------
# Core physiological signals
# --------------------------------------------------

CORE_SIGNALS = [
    "HR",
    "O2Sat",
    "Temp",
    "SBP",
    "MAP",
    "DBP",
    "Resp",
]

# --------------------------------------------------
# Hemodynamic settings
# --------------------------------------------------

MAP_THRESHOLD = 65

LOOKBACK_HOURS = 6
PREDICTION_HOURS = 6

# --------------------------------------------------
# Utilities
# --------------------------------------------------

def ensure_dirs():
    """
    Create output folders if missing.
    """

    dirs = [
        INTERIM_DIR,
        PROCESSED_DIR,
        FIGURE_DIR,
        TABLE_DIR,
        REPORT_DIR,
    ]

    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)


def savefig(name, dpi=300, bbox_inches="tight"):
    """
    Save matplotlib figure.
    """

    ensure_dirs()

    path = FIGURE_DIR / name

    plt.savefig(path, dpi=dpi, bbox_inches=bbox_inches)

    print(f"Saved figure: {path}")


def savetable(df, name):
    """
    Save dataframe as CSV.
    """

    ensure_dirs()

    path = TABLE_DIR / name

    df.to_csv(path, index=False)

    print(f"Saved table: {path}")


def varsave(obj, name):
    """
    Save dataframe/object to processed directory.
    """

    ensure_dirs()

    path = PROCESSED_DIR / name

    if isinstance(obj, pd.DataFrame):

        if name.endswith(".parquet"):
            obj.to_parquet(path, index=False)

        elif name.endswith(".csv"):
            obj.to_csv(path, index=False)

        else:
            obj.to_pickle(path)

    else:
        pd.to_pickle(obj, path)

    print(f"Saved object: {path}")
