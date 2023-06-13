import pandas as pd
from pathlib import Path
from load_save_data import TSVFileReader, FileProcessor, save_data
from cleaning import clean_data

script_dir = Path(__file__).resolve().parent
input_file_path_tsv= script_dir/"data"/"eu_life_expectancy_raw.tsv"
output_file_path = script_dir/"tests"/"fixtures"/"distinct_countries.csv"

def main():
    file_reader = TSVFileReader()
    file_processor = FileProcessor(file_reader)
    life_exp_raw_data = file_processor.processor_file(input_file_path_tsv)

    if isinstance(file_reader, TSVFileReader):
        life_exp = clean_data(life_exp_raw_data)
    else:
        life_exp = life_exp_raw_data

    distinct_countries = pd.DataFrame(life_exp.sort_values(by = "region", key=lambda x: x.str.len())['region'].unique(), columns=["region_country"])
    distinct_countries.to_csv(output_file_path, index=False)

    

if __name__ == '__main__': 
    main()


