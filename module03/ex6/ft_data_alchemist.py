#!/usr/bin/env python3
import random

initial_players = ['Alice', 'bob', 'Charlie', 'dylan',
                   'Emma', 'Gregory', 'john', 'kevin', 'Liam']

print("=== Game Data Alchemist ===")
print(f"Initial list of players: {initial_players}")

capitalized_all = [name.capitalize() for name in initial_players]
print(f"New list with all names capitalized: {capitalized_all}")

capitalized_only = [name for name in initial_players
                    if name == name.capitalize()]
print(f"New list of capitalized names only: {capitalized_only}")

score_dict = {name: random.randint(0, 1000) for name in capitalized_all}
print(f"Score dict: {score_dict}")

average_score = sum(score_dict.values()) / len(score_dict)
print(f"Score average is {average_score:.2f}")

high_scores = {name: score for name, score
               in score_dict.items() if score > average_score}
print(f"High scores: {high_scores}")
