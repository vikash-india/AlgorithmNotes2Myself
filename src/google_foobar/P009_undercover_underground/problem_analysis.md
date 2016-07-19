# Problem Analysis

### Concepts/Theories
* None

### Analysis

#### Case 1: N = 2, K = 1, Answer = 1
* Nodes = ['A', 'B']
* Edges = ['AB']
* [Graph Visualisation](problem_analysis_graph_01_2X1.png) with following edges.

```
'AB'
```

#### Case 2: N = 3, K = 2, Answer = 3
* Nodes = ['A', 'B', 'C']
* Edges = ['AB', 'BC', 'CA']
* [Graph Visualisation](problem_analysis_graph_02_3X2.png) with following edges.

```
'AB', 'BC'
'AB', 'CA'
'BC', 'CA'
```

#### Case 3: N = 3, K = 3, Answer = 1
* Nodes = ['A', 'B', 'C']
* Edges = ['AB', 'BC', 'CA']
* [Graph Visualisation](problem_analysis_graph_03_3X3.png) with following edges.

```
'AB', 'BC', 'CA'
```

#### Case 4: N = 4, K = 3, Answer = 16
* Nodes = ['A', 'B', 'C', 'D']
* Edges = ['AB', 'BC', 'CD', 'DA', 'AC', 'BD']
* [Graph Visualisation](problem_analysis_graph_04_4X3.png) with following edges.

```
'AB', 'BC', 'CD'
'AB', 'BC', 'DA'
'AB', 'BC', 'AC' ------------------------- Vertex D is isolated!
'AB', 'BC', 'BD'
'AB', 'CD', 'DA'
'AB', 'CD', 'AC'
'AB', 'CD', 'BD'
'AB', 'DA', 'AC'
'AB', 'DA', 'BD' ------------------------- Vertex C is isolated!
'AB', 'AC', 'BD'
'BC', 'CD', 'DA'
'BC', 'CD', 'AC'
'BC', 'CD', 'BD' ------------------------- Vertex A is isolated!
'BC', 'DA', 'AC'
'BC', 'DA', 'BD'
'BC', 'AC', 'BD'
'CD', 'DA', 'AC' ------------------------- Vertex B is isolated!
'CD', 'DA', 'BD'
'CD', 'AC', 'BD'
'DA', 'AC', 'BD'
```

#### Case 5: N = 4, K = 4, Answer = 15
* Nodes = ['A', 'B', 'C', 'D']
* Edges = ['AB', 'BC', 'CD', 'DA', 'AC', 'BD']
* [Graph Visualisation](problem_analysis_graph_05_4X4.png) with following edges.

```
'AB', 'BC', 'CD', 'DA'
'AB', 'BC', 'CD', 'AC'
'AB', 'BC', 'CD', 'BD'
'AB', 'BC', 'DA', 'AC'
'AB', 'BC', 'DA', 'BD'
'AB', 'BC', 'AC', 'BD'
'AB', 'CD', 'DA', 'AC'
'AB', 'CD', 'DA', 'BD'
'AB', 'CD', 'AC', 'BD'
'AB', 'DA', 'AC', 'BD'
'BC', 'CD', 'DA', 'AC'
'BC', 'CD', 'DA', 'BD'
'BC', 'CD', 'AC', 'BD'
'BC', 'DA', 'AC', 'BD'
'CD', 'DA', 'AC', 'BD'
```

#### Case 6: N = 4, K = 5, Answer = 6
* Nodes = ['A', 'B', 'C', 'D']
* Edges = ['AB', 'BC', 'CD', 'DA', 'AC', 'BD']
* [Graph Visualisation](problem_analysis_graph_06_4X5.png) with following edges.

```
'AB', 'BC', 'CD', 'DA', 'AC'
'AB', 'BC', 'CD', 'DA', 'BD'
'AB', 'BC', 'CD', 'AC', 'BD'
'AB', 'BC', 'DA', 'AC', 'BD'
'AB', 'CD', 'DA', 'AC', 'BD'
'BC', 'CD', 'DA', 'AC', 'BD'
```

#### Case 7: N = 4, K = 6, Answer = 1
* Nodes = ['A', 'B', 'C', 'D']
* Edges = ['AB', 'BC', 'CD', 'DA', 'AC', 'BD']
* [Graph Visualisation](problem_analysis_graph_07_4X6.png) with following edges.

```
'AB', 'BC', 'CD', 'DA', 'AC', 'BD'
```

### Solution/Algorithm
<pre>
function answer(numbers)
    Input: 
        - (int list) numbers = A list of integers
    Output: 
        - (int) The sum of numbers

    1. set result = sum(numbers)

    2. return result
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
