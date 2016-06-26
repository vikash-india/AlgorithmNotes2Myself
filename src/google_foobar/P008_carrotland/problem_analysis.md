# Problem Analysis

### Concepts/Theories
* Pick's Theorem to find the area of a polygon using the lattice points inside polygon and the lattice points on the
  boundary of the polygon.
* Shoelace formula to find the area of a polygon when the vertices are given in an ordered pair on a plane. Use this
  to find the area of the triangle given its three coordinates (x1, y1), (x2, y2), (x3, y3).
* The property of GCD in a Cartesian coordinate system, where gcd(a, b) can be interpreted as the number of segments 
  between points with integral coordinates on the straight line segment joining the points (0, 0) and (a, b). 

### Analysis
Let's first visualise the problem by drawing a few triangles using the 3 coordinates of a triangle on a 2-D plane. Say,
we create the following images of the triangles to explore our problem further.

1. [Triangle - 1](problem_analysis_triangle_01.png)
2. [Triangle - 2](problem_analysis_triangle_02.png)
3. [Triangle - 3](problem_analysis_triangle_03.png)
4. [Triangle - 4](problem_analysis_triangle_04.png)
5. [Triangle - 5](problem_analysis_triangle_05.png)

#### Some Obeservations
1. Little bit of googling on how to find the interior points of a triangle given its coordinate will point us to the
   Pick's theorem. Pick's Theorem is a method for determining the area of any polygon whose vertices are points on a 
   lattice, a regularly spaced array of points. This is exactly what we need. Use 
   [Pick's theorem](https://en.wikipedia.org/wiki/Pick%27s_theorem).
2. In order to use Pick's theorem to find the interior points of a triangle, we need to know the area of a triangle and
   the number of points on the boundary of the triangle.
3. The area of triangle can be found out using the Shoelace formula. Shoelace formula is a mathematical algorithm to 
   determine the area of a simple polygon whose vertices are described by ordered pairs in the plane. Use 
   [Shoelace Formula](https://en.wikipedia.org/wiki/Shoelace_formula#Explanation_of_name).
4. The number of boundary points on the triangle can be found using the Greatest Common Divisor (GCD). In a Cartesian 
   coordinate system, gcd(a, b) can be interpreted as the number of segments between points with integral coordinates on 
   the straight line segment joining the points (0, 0) and (a, b). This can also be used in our case even when the line
   does not pass through origin because the line y = mx + c when shifted to pass through origin c, the number of integer
   points that the line will cross between 2 points will remain same.

### Solution/Algorithm
<pre>
function answer(vertices)
    Input: 
        - (int list of list) vertices = A list of list of integers coordinates. Eg. [[x1, y1], [x2, y2], [x3, y3]]
    Output: 
        - (int) Total number of interior points of the triangle.

    1. set x1, y1 = vertices[0][0], vertices[0][1]
    2. set x2, y2 = vertices[1][0], vertices[1][1]
    3. set x3, y3 = vertices[2][0], vertices[2][1]

       # Area of triangle using Shoelace formula
    4. area = .5 * abs((x1 - x3) * (y2 - y1) - (x1 - x2) * (y3 - y1))

       # Number of integer points on the boundaries
    5. boundary = gcd(abs(x1 - x2), abs(y1 - y2)) + gcd(abs(x2 - x3), abs(y2 - y3)) + gcd(abs(x3 - x1), abs(y3 - y1))

       # Number of integer points inside the triangle using Pick's theorem
    6. interior_points = area - boundary / 2 + 1

    7. return int(interior_points)
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
