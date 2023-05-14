""" This module cleans the data"""

import pandas as pd
import numpy as np


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
