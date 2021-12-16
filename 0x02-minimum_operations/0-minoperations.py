#!/usr/bin/python3
"""FIle that uses the min of operations"""


def minOperations(n):
  """given a number n, this method calculates the fewest name of operations"""

  CopyPaste = 2
  Paste = 1
  Htotal = 1
  Previoush = 1
  numofops = 0

  if n <= 1:
      return 0

  while Htotal < n:
      if Htotal == 1:
          numofops += CopyPaste
          Htotal = Htotal + Htotal
      elif n % Htotal == 0 and Htotal * 2 <= n:
          numofops += CopyPaste
          Previoush = Htotal
          Htotal = Htotal + Htotal
      else:
          Htotal += Previoush
          numofops += Paste
  return numofops
