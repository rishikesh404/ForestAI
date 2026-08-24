"""Tests for data ingestion module."""

import sys
from pathlib import Path

import pytest

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pandas as pd
from src.data import (
    load_covertype_data,
    get_feature_columns,
    get_target_column,
    COLUMN_NAMES,
    EXPECTED_NUM_COLUMNS,
    TARGET_COLUMN,
    DEFAULT_RAW_PATH,
)


class TestIngestion:
    """Tests for covertype data ingestion."""

    def test_raw_file_exists(self):
        """Verify the raw data file exists at expected location."""
        assert DEFAULT_RAW_PATH.exists(), f"Raw file not found at {DEFAULT_RAW_PATH}"

    def test_load_data_returns_dataframe(self):
        """Test that loading returns a pandas DataFrame."""
        df = load_covertype_data()
        assert isinstance(df, pd.DataFrame)

    def test_expected_number_of_columns(self):
        """Test that the loaded data has 55 columns."""
        df = load_covertype_data()
        assert df.shape[1] == EXPECTED_NUM_COLUMNS

    def test_expected_number_of_rows(self):
        """Test that the loaded data has 581,012 rows."""
        df = load_covertype_data()
        assert df.shape[0] == 581012

    def test_target_column_exists(self):
        """Test that Cover_Type target column exists."""
        df = load_covertype_data()
        assert TARGET_COLUMN in df.columns

    def test_target_column_values(self):
        """Test that target values are in expected range 1-7."""
        df = load_covertype_data()
        assert df[TARGET_COLUMN].min() == 1
        assert df[TARGET_COLUMN].max() == 7

    def test_column_names_match_documentation(self):
        """Test that column names match UCI documentation."""
        df = load_covertype_data()
        assert list(df.columns) == COLUMN_NAMES

    def test_data_non_empty(self):
        """Test that loaded data is not empty."""
        df = load_covertype_data()
        assert len(df) > 0
        assert df.shape[1] > 0

    def test_invalid_path_raises_clear_error(self):
        """Test that missing file produces clear FileNotFoundError."""
        with pytest.raises(FileNotFoundError) as exc_info:
            load_covertype_data("data/raw/covertype/nonexistent.gz")
        assert "not found" in str(exc_info.value).lower()

    def test_get_feature_columns_excludes_target(self):
        """Test that feature columns list excludes target."""
        features = get_feature_columns()
        assert TARGET_COLUMN not in features
        assert len(features) == EXPECTED_NUM_COLUMNS - 1

    def test_get_target_column(self):
        """Test target column name accessor."""
        assert get_target_column() == TARGET_COLUMN


if __name__ == "__main__":
    pytest.main([__file__, "-v"])