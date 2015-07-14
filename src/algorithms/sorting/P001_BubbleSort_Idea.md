# Description: Bubble Sort Algorithm

### Bubble Sort
- Bubble sort, (aka sinking sort), is a simple sorting algorithm that repeatedly steps through the list to be sorted,
  compares each pair of adjacent items and swaps them if they are in the wrong order.
- The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.
- Bubble sort is an internal sort where the sorting process takes place entirely within the main memory of a computer.
  This is possible whenever the data to be sorted is small enough to all be held in the main memory.
- It is too slow and impractical for most problems even when compared to insertion sort.
- It can be practical if the input is usually in sort order but may occasionally have some out-of-order elements nearly
  in position.
- The only significant advantage that bubble sort has over most other implementations, including quicksort, but not
  insertion sort, is that the ability to detect that the list is sorted is efficiently built into the algorithm.

### Rabbits and Turtles
- Large elements at the beginning of the list do not pose a problem, as they are quickly swapped. Small elements towards
  the end, however, move to the beginning extremely slowly. This has led to these types of elements being named rabbits
  and turtles, respectively.
- Various efforts have been made to eliminate turtles to improve upon the speed of bubble sort. Cocktail sort is a
  bi-directional bubble sort that goes from beginning to end, and then reverses itself, going end to beginning. It can
  move turtles fairly well, but it retains O(n<sup>2</sup>) worst-case complexity.
- Comb sort compares elements separated by large gaps, and can move turtles extremely quickly before proceeding to
  smaller and smaller gaps to smooth out the list. Its average speed is comparable to faster algorithms like quicksort.

### Variations
- Odd-even sort is a parallel version of bubble sort, for message passing systems.
- Cocktail sort is another parallel version of the bubble sort.
- In some cases, the sort works from right to left (the opposite direction), which is more appropriate for partially
  sorted lists, or lists with unsorted items added to the end.

### Algorithm
* Input(s)
    - A List of Unsorted Numbers.
* Output
    - A List of SORTED numbers.
* Algorithm
    1. Get a list of unsorted numbers.
    2. Compare each pair of adjacent elements from the beginning of the list, and, if they are in reverse order, swap
       them.
    3. If at least one swap has been made, repeat Step 1.
    4. Stop.

### Optimisation(s)
1. The bubble sort algorithm can be easily optimised by observing that the n-th pass finds the n-th largest element and
   puts it into its final place. So, the inner loop can avoid looking at the last n-1 items when running for the n-th
   time.

### Complexity
- Worst case time complexity is O(n<sup>2</sup>) where n is the number of items being sorted.
- Best case time complexity is  O(n) where n is the number of items being sorted.
- Average case time complexity is O(n<sup>2</sup>) where n is the number of items being sorted.
- Worst case space complexity is O(1).

### Interesting URLs
- [Bubble Sort Animations](http://www.cs.armstrong.edu/liang/animation/web/BubbleSort.html)
- [Animations of Sorting Algorithms - 1](http://sorting.at/)
- [Animations of Sorting Algorithms - 2](http://www.sorting-algorithms.com/)
- [Data Structure Visualisations](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)

### TODO
- None
