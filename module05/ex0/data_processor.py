#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any
import typing

class DataProcessor(ABC):
    def __init__(self):
        self._data: list[str] = []
        self._rank: int = 0
        

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass
    def output(self) -> tuple[int, str]:
        if not self._data:
            raise ValueError("No data to extract")
        outp = (self._rank, str(self._data[0]))
        self._rank += 1
        self._data.pop(0)
        return outp
        


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, int) or isinstance(data, float):
            return True
        if isinstance(data, list):
            if not data:
                return False
            return all(isinstance(element, (int, float)) for element in data)
        return False
    
    def ingest(self, data: int | float | list[int] | list[float]) -> None:
        if self.validate(data):
            if isinstance(data, int) or isinstance(data, float):
                self._data.append(str(data))
            elif isinstance(data, list):
                for element in data:
                    self._data.append(str(element))
        else:
            raise ValueError("Got exception: Improper numeric data")
        
        
class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            if not data:
                return False
            return True
        if isinstance(data, list):
            if not data:
                return False
            return all(isinstance(element, str) for element in data)
        return False
    
    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data):
            if isinstance(data, str):
                self._data.append(data)
            elif isinstance(data, list):
                for element in data:
                    self._data.append(element)
        else:
            raise ValueError("Got exception: Improper numeric data")
        
class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            if not data:
                return False
            return all(isinstance(key, str) and isinstance(value, str)
                       for key, value in data.items())
        if isinstance(data, list):
            if not data:
                return False
            return all(self.validate(item) for item in data)
        return False
    
    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if self.validate(data):
            if isinstance(data, dict):
                self._data.append(f"{data['log_level']}: {data['log_message']}")
            elif isinstance(data, list):
                for d in data:
                    self._data.append(f"{d['log_level']}: {d['log_message']}")
        else:
            raise ValueError("Got exception: Improper log data")
            
def main():
    print("=== Code Nexus - Data Processor ===\n")
    n = NumericProcessor()
    t = TextProcessor()
    l = LogProcessor()
    numbers: list[int] = [1, 2, 3, 4, 5]
    words: list[str] = ["Hello", "Nexus", "World"]
    logs: list[dict[str, str]] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'},
    ]
    print("Testing Numeric Processor...")
    print(f"Trying to validate input '42': {n.validate(42)}")
    print(f"Trying to validate input 'Hello': {n.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        n.ingest("foo")
    except Exception as e:
        print(e)
    print(f"Processing data:{numbers}")
    print("Extracting 3 values...")
    n.ingest(numbers)
    for _ in range(3):
        try:
            rank, value = n.output()
            print(f"Numeric value {rank}: {value}")
        except Exception as e:
            print(e)
    print("Testing Text Processor...")
    print(f"Trying to validate input '42': {t.validate(42)}")
    print(f"Processing data: {words}")
    print("Extracting 1 value...")
    t.ingest(words)
    t_rank, t_value = t.output()
    print(f"Text value {t_rank}: {t_value}")
    print("Testing Log Processor...")
    print(f"Trying to validate input 'Hello': {l.validate('Hello')}")
    print(f"Processing data: {logs}")
    print("Extracting 2 values...")
    l.ingest(logs)
    for _ in range(2):
        l_rank, l_value = l.output()
        print(f"Log entry {l_rank}: {l_value}")


    
    
if __name__ == "__main__":
    main()