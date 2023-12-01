#!/usr/bin/env python3
# coding: utf-8


import os
import time


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def part1(data):
    print('part1:')
    total = 0
    for line in data:
        total += solve(line)

    print(total)


def part2(data):
    print('part2:')
    total = 0
    for line in data:
        line = find_and_combine_first_last_numbers(line)
        total += solve(line)

    print(total)


def solve(line):
    numbers = []
    for c in line:
        if c.isnumeric():
            numbers.append(int(c))

    if numbers:
        res = int("{}{}".format(numbers[0], numbers[-1]))
        return res
    return 0


def find_and_combine_first_last_numbers(s):
    num_words = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    first_number = None
    last_number = None

    # Find the first number or number word
    for i in range(len(s)):
        for word, digit in num_words.items():
            if s[i:i+len(word)] == word:
                first_number = digit
                break
        if first_number or s[i].isdigit():
            first_number = first_number if first_number else s[i]
            break

    # Find the last number or number word
    for i in range(len(s) - 1, -1, -1):
        for word, digit in num_words.items():
            if i - len(word) + 1 >= 0 and s[i-len(word)+1:i+1] == word:
                last_number = digit
                break
        if last_number or s[i].isdigit():
            last_number = last_number if last_number else s[i]
            break

    return first_number + last_number if first_number and last_number else None


def main():
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)
    with open(inputfile) as f:
        data = f.read().splitlines()
        part1(data) # 53194
        part2(data) # 54249


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
