# Code Challenge 35

## Class of hash table

## add_vertex function

### arguments : value

### returns: new vertex

### big O

#### time : O(1) space : O(1)

### Approach

#### this function gets a value and creates a new node from it then adds it to the adj_list as a key with an empty list as a value for that key

## add_edge function

### arguments : vertex1, vertex2, weight : optional

### returns: nothing

### big O

#### time : O(1) space : O(1)

### Approach

#### this function gets called with to vertices and an optional weight parameter then checks if the two vertices exist in the adj_list then create an edg from both vertices and add them to the list of edges for each one of them

## get_vertices function

### arguments : None

### returns: a list of vertices

### big O

#### time : O(n) space : O(n)

### Approach

#### this function is called with no arguments and returns a list of vertices

## get_neighbors function

### arguments : vertex

### returns: list of edges of the vertex

### big O

#### time : O(n) space : O(n)

### Approach

#### this function is called with a vertex as an argument and returns a list of edges connected to it

## get_size function

### arguments : none

### returns: size

### big O

#### time : O(1) space : O(1)

### Approach

#### this function is called with no arguments and returns the size of the graph
