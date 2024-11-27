# Class diagram

```mermaid
classDiagram
class AbstractReader{
    -__init__(self)
    -read(self) -> list[Any]
}
class FileReader{
    -__init__(self, path: Path)
    +Path file_path
}
class CSVFileReader{
    -__init__(self, path: Path)
    +file_path: Path 
    +self.data: list[dict[str, str | int]] 
    -read(self) -> list[list[str]]
}
class JSONFileReader{
    -__init__(self, path: Path)
    +file_path: Path 
    +self.data: list[dict[str, str | int]] 
    -read(self) -> list[dict[str, str | int]]
}
class ConsolePrinter{
    -__init__(self, data)
    +self.data: list[dict[str, str | int]
    -print_all(self) -> None
    -print_paginated(self, page: int, items_per_page: int) -> None
}
class itemSearcher{
    -__init__(self, data)
    +self.data: list[dict[str, str | int]
    -find_by_id(self, item_id: int) -> dict[str, str | int]
    -find_by_name(self, name: str) -> list[dict[str, str | int]]
}
AbstractReader <|-- FileReader
FileReader <|-- CSVFileReader
FileReader <|-- JSONFileReader
```
