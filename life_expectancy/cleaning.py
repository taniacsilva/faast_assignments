""" This module cleans the data"""

import argparse
from pathlib import Path
import pandas as pd
import numpy as np


def load_data() -> pd.DataFrame:
    """
    Load eu_life_expectancy_raw.tsv data from the data folder
    Returns:
        life_exp_raw_data(Pandas DataFrame): DataFrame with data to be cleaned
    """
    script_dir = Path(__file__).resolve().parent
    file_path = script_dir/"data"/"eu_life_expectancy_raw.tsv"

    with open(file_path, "r", encoding="UTF-8") as file:
        life_exp_raw_data = pd.read_csv(file, sep="\t")

    return life_exp_raw_data


def clean_data(
        life_exp_raw_data: pd.DataFrame,
        region: str = 'PT'
) -> pd.DataFrame:
    """ 
    Cleans the life expectancy data by split columns,
    filter the region, unpivot the years to long format and
    ensure year is an integer and value is a float type
    Args:
        life_exp_raw_data(Pandas DataFrame): DataFrame with data to be cleaned
        region (str): String with region information

    Returns: 
        life_exp (Pandas DataFrame): DataFrame with life expectancy cleaned data
    """

    # Split column with unit, sex, age, geo to multiple columns
    columns = ["unit", "sex", "age", "region"]
    life_exp_raw_data[columns] = (life_exp_raw_data.iloc[:,0].str.split(',', expand = True))
    life_exp = life_exp_raw_data.drop(columns=life_exp_raw_data.columns[0])

    # Filters only the data for the region selected
    life_exp = life_exp.loc[life_exp["region"] == region]

    # Unpivot the years to long format
    life_exp = life_exp.melt(
        id_vars = columns,
        var_name = "year",
        value_name = "value"
        )

    # Ensure year is an int
    life_exp["year"] = life_exp["year"].str.replace(" ", "").astype(int)

    # Remove letters, whitespaces and replace ":" by NaN
    life_exp["value"] = life_exp["value"].str.replace(r"[a-zA-Z\s]+", "",  regex=True)
    life_exp["value"] = life_exp["value"].replace(":", np.NaN)
    # Ensure value is a float and drop NA values
    life_exp["value"] = life_exp["value"].astype(float)
    life_exp = life_exp.dropna(subset=["value"])

    return life_exp


def save_data (
        life_exp: pd.DataFrame
) -> None:
    """
    Save the resulting data frame to the data folder as pt_life_expectancy.csv
    Args:
        life_exp (Pandas DataFrame): DataFrame with life expectancy cleaned data
    """
    script_dir = Path(__file__).resolve().parent
    life_exp.to_csv(script_dir/"data"/"pt_life_expectancy.csv", index=False)


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
