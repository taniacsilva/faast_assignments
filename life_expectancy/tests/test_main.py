"""Tests for the main module"""

import pandas as pd

from life_expectancy.main import main


def test_main(pt_life_expectancy_expected):
    """Run the `main` function and compare the output to the expected output
    Args:
        pt_life_expectancy_expected (Fixture) : load the expected output of the cleaning script
    Returns:
    """
    # Call the main function and get the result
    pt_life_expectancy_actual = main(region = 'PT').reset_index(drop=True)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
