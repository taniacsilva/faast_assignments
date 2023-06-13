""" This module cleans the data"""
from enum import Enum
import pandas as pd
import numpy as np

class Regions(Enum):
    """Represents the Countries and Regions that exist in the raw dataset"""
    AT = 'AT'
    FI = 'FI'
    ES = 'ES'
    EL = 'EL'
    EE = 'EE'
    DK = 'DK'
    DE = 'DE'
    CZ = 'CZ'
    CY = 'CY'
    CH = 'CH'
    BG = 'BG'
    BE = 'BE'
    FX = 'FX'
    SK = 'SK'
    SI = 'SI'
    SE = 'SE'
    RO = 'RO'
    PT = 'PT'
    PL = 'PL'
    NO = 'NO'
    NL = 'NL'
    LU = 'LU'
    LT = 'LT'
    IT = 'IT'
    UK = 'UK'
    IS = 'IS'
    HU = 'HU'
    IE = 'IE'
    MT = 'MT'
    MK = 'MK'
    LI = 'LI'
    FR = 'FR'
    RS = 'RS'
    HR = 'HR'
    LV = 'LV'
    UA = 'UA'
    TR = 'TR'
    ME = 'ME'
    AL = 'AL'
    AZ = 'AZ'
    GE = 'GE'
    BY = 'BY'
    AM = 'AM'
    MD = 'MD'
    SM = 'SM'
    RU = 'RU'
    XK = 'XK'
    EFTA = 'EFTA'
    EA18 = 'EA18'
    EA19 = 'EA19'
    EU28 = 'EU28'
    EEA31 = 'EEA31'
    DE_TOT = 'DE_TOT'
    EU27_2020 = 'EU27_2020'
    EU27_2007 = 'EU27_2007'
    EEA30_2007 = 'EEA30_2007'

    @staticmethod
    def obtain_countries_list():
        "Return list of actual countries"
        regions_only = [
            'EFTA',
            'EA18',
            'EA19',
            'EU28',
            'EEA31',
            'DE_TOT',
            'EU27_2020',
            'EU27_2007',
            'EEA30_2007'
            ]
        
        return [item.value for item in Regions if item.value not in regions_only]


def clean_data (life_exp_raw_data: pd.DataFrame):
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

def feature_cleaning(life_exp: pd.DataFrame):
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
        region: Regions = Regions.PT
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