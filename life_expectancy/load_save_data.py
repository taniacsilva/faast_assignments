"""This model loads and saves the data"""
from pathlib import Path

import pandas as pd


def load_data(
        input_file_path: Path
    ) -> pd.DataFrame:
    """
    Load eu_life_expectancy_raw.tsv data from the data folder
    Args:
        input_file_path (Path): Path for the file to be loaded
    Returns:
        life_exp_raw_data (Pandas DataFrame): DataFrame with data to be cleaned
    """
    with open(input_file_path, "r", encoding="UTF-8") as file:
        life_exp_raw_data = pd.read_csv(file, sep="\t")

    return life_exp_raw_data


def save_data(
        life_exp: pd.DataFrame,
        output_file_path: Path
    ) -> None:
    """
    Save the resulting data frame to the data folder as pt_life_expectancy.csv
    Args:
        life_exp (Pandas DataFrame): DataFrame with life expectancy cleaned data
        output_file_path(Path) : Path where the file should be saved
    """
    life_exp.to_csv(output_file_path, index=False)
