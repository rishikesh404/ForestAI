"""Data ingestion module for UCI Covertype dataset."""

from pathlib import Path
import pandas as pd


# Column names based on UCI documentation (covtype.info)
COLUMN_NAMES = [
    "Elevation",
    "Aspect",
    "Slope",
    "Horizontal_Distance_To_Hydrology",
    "Vertical_Distance_To_Hydrology",
    "Horizontal_Distance_To_Roadways",
    "Hillshade_9am",
    "Hillshade_Noon",
    "Hillshade_3pm",
    "Horizontal_Distance_To_Fire_Points",
    # 4 Wilderness Area binary columns
    "Wilderness_Area_Rawah",
    "Wilderness_Area_Neota",
    "Wilderness_Area_Comanche_Peak",
    "Wilderness_Area_Cache_la_Poudre",
    # 40 Soil Type binary columns
    "Soil_Type_1",
    "Soil_Type_2",
    "Soil_Type_3",
    "Soil_Type_4",
    "Soil_Type_5",
    "Soil_Type_6",
    "Soil_Type_7",
    "Soil_Type_8",
    "Soil_Type_9",
    "Soil_Type_10",
    "Soil_Type_11",
    "Soil_Type_12",
    "Soil_Type_13",
    "Soil_Type_14",
    "Soil_Type_15",
    "Soil_Type_16",
    "Soil_Type_17",
    "Soil_Type_18",
    "Soil_Type_19",
    "Soil_Type_20",
    "Soil_Type_21",
    "Soil_Type_22",
    "Soil_Type_23",
    "Soil_Type_24",
    "Soil_Type_25",
    "Soil_Type_26",
    "Soil_Type_27",
    "Soil_Type_28",
    "Soil_Type_29",
    "Soil_Type_30",
    "Soil_Type_31",
    "Soil_Type_32",
    "Soil_Type_33",
    "Soil_Type_34",
    "Soil_Type_35",
    "Soil_Type_36",
    "Soil_Type_37",
    "Soil_Type_38",
    "Soil_Type_39",
    "Soil_Type_40",
    # Target
    "Cover_Type",
]

EXPECTED_NUM_COLUMNS = 55
TARGET_COLUMN = "Cover_Type"
DEFAULT_RAW_PATH = Path("data/raw/covertype/covtype.data.gz")


def load_covertype_data(raw_path: Path | str = DEFAULT_RAW_PATH) -> pd.DataFrame:
    """
    Load the UCI Covertype dataset from the raw gzipped file.

    Args:
        raw_path: Path to the covtype.data.gz file.

    Returns:
        DataFrame with 55 columns (54 features + 1 target) and proper column names.

    Raises:
        FileNotFoundError: If the raw file doesn't exist.
        ValueError: If the loaded data doesn't have the expected structure.
    """
    raw_path = Path(raw_path)

    if not raw_path.exists():
        raise FileNotFoundError(f"Raw data file not found: {raw_path}")

    # Load the gzipped CSV (no header, comma-separated)
    df = pd.read_csv(raw_path, compression="gzip", header=None, names=COLUMN_NAMES)

    # Validate structure
    if df.shape[1] != EXPECTED_NUM_COLUMNS:
        raise ValueError(
            f"Expected {EXPECTED_NUM_COLUMNS} columns, got {df.shape[1]}. "
            f"File may be corrupted or have unexpected format."
        )

    if df.shape[0] == 0:
        raise ValueError("Loaded dataset is empty")

    if TARGET_COLUMN not in df.columns:
        raise ValueError(f"Target column '{TARGET_COLUMN}' not found in loaded data")

    return df


def get_feature_columns() -> list[str]:
    """Return list of feature column names (excluding target)."""
    return [c for c in COLUMN_NAMES if c != TARGET_COLUMN]


def get_target_column() -> str:
    """Return the target column name."""
    return TARGET_COLUMN