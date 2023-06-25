"""This model loads and saves the data"""

from pathlib import Path
from typing import Any, Protocol
import zipfile
import pandas as pd
from life_expectancy.cleaning import clean_data, rename_and_drop_cols


class FileHandlerStrategy(Protocol):
    """Reads Aand Cleans the file"""

    def load_file(self, file:Any):
        """
        Reads the file and returns the data as a pandas DataFrame
        Args:
            file (Any): file object to read
        """
    def clean_file(self, file:Any):
        """
        Cleans data and returns the data as a pandas DataFrame
        Args:
            file (Any): file object to read
        """

class TSVFileHandler:
    """Reads the TSV File"""

    def load_file(self, file:Any) -> pd.DataFrame:
        """
        Reads a TSV file and returns the data as a pandas DataFrame
        Args:
            file (Any): file object to read
        Returns:
            pd.DataFrame: The data read from the TSV file as a pandas DataFrame
        """

        return pd.read_csv(file, sep= "\t")

    def clean_data(self, file: Any) -> pd.DataFrame:
        """
        Cleans data and returns the data as a pandas DataFrame
        Args:
            file (Any): file object to read
        Returns:
            pd.DataFrame: The data read from the JSON file as a pandas DataFrame"""

        cleaned_data = clean_data(file)

        return cleaned_data


class JSONFileHandler:
    """Reads the JSON File"""

    def load_file(self, file:Any) -> pd.DataFrame:
        """        
        Reads a JSON file and returns the data as a pandas DataFrame
        Args:
            file (Any): file object to read
        Returns:
            pd.DataFrame: The data read from the JSON file as a pandas DataFrame"""

        return pd.read_json(file, compression="infer")

    def clean_data(self, file: Any) -> pd.DataFrame:
        """
        Cleans data and returns the data as a pandas DataFrame
        Args:
            file (Any): file object to read
        Returns:
            pd.DataFrame: The data read from the JSON file as a pandas DataFrame"""

        cleaned_data = rename_and_drop_cols(file)

        return cleaned_data


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
