"""Pytest configuration file"""

import pandas as pd
import pytest
from pathlib import Path

from . import FIXTURES_DIR, OUTPUT_DIR


@pytest.fixture(autouse=True)
def run_before_and_after_tests() -> None:
    """Fixture to execute commands before and after a test is run"""
    # Setup: fill with any logic you want

    yield # this is where the testing happens

    # Teardown : fill with any logic you want
    file_path = OUTPUT_DIR / "pt_life_expectancy.csv"
    file_path.unlink(missing_ok=True)


@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")

@pytest.fixture()
def eu_life_expectancy_input_expected() -> pd.DataFrame:
    """Fixture to load the expected raw data"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_raw.tsv", sep="\t")

@pytest.fixture()
def input_file_path_test() -> Path:
    """Fixture for the path to the test file to be loaded"""
    script_dir = Path(__file__).resolve().parent
    return script_dir/"fixtures"/"eu_life_expectancy_raw.tsv"
    
@pytest.fixture()
def output_file_path_test() -> Path:
    """Fixture for the path where the test file could be saved"""
    script_dir = Path(__file__).resolve().parent
    return script_dir / "fixtures" / "pt_life_expectancy_test_save_data.csv"
