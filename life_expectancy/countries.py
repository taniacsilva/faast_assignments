"""This module contains enumerates the possible entries for region """
from enum import Enum
from pathlib import Path

script_dir = Path(__file__).resolve().parent
input_file_path_tsv= script_dir/"data"/"eu_life_expectancy_raw.tsv"
output_file_path = script_dir/"tests"/"fixtures"/"distinct_countries.csv"

class Region(Enum):
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

        return [item.value for item in Region if item.value not in regions_only]
    