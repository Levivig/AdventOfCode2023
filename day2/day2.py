#!/usr/bin/env python3
# coding: utf-8


import os
import time


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def part1(data):
    print('part1:')
    
    validGames = []
    for line in data:
        gameId = int(line.split(":")[0].split(" ")[-1])
        valid = True
        for draw in line.split(":")[1].split(";"):
            for cubes in draw.split(","):
                if not checkIfValid(cubes):
                    valid = False
                    break

        if valid:
            validGames.append(gameId)

    print(sum(validGames))


def checkIfValid(cubes):
    red = 12
    green = 13
    blue = 14

    cubes = cubes.strip()
    count = int(cubes.split(" ")[0])
    name = cubes.split(" ")[1]

    if name == "red" and count > red:
        return False
    if name == "green" and count > green:
        return False
    if name == "blue" and count > blue:
        return False
    
    return True
    

def part2(data):
    print('part2:')
    powers = []
    for line in data:
        redMin = 0
        greenMin = 0
        blueMin = 0
        for draw in line.split(":")[1].split(";"):
            for cubes in draw.split(","):
                (redMin,greenMin, blueMin) = findMin(cubes, redMin, greenMin, blueMin)

        powers.append(redMin * greenMin * blueMin)

    print(sum(powers))


def findMin(cubes, redMin, greenMin, blueMin):
    cubes = cubes.strip()
    count = int(cubes.split(" ")[0])
    name = cubes.split(" ")[1]
    if name == "red" and count > redMin:
        redMin = count
    if name == "green" and count > greenMin:
        greenMin = count
    if name == "blue" and count > blueMin:
        blueMin = count
    
    return (redMin, greenMin, blueMin)


def main():
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)
    with open(inputfile) as f:
        data = f.read().splitlines()
        part1(data) # 2406
        part2(data) # 78375


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
