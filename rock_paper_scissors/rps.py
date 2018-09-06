#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    #return an array
    allPossibilities = []
    #possible plays list
    options = ['rock', 'paper', 'scissors']
    def generate_plays(rounds_left, result=[]):
        if rounds_left == 0:
            allPossibilities.append(result)
            return
        for option in options:
            generate_plays(rounds_left - 1, result + [option])

    generate_plays(n, [])
    return allPossibilities


if __name__ == "__main__":
  # Test out your implementation from the command line
  # with `python rps.py [n]` with different n values
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
