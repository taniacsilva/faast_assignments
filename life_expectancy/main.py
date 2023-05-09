"""This is the main module"""

import argparse
import pandas as pd

from life_expectancy.cleaning import clean_data
from life_expectancy.load_save_data import load_data, save_data


def main(region: str = 'PT') -> None:
    """
    Main function that load, cleans and save a cleaned version of the life expectancy data
    Args:
        region (str): String with region information
    """
    life_exp_raw_data = load_data()
    life_exp = clean_data(life_exp_raw_data, region)
    save_data(life_exp)


if __name__ == '__main__': # pragma: no cover
    parser = argparse.ArgumentParser(description="Process all the arguments for this cleaning")
    parser.add_argument("--region", default="PT", help="Filters data for this region", type=str)
    args = parser.parse_args()
    main(region = args.region)
