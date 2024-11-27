class ConsolePrinter:
    def __init__(self, data: list[dict[str, str | int]]):
        self.data = data

    def print_all(self) -> None:
        for item in self.data:
            print(f"ID: {item['id']}, Name: {item['name']}, "
                  f"Type: {item['type']}, Condition: {item['condition']}, "
                  f"Amount: {item['amount']}")

    def print_paginated(self, page: int, items_per_page: int = 10) -> None:
        start = (page - 1) * items_per_page
        end = start + items_per_page
        for item in self.data[start:end]:
            print(f"ID: {item['id']}, Name: {item['name']}, "
                  f"Type: {item['type']}, Condition: {item['condition']}, "
                  f"Amount: {item['amount']}")
