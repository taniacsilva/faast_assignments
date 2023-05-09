"""This model loads and saves the data"""

from pathlib import Path
import pandas as pd


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