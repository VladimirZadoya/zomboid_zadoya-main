from pathlib import Path
from src.file_readers import CSVFileReader, JSONFileReader


if __name__ == "__main__":
    usr_csv = Path(".data/model.csv")
    usr_json = Path(".data/model.json")
    csv_reader = CSVFileReader(usr_csv)
    json_reader = JSONFileReader(usr_json)
    print(csv_reader.read())
    