#!/usr/bin/env python3
import sys

###
# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements 
# if they are in wrong order.
###
## Example: 
### First Pass: 
####( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1. 
####( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4 
####( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2 
####( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), 
#### algorithm does not swap them.
### Second Pass: 
####( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ) 
####( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2 
####( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 
####( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 ) 
### Now, the array is already sorted, but our algorithm does not know if it is completed. 
### The algorithm needs one whole pass without any swap to know it is sorted.
### Third Pass: 
####( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 
####( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 
####( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 
####( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 


def bubble_sort(elements, low, high):

  if low == high:
    return

  for x in range(low, high):
    if elements[x] > elements[x+1]:
      elements[x], elements[x+1] = elements[x+1], elements[x]

  print(elements)
  bubble_sort(elements, 0, high-1)

if __name__=="__main__":
  elements = [ int(x) for x in sys.argv[1:] ]
  bubble_sort(elements, 0, len(elements)-1)
  print("After sorting: ", elements)