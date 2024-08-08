import csv
import json
from pathlib import Path
from typing import List, Tuple, Dict

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'datas'


def get_json_from_file(filename: str) -> Dict:
    """
    Reads and returns the JSON data from the specified file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        Dict: The JSON data loaded as a dictionary.
    """
    file_path = DATA_DIR / filename
    with open(file_path, 'r') as file:
        return json.load(file)


def get_csv_data_as_dict(filename: str) -> List[Dict]:
    """
    Reads and returns the CSV data as a list of dictionaries.

    Args:
        filename (str): The name of the CSV file.

    Returns:
        List[Dict]: The CSV data as a list of dictionaries.
    """
    file_path = DATA_DIR / filename
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        return list(csv_reader)


def get_data_as_list(filename: str) -> List[List[str]]:
    """
    Reads and returns the CSV data as a list of lists.

    Args:
        filename (str): The name of the CSV file.

    Returns:
        List[List[str]]: The CSV data as a list of lists.
    """
    file_path = DATA_DIR / filename
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        return list(csv_reader)


def get_data_as_tuple(filename: str) -> List[Tuple[List[str], str]]:
    """
    Reads and returns the CSV data as a list of tuples, where each tuple contains a list of inputs and a scalar value
    for the output status.

    Args:
        filename (str): The name of the CSV file.

    Returns:
        List[Tuple[List[str], str]]: The CSV data as a list of tuples.
    """
    data_list = get_data_as_list(filename)
    return [(row[:2], row[2]) for row in data_list]


if __name__ == "__main__":
    print('~~~~~~~~~~~~~')
    # print(get_csv_data_as_dict('registerApiData.csv'))
    # print(get_data_as_list('registerApiDataWithStatus.csv'))

    keys = ['a', 'b', 'c', 'd']
    values = ['alpha', 'beta', 'delta']
    d = dict(zip(keys, values))
    print(d)
