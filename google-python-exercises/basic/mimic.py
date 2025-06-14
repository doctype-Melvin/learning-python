#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

# Google's Python Class
# http://www.apache.org/licenses/LICENSE-2.0
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  mimic_dict = {}
  
  read_file = open(filename, encoding='utf-8')
  full_string = read_file.read()
  full_split = full_string.split()
  read_file.close()

  current = ''
  
  for word in full_split:
    if not current in mimic_dict:
      mimic_dict[current] = [word]
    else:
      mimic_dict[current].append(word)
    current = word
  
  return  mimic_dict

  """
  # this is a quite complex solution
  # why: I've used a while loop and an iterator variable i
  # to track the current word (i) and the next word (i+1)
  # this does not include the empty string to initialise
  # the dictionary 

  for string in full_split:
    giant_string.append(string.lower())

  i = 0

  while i < len(giant_string):
    if (i+1 < len(giant_string)):
      if not giant_string[i] in mimic_dict:
        mimic_dict[giant_string[i]] = [giant_string[i+1]]
        i += 1
      else:
        mimic_dict[giant_string[i]].append(giant_string[i+1])
        i += 1
    else:
      i += 1
  print(i)
  """


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # set range to 200 iterations = 200 words
  for i in range(200):
    # replace line break with space at end of string
    print(word, end=' ')
    # find the list associated with the word from mimic_dict
    str_list = mimic_dict.get(word)
    # in any case where there is no list 
    if not str_list:
      # get the list of the empty string
      str_list = mimic_dict.get('')
      # the next word is chosen randomly from the list
    word = random.choice(str_list)

# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
