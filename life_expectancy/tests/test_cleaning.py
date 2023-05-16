"""Tests for the cleaning module"""

import pandas as pd

from life_expectancy.cleaning import clean_data


def test_cleaning(pt_life_expectancy_expected, eu_life_expectancy_input_expected):
    """Compare the output of the "clean_data" function to the expected output
        Args:
            pt_life_expectancy_expected (Fixture): load the expected output of the cleaning script
            eu_life_expectancy_raw_expected (Fixture): load the expected raw data
        Returns:
    """
    # Call the clean_data function and get the result
    clean_data_output_actual = clean_data(
        eu_life_expectancy_input_expected,
        region = 'PT'
    ).reset_index(drop=True)

    clean_data_output_expected = pt_life_expectancy_expected

    pd.testing.assert_frame_equal(
        clean_data_output_actual, clean_data_output_expected
    )
           