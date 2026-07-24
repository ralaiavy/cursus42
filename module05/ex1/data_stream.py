#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any
import typing

class DataProcessor(ABC):
    def __init__(self):
        self._data: list[str] = []
        self.ingested_count: int = 0
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
                self.ingested_count += 1
                self._data.append(str(data))
            elif isinstance(data, list):
                self.ingested_count += len(data)
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
                self.ingested_count += 1
                self._data.append(data)
            elif isinstance(data, list):
                self.ingested_count += len(data)
                for element in data:
                    self._data.append(element)
        else:
            raise ValueError("Got exception: Improper numeric data")
        
class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
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
                self.ingested_count += 1
                self._data.append(f"{data['log_level']}: {data['log_message']}")
            elif isinstance(data, list):
                self.ingested_count += len(data)
                for d in data:
                    self._data.append(f"{d['log_level']}: {d['log_message']}")
        else:
            raise ValueError("Got exception: Improper log data")
        

class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if isinstance(proc, DataProcessor):
            self.processors.append(proc)
        else:
            print("error type")
    
    def process_stream(self, stream: list[typing.Any]) -> None:
        for data in stream:
            processed = False
            for proc in self.processors:
                if proc.validate(data):
                    proc.ingest(data)
                    processed = True
                    break
            if not processed:
                print(
                    "DataStream error - Can't process element in stream:"
                    f" {data}"
                )
    
    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
        else:
            for proc in self.processors:
                print(
                    f"{type(proc).__name__}: "
                    f"total {proc.ingested_count} items processed, "
                    f"remaining {len(proc._data)} on processor"
                )     
    
    
def main():
    stream = DataStream()
    print("""=== Code Nexus - Data Stream ===
          Initialize Data Stream...""")
    stream.print_processors_stats()
    data_list: list[Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead',
            },
            {
                'log_level': 'INFO', 
                'log_message': 'User wil is connected'
            },
        ],
        42,
        ['Hi', 'five'],
    ]
    print("Registering Numeric Processor"
          f" Send first batch of data on stream: {data_list}")
    num = NumericProcessor()
    
    stream.register_processor(num)
    stream.process_stream(data_list)
    stream.print_processors_stats()
    
    print("\nRegistering other data processors")
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(text)
    stream.register_processor(log)
    print("Send the same batch again")
    stream.process_stream(data_list)
    stream.print_processors_stats()
    
    print(
        "\nConsume some elements from the data processors:"
        " Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        try:
            num.output()
        except Exception as e:
            print(e)
    for _ in range(100000):
        try:
            text.output()
        except Exception as e:
            print(e)
    try:
        log.output()
    except Exception as e:
        print(e)
    stream.print_processors_stats()

if __name__ == "__main__":
    main()