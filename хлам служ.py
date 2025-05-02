import sys
from sys import stdin
import json

json_name = 'scoring.json'

with open(json_name) as file:
    data = json.load(file)

answers = [x.strip("\n") for x in sys.stdin.readlines()]

score = 0

for test in data:
    i = test["points"] // len(test["tests"])
    for answer in answers:
        for t in test["tests"]:
            if t["pattern"] == answer:
                score += i
print(score)
