#!/usr/bin/env python3

def preprocessing(pat):

  # This constructs lps array
  # lps: longest proper prefix which is also suffix
  # proper prefix of "ABC" is "", "A", and "AB" and NOT "ABC"
  # proper suffix of "ABC" is "", "C", and "BC"

  pat_len = len(pat)
  lps = [0] * pat_len

  for i in range(pat_len):
    cur = pat[0:i+1]
    cur_len = len(cur)
    for j in range(cur_len):
      if cur[0:j] == cur[cur_len-j:cur_len]:
        if len(cur[0:j]) > lps[i]:
          lps[i] = len(cur[0:j])

  return lps

def searchForPattern(lps, pat, txt):

  i = 0
  j = 0

  while i < len(txt):

    if txt[i] == pat[j]:
      i = i + 1
      j = j + 1
    else:
      if j > 0:
        j = lps[j-1]
      elif j == 0:
        i = i + 1

    if j == len(pat):
      return i - j

  return -1

if __name__=="__main__":

  pat = "code"
  txt = "lecodletcodecode"
  lps = preprocessing(pat)
  print(searchForPattern(lps, pat, txt))