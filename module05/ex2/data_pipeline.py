#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any
import typing
from typing import Protocol

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

class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...

class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        output = ",".join(
            value
            for _, value in data
        )
        print(f"CSV Output: {output}")


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        output = ", ".join(
            f'"item_{key}": "{value}"'
            for key, value in data
        )
        print(f'JSON Output: {{{output}}}')
        
        

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
                    
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            data_to_export = []
            for _ in range(nb):
                try:
                    data_to_export.append(proc.output())
                except ValueError:
                    break
            plugin.process_output(data_to_export)
                
        
def main():
    print("=== Code Nexus - Data Pipeline ==="
          "Initialize the Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()
    print("Registering Processors\n")
    num: NumericProcessor = NumericProcessor()
    text: TextProcessor = TextProcessor()
    proc: LogProcessor = LogProcessor()
    stream.register_processor(num)
    stream.register_processor(text)
    stream.register_processor(proc)
    data: list[Any] = ['Hello world', [3.14, -1, 2.71],
                       [{'log_level': 'WARNING',
                         'log_message': 'Telnet access! Use ssh instead'},
                        {'log_level': 'INFO',
                         'log_message': 'User wil is connected'}],
                       42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {data}\n")
    stream.process_stream(data)
    stream.print_processors_stats()
    print()
    print("Send 3 processed data from each processor to a CSV plugin:")
    csvEXP = CSVExportPlugin()
    stream.output_pipeline(3, csvEXP)
    print()
    stream.print_processors_stats()
    new_data: list[Any] = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days',
            },
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello',
    ]
    print(f"Send another batch of data: {new_data}")
    stream.process_stream(new_data)
    stream.print_processors_stats()
    print("Send 5 processed data from each processor to a JSON plugin:")
    jsonEXP = JSONExportPlugin()
    stream.output_pipeline(5, jsonEXP)
    print()
    stream.print_processors_stats()
if __name__ == "__main__":
    main()