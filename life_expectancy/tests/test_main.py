"""Tests for the main module"""
# pylint: disable=unused-argument

from pytest import MonkeyPatch
import pandas as pd

from life_expectancy.main import main



def test_main(pt_life_expectancy_expected, monkeypatch: MonkeyPatch):
    """Run the `main` function and compare the output to the expected output
    Args:
        pt_life_expectancy_expected (Fixture) : load the expected output of the cleaning script
        monkeypatch (MonkeyPatch): pytest fixture that provides a way to modify the behavior of 
            functions or classes during tests.
    Returns:
    """
    # Define a mock function to replace pd.DataFrame.to_csv
    def mock_to_csv(*args, **kwargs):
        print("Data saved successfully")

    # Patch pd.DataFrame.to_csv to return the mock function instead of the real one
    monkeypatch.setattr(pd.DataFrame, 'to_csv', mock_to_csv)

    # Call the main function and get the result
    pt_life_expectancy_actual = main(region = 'PT').reset_index(drop=True)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
