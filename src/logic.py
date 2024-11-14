"""App logic"""
from pathlib import Path
import pandas as pd

DIR_PATH = Path(__file__).parent.parent.parent.parent
INPUT_DIR = DIR_PATH / "InputFiles"
OUTPUT_DIR = DIR_PATH / "OutputFiles"
INPUT_FILE = fr"{INPUT_DIR}\names.txt"

def read_file():
    """
    Reads the input text file and returns its contents as a list of strings.

    Returns:
        list: A list of strings where each element is a line from the file,
              stripped of leading/trailing whitespace.
    """
    with open(INPUT_FILE, "r") as f:
        return [item.strip() for item in f.readlines()]


def convert_to_dict(data) -> dict:
    """
        Converts a list of strings into a dictionary, counting occurrences of each string.

        Args:
            data (list): A list of strings.

        Returns:
            dict: A dictionary with strings as keys and their respective counts as values.
    """
    result = {}
    for item in data:
        if item in result:
            result[item] += 1
        else:
            result[item] = 0
    return result


def save_dict_to_file(data: dict) -> None:
    """
       Saves a dictionary to both CSV and Excel files in the output directory.

       Args:
           data (dict): A dictionary with strings as keys and integers as values,
                        representing the count of each string.

       Returns:
           None
   """
    df = pd.DataFrame.from_dict(data, orient="index")
    df.to_csv(fr"{OUTPUT_DIR}\result.csv")
    df.to_excel(fr"{OUTPUT_DIR}\result.xlsx")