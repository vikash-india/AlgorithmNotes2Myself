# Problem Analysis

### Concepts/Theories
* Divide & conquer algorithmic technique which involves the following steps
    - Divide the bigger problem into smaller sub problems.
    - Conquer the smaller sub problems individually.
    - Combine the results of conquered sub problems to get the final result.
* Permutation of n different things can be done in n! ways.

### Analysis
Let's consider the sequence [5, 9, 8, 2, 1] build a binary search tree using the following rules mentioned in the 
problem.

1. All the numbers in the sequence are distinct.
2. First number of the sequence becomes the root.
3. The bigger number goes to the left of the root.
4. The smaller number goes to the right of the root.

The sequence [5, 9, 8, 2, 1] will generated the following binary search tree.
<pre>
      5
     / \
    9   2
     \   \
      8   1
</pre>

Any of the following sequence will also generate the same tree shown above.

1. [5, 9, 8, 2, 1] - The original sequence.
2. [5, 9, 2, 8, 1]
3. [5, 9, 2, 1, 8]
4. [5, 2, 9, 8, 1]
5. [5, 2, 9, 1, 8]
6. [5, 2, 1, 9, 8]

Since there are 6 sequence combinations that yields the same binary search tree, the answer to this problem is 6.

#### Some Observations
1. If there is just one number in the sequence, there is only 1 combination to generate the same binary search tree.
2. If there are two numbers in the sequence, there is still only 1 combination to generate the same binary search tree.
3. If there are 3 or more numbers in the sequence, the first number becomes the root, rest can be further divided in two 
   groups of left sub tree and right sub tree.
4. Fixing 5 as the root, the [9, 8, 2, 1] can be arranged in 24 (ie 4!) ways. Out of those 24 ways only those 
   permutations will lead to the same binary search tree where 9 comes before 8 and 2 comes before 1. Hence the result 
   4! / (2 * 2). Half of the permutations will have 8 before 9 and the other half will have 9 before 8. Similarly half 
   of the permutation will have 2 before 1 and the other half will have 1 before 2.

#### Dividing Strategy
Take any sequence, make the first element as root and divide rest of the elements into left tree and right tree based on 
the value of the root element.

#### Conquering Strategy
If the sub problem has 2 or less than 2 elements then the result is 1. If the sub problem has more than 2 elements then
it should be further divided into smaller problems using the above Dividing Strategy.

#### Combining Strategy
Combining strategy is the most interesting part in this problem. It has two sub parts. 

#### 1. Combining the result of left_tree and right_tree at the same level l.
```
level_result = 
        factorial of (the number of elements in left_tree + the number of elements in right_tree) / 
        (factorial of the number of elements in left_tree * factorial of the number of elements 
        in right_tree)
 
Alternatively, 
level_result = (len(left_tree) + len(right_tree))! / (len(left_tree)! * len(right_tree)!)
```

This is like finding all the permutations of numbers in 2 lists such that the inherent order in each list is maintained 
in the resulting permutations.
 
Let's take an example of combining the list [9, 8] as the left_tree with the list [2, 1] as the right_tree. 

Any permutation/arrangement where 9 comes before 8 will result in the same left_tree. Similarly any permutation where
2 comes before 1 will result in the same right_tree. 

The combined permutation of the list [9, 8, 2, 1] will be the permutation where 9 always comes before 8 and 2 always 
comes before 1. This can be done in 4! / (2! * 2!). 

#### 2. Combining the level l result with the result computed for levels l+.
```
result = level_result * right_result * left_result
```

### Solution/Algorithm
<pre>
function answer([N<sub>1</sub>, N<sub>2</sub>, ..., N<sub>n</sub>])
    Input: 
        - A list of values [N<sub>1</sub>, N<sub>2</sub>, ..., N<sub>n</sub>] 
    Output: 
        - The total number of arrangements which generates the same binary search tree.
        
    1. left_tree, right_tree = divide([N<sub>1</sub>, N<sub>2</sub>, ..., N<sub>n</sub>])

    2. left_result = conquer(left_tree)
    3. right_result = conquer(right_tree)

    4. result = combine(left_tree, right_tree, left_result, right_result)

    5. return result


function divide([N<sub>1</sub>, N<sub>2</sub>, ..., N<sub>n</sub>])
    Input: 
        - A list of values [N<sub>1</sub>, N<sub>2</sub>, ..., N<sub>n</sub>]
    Output: 
        - Two list left_tree and right_tree such that left_tree has all elements greater than first 
          element and right_tree has all elements less than the first element.

    1. root = N<sub>1</sub>
    2. for i = N<sub>1</sub> to N<sub>n</sub>:
    3.     if N<sub>i</sub> < root:
    4.         Add N<sub>i</sub> to the right_tree.
    5.     else:
    6.         Add N<sub>i</sub> to the left_tree.

    7. return left_tree, right_tree


function conquer([N<sub>1</sub>, N<sub>2</sub>, ..., N<sub>n</sub>])
    Input: 
        - A list of seq values [N<sub>1</sub>, N<sub>2</sub>, ..., N<sub>n</sub>] 
    Output: 
        - The result for the smaller sub-problem.

    1. result = 1
    2. if n > 2:
    3.     result = answer([N<sub>1</sub>, N<sub>2</sub>, ..., N<sub>n</sub>)
    
    4. return result


function combine([L<sub>1</sub>, L<sub>2</sub>, ..., L<sub>m</sub>], [R<sub>1</sub>, R<sub>2</sub>, ..., R<sub>n</sub>], left_result, right_result)
    Input: 
        - A list of values [L<sub>1</sub>, L<sub>2</sub>, ..., L<sub>m</sub>] for the left tree.
        - A list of values [R<sub>1</sub>, R<sub>2</sub>, ..., R<sub>n</sub>] for the right tree.
        - An integer as the result of the left_tree till now.
        - An integer as the result of the right_tree till now.
    Output: 
        - An integer which is the combined result of the left_tree, the right_tree and the result 
          computed for the current level. 

    1. level_result = factorial(m + n) / (factorial(m) * factorial(n))
    2. result = level_result * right_result * left_result
    
    3. return result
</pre>

### Optimisation(s)
* Use memoization to speed up the computation of factorial.

### Complexity
* Worst case time complexity: NA
* Best case time complexity: NA
* Average case time complexity: NA
* Worst case space complexity: NA

### Reference(s)
- [None](#)

### Note
- None

### TODO
- None
