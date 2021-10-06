#!/usr/bin/env python3

import sys

## Quick sort - pivot
## Recursive algo
## A pivot is simply one of the elements - usually the first or last element
## Select a "low" and "high" - usually the second element and the last element respectively
## Increment "low" till you find a value greater than pivot and stop it there
## Decrement "high" till you find a value lower than pivot
## Swap the position of values for both low and high and continue
## Once the high < low, swap high with pivot and then break into partitions
### In this exercise, during the initial iteration:
####  arr[0] - pivot, arr[1] - low, len(arr)-1: high

def partition(elements, low, high, pivot_element):
  if pivot_element == "first":
    pivot = low - 1
  elif pivot_element == "last":
    pivot = high + 1
  
  while True:

    ## Move low until you find a number greater than pivot
    while elements[low] < elements[pivot]:
      low = low + 1
      if low >= high: break

    ## Move high until you find a number less than pivot
    ## high>low is required so as to not decrement when low
    ## and high are the same
    while elements[high] > elements[pivot]:
      if (pivot_element == "last" and high > low) or (pivot_element == "first"):
        high = high - 1
      if high <= low: break

    if high <= low:
      elements[high], elements[pivot] = elements[pivot], elements[high]
      return high
    else:
      elements[high], elements[low] = elements[low], elements[high]


def quick_sort(elements, low, high, pivot_element):
  if low <= high:
    pivot_position = partition(elements, low, high, pivot_element)

    if pivot_element == "first":
      quick_sort(elements, low, pivot_position-1, pivot_element)
      quick_sort(elements, pivot_position+2, high, pivot_element)
    elif pivot_element == "last":
      quick_sort(elements, low, pivot_position-2, pivot_element)
      quick_sort(elements, pivot_position+1, high, pivot_element)


if __name__=="__main__":
  elements = [ int(x) for x in sys.argv[1:] ]
  #print(elements)
  #quick_sort(elements, 1, len(elements)-1, "first")
  quick_sort(elements, 0, len(elements)-2, "last")
  print("After sorting:", elements)