import os
import json
import csv
from typing import List, Dict
from pathlib import Path


import argparse
import json
import csv
from pathlib import Path
from typing import List, Dict


class FileHandler:
    
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.data = self._read_file()

    def _read_file(self) -> List[Dict]:
        if not self.file_path.exists():
            raise FileNotFoundError(f"Файл '{self.file_path}' не существует.")
        
        if self.file_path.suffix == ".json":
            return self._read_json()
        elif self.file_path.suffix == ".csv":
            return self._read_csv()
        elif self.file_path.suffix == ".xml":
            return self._read_xml()
        else:
            raise ValueError(f"Неподдерживаемый формат файла: {self.file_path.suffix}")

    def _read_json(self) -> List[Dict]:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _read_csv(self) -> List[Dict]:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)

    def _read_xml(self) -> List[Dict]:
        import xml.etree.ElementTree as ET
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        return [{child.tag: child.text for child in elem} for elem in root]


class DataAnalyzer:
    
    def __init__(self, data: List[Dict]):
        self.data = data

    def get_condition_percentages(self, filter_name: str = None) -> Dict[str, float]:
        filtered_data = [item for item in self.data if (not filter_name or item.get("name") == filter_name)]
        total_items = len(filtered_data)
        
        if total_items == 0:
            return {}

        condition_count = {}
        for item in filtered_data:
            condition = item.get("condition")
            condition_count[condition] = condition_count.get(condition, 0) + 1

        return {condition: (count / total_items) * 100 for condition, count in condition_count.items()}


def print_percentage_results(results: Dict[str, float], filter_name: str = None):
    if filter_name:
        print(f"Проценты по условиям для предметов с именем '{filter_name}':")
    else:
        print("Проценты по условиям для всех предметов:")
    
    for condition, percentage in results.items():
        print(f"{condition}: {percentage:.2f}%")


def main():
    parser = argparse.ArgumentParser(description="Анализ данных из файла.")
    parser.add_argument("file_path", type=Path, help="Путь к файлу (JSON, CSV, XML).")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--percentage-all", action="store_true", help="Показать проценты по условиям для всех предметов.")
    group.add_argument("--percentage-name", type=str, help="Показать проценты по условиям для предметов с указанным именем.")

    args = parser.parse_args()

    try:
        file_handler = FileHandler(args.file_path)
        analyzer = DataAnalyzer(file_handler.data)

        if args.percentage_all:
            results = analyzer.get_condition_percentages()
            print_percentage_results(results)

        if args.percentage_name:
            results = analyzer.get_condition_percentages(args.percentage_name)
            print_percentage_results(results, args.percentage_name)

    except (FileNotFoundError, ValueError) as e:
        print(f"Ошибка: {e}")
        exit(1)

if __name__ == "__main__":
    main()
