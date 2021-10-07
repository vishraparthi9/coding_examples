#!/usr/bin/env python3

import sys
###
## The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
## 1) The subarray which is already sorted. 
## 2) Remaining subarray which is unsorted.
## In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray. 
### Following example explains the above steps: 
#### arr[] = 64 25 12 22 11

#### // Find the minimum element in arr[0...4] and place it at beginning
#### 11 25 12 22 64

#### // Find the minimum element in arr[1...4] and place it at beginning of arr[1...4]
#### 11 12 25 22 64

#### // Find the minimum element in arr[2...4] and place it at beginning of arr[2...4]
#### 11 12 22 25 64

#### // Find the minimum element in arr[3...4] and place it at beginning of arr[3...4]
#### 11 12 22 25 64 
###

def selection_sort(elements):

  for i in range(len(elements)):
    minimum_position = i
    minimum = elements[i]
    for j in range(i+1, len(elements)):
      if elements[j] < minimum:
        minimum_position = j
        minimum = elements[j]

    elements[i], elements[minimum_position] = elements[minimum_position], elements[i]

  return

if __name__=="__main__":
  elements = [ int(x) for x in sys.argv[1:] ]
  selection_sort(elements)
  print("After sorting: ", elements)