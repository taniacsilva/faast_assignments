"""Tests for the load_save_data module"""
# pylint: disable=unused-argument

from pathlib import Path
from pytest import MonkeyPatch

import pandas as pd

from life_expectancy.load_save_data import load_data, save_data

script_dir = Path(__file__).resolve().parent


def test_load_data(eu_life_expectancy_raw_expected) -> None:
    """Run the `load_data` function and compare the raw data loaded to the expected raw data loaded
        Args:
            eu_life_expectancy_raw_data (Fixture) : load the expected raw data
        Returns: 
    """

    # Call the load_data function and get the result
    input_file_path = script_dir/"fixtures"/"eu_life_expectancy_raw.tsv"
    eu_life_expectancy_raw_actual = load_data(input_file_path)

    pd.testing.assert_frame_equal(
        eu_life_expectancy_raw_actual, eu_life_expectancy_raw_expected
    )


def test_save_data(
        monkeypatch: MonkeyPatch,
        capsys
    ) -> None:
    """Run the `save_data` function and compare if data is being saved
        Args:
            monkeypatch: pytest fixture that provides a way to modify the behavior of 
            functions or classes during tests.
            capsys: pytest fixture that allows capturing stdout and stderr during tests.
        Returns:
    """
    # Create a sample DataFrame to use for testing
    data = pd.DataFrame()

    # Define a mock function to replace pd.DataFrame.to_csv
    def mock_to_csv(*args, **kwargs):
        print("Data saved successfully")

    # Patch pd.DataFrame.to_csv to return the mock function instead of the real one
    monkeypatch.setattr(pd.DataFrame, 'to_csv', mock_to_csv)

    # Call the save_data function and get the result
    output_file_path = script_dir / "fixtures" / "pt_life_expectancy_test_save_data.csv"
    save_data(data, output_file_path)

    captured = capsys.readouterr()

    assert "Data saved successfully" in captured.out
    