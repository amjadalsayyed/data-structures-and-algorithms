class Node:
    """Node class with 3 variables value, weight, and next
    """
    def __init__(self, value):
        self.value = value
        self.weight = None
        self.next = []

class Edge:
    def __init__(self,vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj_list = {}
        self.size = 0

    def add_vertex(self, value):
        """this function gets a value and creates a new node from it then adds it to the adj_list as a key with an empty list as a value for that key"""
        new_vertex = Node(value)
      
        self.adj_list[new_vertex] = []
        self.size += 1
        return new_vertex
    
    def add_edge(self,vertex1, vertex2, weight=0):

        """this function gets called with to vertices and an optional weight parameter then checks if the two vertices exist in the adj_list then create an edg from both vertices and add them to the list of edges for each one of them"""

        if not vertex1 in self.adj_list.keys():
            return("this vertex does not exist")
        
        if not vertex2 in self.adj_list.keys():
            return("this vertex does not exist")
        
        edge1 = Edge(vertex2, weight)
        self.adj_list[vertex1].append(edge1)

        edge2 = Edge(vertex1, weight)
        self.adj_list[vertex2].append(edge2)

    def get_vertices(self):
         """this function is called with no arguments and returns a list of vertices"""
         vertices = []
         for i in self.adj_list.keys():
             vertices.append(i.value)
         return vertices

    def get_neighbors(self,vertex):
        """this function is called with a vertex as an argument and returns a list of edges connected to it"""
        result = []
       
        for i in self.adj_list[vertex]:
                tub = (i.vertex.value,i.weight)
                result.append(tub)
        return result
    
    def get_size(self):
        """this function is called with no arguments and returns the size of the graph"""
        return self.size

    def __str__(self):
        output = ''
        for vertex in self.adj_list.keys():
            output += f'{vertex.value} -> '
            for edge in self.adj_list[vertex]:
                output += f'{edge.vertex.value} -----> '
            output += '\n'
        return output

    def bfs (self,vertex):
        """this function will declare a queue with the given vertex in it,output list ,visited vertex dict and a current vertex then mark the given vertex as visited by adding it to the visited vertex dictionary then using a while loop to loop until the queue is empty in the loop it pop the first vertex in the queue and append its value to the output list then do a for loop to loop over the neighbors of the current vertex and adds its values to the queue and mark them as visted by adding them to the visited vertex dictionary with a value of True"""
        queue = [vertex]
        output = []
        visited_vertex = {}
        current_vertex = None
        visited_vertex[vertex] = True

        while(len(queue) > 0):
            current_vertex = queue.pop(0)
            output.append(current_vertex.value)
            
            for i in self.adj_list[current_vertex]:
                if i not in visited_vertex :
                    visited_vertex[i] = True
                    queue.append(i)
        return output        
