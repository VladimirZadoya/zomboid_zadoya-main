import json
import csv
from pathlib import Path
from abc import ABC, abstractmethod
from typing import Any


class AbstractReader(ABC):
    def __init__(self):
        pass
        
    @abstractmethod
    def read(self) -> list[Any]:
        pass

class FileReader(AbstractReader):
    def __init__(self, path: Path):
        self.file_path = path


class CSVFileReader(FileReader):
    def __init__(self, path: str):
        self.file_path = path
        self.data: list[dict[str, str | int]] = []

    def read(self) -> list[dict[str, str | int]]:
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Нормалізація ключів до нижнього регістру та обробка значень
                    normalized_row = {
                        key.lower(): self._convert_value(value) for key, value in row.items()
                    }
                    self.data.append(normalized_row)
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except Exception as e:
            print(f"Error reading CSV file: {e}")
        return self.data


class JSONFileReader(FileReader):
    def __init__(self, path: str):
        self.file_path = path
        self.data: list[dict[str, str | int]] = []

    def read(self) -> list[dict[str, str | int]]:
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                loaded_data = json.load(file)
                if not isinstance(loaded_data, list):
                    raise ValueError("The JSON file must contain a list of objects.")
                for entry in loaded_data:
                    if isinstance(entry, dict) and all(isinstance(v, (str, int)) for v in entry.values()):
                        # Нормалізація ключів до нижнього регістру
                        normalized_entry = {key.lower(): value for key, value in entry.items()}
                        self.data.append(normalized_entry)
                    else:
                        raise ValueError("JSON entries must be dictionaries with string or integer values.")
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except json.JSONDecodeError:
            print(f"File {self.file_path} contains invalid JSON.")
        except Exception as e:
            print(f"Error reading JSON file: {e}")
        return self.data