# bubble_sort

A [bubble sort](https://en.wikipedia.org/wiki/Bubble_sort)  is a sorting algorithm that iterates through a list of numbers, comparing neighboring pairs. If the first number is greater than the second, the algorithm swaps their positions and moves on to the next pair. If the first number is less than the second, the algorithm moves on to the next pair without making any changes.

The algorithm continues this process, looping through the array until there are no more changes to make.


```py
initialList = [1, 4, 2, 3]

bubble_sort(initial_list) # [1,2,3,4]

# the algorithm starts at the beginning of the array
1 > 4? # no, move on

[1,4,3,2]
4 > 3? # yes, switch them

[1,3,4,2]
4 > 2? # yes, switch them

[1,3,2,4]
# loop through again

1 > 3? # no, move on
[1,3,2,4]

3 > 2? # yes, switch them
[1,2,3,4]

3 > 4? # no, move on
[1,2,3,4]

# no more changes to make
finalList = [1, 2, 3, 4]
```
