"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Yelp.

Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].

"""
import itertools

d = {"2":["a","b","c"], "3": ["d", "e", "f"], "4":["g", "k", "k"]}

lists = []
for key in d:
    lists.append(d[key])

result = ["".join(a) for a in list(itertools.product(*lists))]
print(result)
