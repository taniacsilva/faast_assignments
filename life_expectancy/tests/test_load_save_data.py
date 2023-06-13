"""Tests for the load_save_data module"""
# pylint: disable=unused-argument

from pathlib import Path
from pytest import MonkeyPatch

import pandas as pd

from life_expectancy.load_save_data import TSVFileReader, JSONFileReader, FileProcessor, save_data


script_dir = Path(__file__).resolve().parent



def test_load_data_TSV(eu_life_expectancy_input_expected, input_file_path_test) -> None:
    """Run the `load_data` function and compare the raw data loaded to the expected raw data loaded
        Args:
            eu_life_expectancy_raw_expected (Fixture): load the expected raw data
            input_file_path_test (Fixture):  Fixture for the path to the test file to be loaded
        Returns: 
    """
    file_reader = TSVFileReader()
    file_processor = FileProcessor(file_reader)

    # Call the load_data function and get the result
    eu_life_expectancy_input_actual = file_processor.processor_file(input_file_path_test)

    pd.testing.assert_frame_equal(
        eu_life_expectancy_input_actual, eu_life_expectancy_input_expected
    )

def test_load_data_zip(eurostat_life_input_expect_zip, input_file_path_test_zip) -> None:
    """Run the `load_data` function and compare the raw data loaded to the expected raw data loaded
        Args:
            eu_life_expectancy_raw_expected_zip (Fixture): load the expected raw data
            input_file_path_test_zip (Fixture):  Fixture for the path to the test file to be loaded
        Returns: 
    """
    file_reader = JSONFileReader()
    file_processor = FileProcessor(file_reader)

    # Call the load_data function and get the result
    eu_life_expectancy_input_actual = file_processor.processor_file(input_file_path_test_zip)

    pd.testing.assert_frame_equal(
        eu_life_expectancy_input_actual, eurostat_life_input_expect_zip
    )

def test_save_data(
        monkeypatch: MonkeyPatch,
        capsys,
        output_file_path_test
    ) -> None:
    """Run the `save_data` function and compare if data is being saved
        Args:
            monkeypatch (MonkeyPatch): pytest fixture that provides a way to modify the behavior of 
            functions or classes during tests.
            capsys (Fixture): pytest fixture that allows capturing stdout and stderr during tests.
            output_file_path_test (Fixture): Fixture for the path where the test file could be saved
        Returns:
    """
    # Create a sample DataFrame to use for testing
    data = pd.DataFrame()

    # Define a mock function to replace pd.DataFrame.to_csv
    def mock_to_csv(*args, **kwargs):
        print("Data saved successfully")

    # Patch pd.DataFrame.to_csv to return the mock function instead of the real one
    monkeypatch.setattr(data, 'to_csv', mock_to_csv)

    # Call the save_data function and get the result
    save_data(data, output_file_path_test)

    captured = capsys.readouterr()

    assert "Data saved successfully" in captured.out
    