"""Data ingestion package for ForestAI V1."""

from .ingestion import (
    load_covertype_data,
    get_feature_columns,
    get_target_column,
    COLUMN_NAMES,
    EXPECTED_NUM_COLUMNS,
    TARGET_COLUMN,
    DEFAULT_RAW_PATH,
)

__all__ = [
    "load_covertype_data",
    "get_feature_columns",
    "get_target_column",
    "COLUMN_NAMES",
    "EXPECTED_NUM_COLUMNS",
    "TARGET_COLUMN",
    "DEFAULT_RAW_PATH",
]