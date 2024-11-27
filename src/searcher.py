class ItemSearcher:
    def __init__(self, data: list[dict[str, str | int]]):
        self.data = data

    def find_by_id(self, item_id: int) -> dict[str, str | int]:
        for item in self.data:
            if int(item['ID']) == item_id:
                return item
        raise ValueError(f"Item with ID {item_id} not found.")

    def find_by_name(self, name: str) -> list[dict[str, str | int]]:
        return [item for item in self.data if item['Name'].lower() == name.lower()]
