""" This module cleans the data"""

import argparse
from pathlib import Path
import pandas as pd
import numpy as np


def clean_data(
        region: str = 'PT'
) -> pd.DataFrame:
    """ 
    Cleans the life expectancy data by 
    loading the data, split columns, filter the region, 
    unpivot the years to long format,
    ensure year is an integer and value is a float type
    and by saving the data to a csv format file
    Args:
        region (str): String with region information

    Returns: 
        life_exp (Pandas DataFrame): DataFrame with life expectancy cleaned data
    """

    # Load eu_life_expectancy_raw.tsv data from the data folder
    script_dir = Path(__file__).resolve().parent
    file_path = script_dir / "data"/ "eu_life_expectancy_raw.tsv"


    with open(file_path, "r", encoding="UTF-8") as file:
        life_exp = pd.read_csv(file, sep="\t")

    # Split column with unit, sex, age, geo to multiple columns
    columns = ["unit", "sex", "age", "region"]
    life_exp.rename(columns={ life_exp.columns[0]: "all_columns_in_one"}, inplace = True)
    life_exp[columns] = life_exp.all_columns_in_one.str.split(",", expand = True)
    life_exp = life_exp.drop( columns = "all_columns_in_one")

    # Filters only the data where region equal to PT
    life_exp = life_exp.loc[life_exp["region"] == region]

    # Unpivot the years to long format
    life_exp = life_exp.melt(
        id_vars = columns,
        var_name = "year",
        value_name = "value"
        )

    # Ensure year is an int
    life_exp["year"] = life_exp["year"].str.replace(" ", "").astype(int)

    # Ensure value is a float
    life_exp["value"] = life_exp["value"].str.replace(r"[a-zA-Z\s]+", "",  regex=True)
    life_exp["value"] = life_exp["value"].replace(":", np.NaN)
    life_exp["value"] = life_exp["value"].astype(float)
    life_exp = life_exp.dropna(subset=["value"])

    # Save the resulting data frame to the data folder as pt_life_expectancy.csv
    life_exp.to_csv(script_dir / "data"/ "pt_life_expectancy.csv", index=False)

    return life_exp


if __name__ == '__main__': # pragma: no cover
    parser = argparse.ArgumentParser(description="Process all the arguments for this cleaning")
    parser.add_argument("--region", default="PT", help="Filters data for this region", type=str)
    args = parser.parse_args()
    clean_data(args.region)
