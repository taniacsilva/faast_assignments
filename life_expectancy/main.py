"""This is the main module"""
from pathlib import Path
import argparse
import pandas as pd
from life_expectancy.cleaning import filter_data, clean_data, feature_cleaning, Regions
from life_expectancy.load_save_data import TSVFileReader, JSONFileReader, FileProcessor, save_data


script_dir = Path(__file__).resolve().parent
input_file_path_tsv= script_dir/"data"/"eu_life_expectancy_raw.tsv"
input_file_path_json = script_dir/"data"/"eurostat_life_expect.zip"
output_file_path = script_dir/"data"/"pt_life_expectancy.csv"


def main(region: Regions = Regions.PT) -> pd.DataFrame:
    """
    Main function that load, cleans and save a cleaned version of the life expectancy data
    Args:
        region (Regions): Enum with region information
    """
    # Verify if the region is in the list of Contries and Regions
    if region.value not in Regions.__members__:
        raise ValueError("This is an Invalid Country")

    file_reader = JSONFileReader()
    file_processor = FileProcessor(file_reader)
    life_exp_raw_data = file_processor.processor_file(input_file_path_json)

    if isinstance(file_reader, TSVFileReader):
        life_exp = clean_data(life_exp_raw_data)
    else:
        life_exp = feature_cleaning(life_exp_raw_data)

    life_exp = filter_data(life_exp, region)

    save_data(life_exp, output_file_path)

    return life_exp


if __name__ == '__main__': # pragma: no cover
    parser = argparse.ArgumentParser(description="Process all the arguments for this cleaning")
    parser.add_argument("--region", default=Regions.PT, help="Filters data for this region")
    args = parser.parse_args()
    main(region = args.region)
