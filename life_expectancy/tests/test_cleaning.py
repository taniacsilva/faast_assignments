"""Tests for the cleaning module"""

import pandas as pd

from life_expectancy.cleaning import clean_data, filter_data, feature_cleaning, Regions

def test_cleaning_tsv(pt_life_expectancy_expected, eu_life_expectancy_input_expected):
    """Compare the output of the "clean_data" function to the expected output
        Args:
            pt_life_expectancy_expected (Fixture): load the expected output of the cleaning script
            eu_life_expectancy_input_expected (Fixture): load the expected raw data
        Returns:
    """
    # Call the clean_data function and get the result
    clean_data_output_actual = clean_data(eu_life_expectancy_input_expected)

    clean_data_output_actual = filter_data(
        clean_data_output_actual, 
        region = Regions.PT
    ).reset_index(drop=True)

    clean_data_output_expected = pt_life_expectancy_expected

    pd.testing.assert_frame_equal(
        clean_data_output_actual, clean_data_output_expected
    )

def test_cleaning_zip(pt_life_expectancy_expected, eurostat_life_input_expect_zip):
    """Compare the output of the "clean_data" function for zip files to the expected output
        Args:
            pt_life_expectancy_expected (Fixture): load the expected output of the cleaning script
            eu_life_expectancy_input_expected_zip (Fixture): load the expected raw data
        Returns:
    """
    # Call the clean_data function and get the result
    clean_data_output_actual = feature_cleaning(eurostat_life_input_expect_zip)

    clean_data_output_actual = filter_data(
        clean_data_output_actual, 
        region = Regions.PT
    ).reset_index(drop=True)

    clean_data_output_expected = pt_life_expectancy_expected

    pd.testing.assert_frame_equal(
        clean_data_output_actual, clean_data_output_expected
    )

def test_obtain_countries_list(country_list_expected):
    """Test obtain countries list function to compare the output of the function to the expected output"
        Args:
            country_list_expected (Fixture): load the expected output of the function
    """
    country_list_actual = Regions.obtain_countries_list()

    assert not set(country_list_actual) ^ set(country_list_expected)          