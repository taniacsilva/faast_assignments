"""This model loads and saves the data"""

from pathlib import Path
from typing import Any, Protocol
import zipfile
import pandas as pd


class FileReaderStrategy(Protocol):
    """Reads the file"""

    def __call__(self, file:Any) -> pd.DataFrame:
        """
        Reads the file and returns the data as a pandas DataFrame
        Args:
            file (Any): file object to read
        Returns:
            pd.DataFrame: The data read from the file as a pandas DataFrame
        Raises:
            NotImplementedError: This is a protocol method, so must be implemented by subclasses
        """

        raise NotImplementedError("This method should be implemented by subclasses")


class TSVFileReader:
    """Reads the TSV File"""

    def __call__(self, file:Any) -> pd.DataFrame:
        """
        Reads a TSV file and returns the data as a pandas DataFrame
        Args:
            file (Any): file object to read
        Returns:
            pd.DataFrame: The data read from the TSV file as a pandas DataFrame
        """

        return pd.read_csv(file, sep= "\t")


class JSONFileReader:
    """Reads the JSON File"""

    def __call__(self, file:Any) -> pd.DataFrame:
        """        
        Reads a JSON file and returns the data as a pandas DataFrame
        Args:
            file (Any): file object to read
        Returns:
            pd.DataFrame: The data read from the JSON file as a pandas DataFrame"""

        with zipfile.ZipFile(file) as zip_file:
            with zip_file.open(zip_file.namelist()[0]) as json_file:
                return pd.read_json(json_file)


class FileProcessor:
    """Processes the file using a FileReaderStrategy"""
    def __init__(self, file_reader: FileReaderStrategy):
        self.file_reader = file_reader

    def process_file(self, file_path: Path):
        """
        Processes the file and returns the data as a pandas DataFrame
        Args:
            file_path (Path): The path to the file to process 
        Returns:
            pd.Dataframe: The data read from the file as a pandas DataFrame
        """
        with open(file_path, "rb") as file:
            life_exp_raw_data = self.file_reader(file)

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
