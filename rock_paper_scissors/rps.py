#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    allPossibilities = []
    options = ['rock', 'paper', 'scissors']
    def build_permutations(round, roundNumber):
        for i in range(0, len(options)):
            round.append(options[i])
            print('roudn', round)
            if n == roundNumber:
                return allPossibilities.append(round)
            else:
                build_permutations(round, roundNumber + 1)
            round.pop(len(round)-1)
    build_permutations([], 1)
    return allPossibilities



if __name__ == "__main__":
  # Test out your implementation from the command line
  # with `python rps.py [n]` with different n values
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
