""" This module cleans the data"""
import pandas as pd
import numpy as np
from life_expectancy.countries import Region

def clean_data (life_exp_raw_data: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the life expectancy data by unpivot the years to long format and
    ensure year is an integer and value is a float type
    Args:
        life_exp_raw_data(Pandas DataFrame): DataFrame with data to be cleaned
    Returns: 
        life_exp (Pandas DataFrame): DataFrame with life expectancy cleaned data"""

    # Split column with unit, sex, age, geo to multiple columns
    column_split = 'unit,sex,age,geo\\time'
    columns = ["unit", "sex", "age", "region"]

    life_exp_raw_data[columns] = life_exp_raw_data[column_split].str.split(',', expand = True)
    life_exp = life_exp_raw_data.drop(columns=[column_split])

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

def rename_and_drop_cols(life_exp: pd.DataFrame):
    """ 
    Cleans the life expectancy data by renaming Columns and drop not necessary ones 

    Args:
        life_exp(Pandas DataFrame): DataFrame with data to be cleaned
    """
    life_exp = life_exp.rename(columns={"country": "region", "life_expectancy": "value"})

    life_exp = life_exp.drop(columns=["flag", "flag_detail"])

    return life_exp

def filter_data(
        life_exp: pd.DataFrame,
        region: Region = Region.PT
) -> pd.DataFrame:
    """ 
    Cleans the life expectancy data by filtering the region
    Args:
        life_exp(Pandas DataFrame): DataFrame with data to be filtered
        region (Countries): String with region information

    Returns:
        life_exp (Pandas DataFrame): DataFrame with life expectancy filtered data
    """

    # Filters only the data for the region selected
    life_exp = life_exp[life_exp["region"] == region.value]

    return life_exp
