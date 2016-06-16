# Problem Analysis

### Concepts/Theories
* Arrays: Array insertion and array search.

### Analysis
Let's take a few examples and explore the problem based on the following rules,

1. There's an array/list with the number of elements between 2 and 5000, both inclusive.
2. The search for a loop starts at the 0th index. 
3. The value at any index in the array redirects to another index in the array. No index redirects to itself.
4. There is a guaranteed loop.

#### Example 1
Let numbers be an array with values [1, 7, 1, 4, 5, 0, 7, 6]. According to the problem, we have to start by visiting the 
0th index of the array, numbers[0], which in turn will redirect us to the next pirate. The value number[0] = 1 means 
the 0th pirate redirects us to pirate at index 1 ie numbers[1]. This goes on till a loop is detected.

Let's keep track of all the pirates who have already been explored using another list pirates_explored. Initially the  
pirates_explored is an empty list.

We start with numbers = [1, 7, 1, 4, 5, 0, 7, 6] and explored_pirates = []

- numbers[0] redirects to 1. pirates_explored = [0].
- numbers[1] redirects to 7. pirates_explored = [0, 1].
- numbers[7] redirects to 6. pirates_explored = [0, 1, 7].
- numbers[6] redirects to 7. pirates_explored = [0, 1, 7, 6]

Since 7 is already explored we have found our loop in [7, 6] of [0, 1, 7, 6]. Hence the answer is 2. 

#### Example 2
Let numbers be an array with values [5, 9, 5, 1, 6, 3, 6, 7, 2, 3, 0, 1]. According to the problem, we have to start by 
visiting the 0th index of the array, numbers[0], which in turn will redirect us to the next pirate. The value 
number[0] = 5 means the 0th pirate redirects us to pirate at index 5 ie numbers[5]. This goes on till a loop is detected.

We start with numbers = [5, 9, 5, 1, 6, 3, 6, 7, 2, 3, 0, 1] and explored_pirates = []

- numbers[0] redirects to 5. pirates_explored = [0]. 
- numbers[5] redirects to 3. pirates_explored = [0, 5]
- numbers[3] redirects to 1. pirates_explored = [0, 5, 3]
- numbers[1] redirects to 9. pirates_explored = [0, 5, 3, 1]
- numbers[9] redirects to 3. pirates_explored = [0, 5, 3, 1, 9] 

Since 3 is already explored, we have found our loop in [3, 1, 9] of [0, 5, 3, 1, 9]. Hence the answer is 3.

#### Example 3
We start with numbers = [5, 9, 5, 1, 6, 3, 6, 7, 2, 3, 0, 1] and explored_pirates = []

- numbers[0] redirects to 5. pirates_explored = [0]. 
- numbers[5] redirects to 3. pirates_explored = [0, 5]
- numbers[3] redirects to 1. pirates_explored = [0, 5, 3]
- numbers[1] redirects to 9. pirates_explored = [0, 5, 3, 1]
- numbers[9] redirects to 3. pirates_explored = [0, 5, 3, 1, 9] 

Since 3 is already explored, we have found our loop in in [3, 1, 9] of [0, 5, 3, 1, 9]. Hence the answer is 3.

### Solution/Algorithm
<pre>
    function answer(numbers)
        Input: 
            - (int list) numbers = A list of sitting order of pirates in the bar.
        Output: 
            - (int) The number of pirates who form a loop.
    
        1. pirates_explored = []
        2. i = 0
           
        3. while True: # Infinite loop is fine since the problem guarantees a loop.
        4.      if i is already present in pirates_explored:
        5.          return the length of that portion of the pirates_explored which forms the loop.
                
        6.      Add the pirate i to pirates_explored list
    
        7.      Set i to the pirate which it was redirected
</pre>

### Optimisation(s)
* NA

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
