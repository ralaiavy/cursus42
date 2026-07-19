#!/usr/bin/env python3
import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["bob", "alice", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab",
               "move", "climb", "swim", "use", "release"]

    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
    event_list: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    while event_list:
        random_index = random.randint(0, len(event_list) - 1)
        event = event_list[random_index]
        del event_list[random_index]
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    event_generator = gen_event()

    for i in range(1000):
        name, action = next(event_generator)
        print(f"Event {i}: Player {name} did action {action}")

    print("\nBuilt list of 10 events:", end=" ")
    event_generator = gen_event()
    list_of_events = [next(event_generator) for _ in range(10)]
    print(list_of_events)

    print()
    for event in consume_event(list_of_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {list_of_events}")
        print()
