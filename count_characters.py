from collections import Counter


def my_count(string):
    return {c: string.count(c) for c in set(string)}


def top_count(string):
    return Counter(string)