class Node:
    """Node class with 3 variables value, weight, and next
    """
    def __init__(self, value):
        self.value = value
        self.weight = None
        self.next = []

class Edge:
    def __init__(self,vertex, weight=0):
        self.value = vertex.value
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj_list = {}
        self.size = 0

    def add_vertex(self, value):
        """this function gets a value and creates a new node from it then adds it to the adj_list as a key with an empty list as a value for that key"""
        new_vertex = Node(value)
      
        self.adj_list[f'{new_vertex.value}'] = []
        self.size += 1
        return new_vertex
    
    def add_edge(self,vertex1, vertex2, weight=0):

        """this function gets called with to vertices and an optional weight parameter then checks if the two vertices exist in the adj_list then create an edg from both vertices and add them to the list of edges for each one of them"""

        
        if not vertex1.value in self.adj_list.keys():
            return "this vertex does not exist"
        
        if vertex2 is None or not vertex2.value in self.adj_list.keys():
            return "this vertex does not exist"
        
        edge1 = Edge(vertex2, weight)
        self.adj_list[f"{vertex1.value}"].append(edge1)
        edge2 = Edge(vertex1, weight)
        self.adj_list[f"{vertex2.value}"].append(edge2)

    def get_vertices(self):
         """this function is called with no arguments and returns a list of vertices"""
         vertices = []
         for i in self.adj_list.keys():
             vertices.append(i)
         return vertices

    def get_neighbors(self,vertex):
        """this function is called with a vertex as an argument and returns a list of edges connected to it"""
        result = []
       
        for i in self.adj_list[vertex.value]:
                tub = (i.value,i.weight)
                result.append(tub)
        return result
    
    def get_size(self):
        """this function is called with no arguments and returns the size of the graph"""
        return self.size

    def __str__(self):
        output = ''
        for vertex in self.adj_list.keys():
            output += f'{vertex} -> '
            for edge in self.adj_list[vertex]:
                
                output += f'{edge.value} -----> '
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
            
            for i in self.adj_list[current_vertex.value]:
                if i.vertex not in visited_vertex :
                    visited_vertex[i.vertex] = True
                    queue.append(i.vertex)
        return output        




        
    def business_trip (self,vertex,cites_list):
        """this function loops over the cites list using the enumarate method to get the index and the value then inside the loop  create a node of the value and get its neibghors and inatilize a new dictionary to stor the nighbors value and weight related to the node value as long as we didn't reach the last value in the cites list the check if there is an edge between the value and the value next to it in the list of cites by checking if its in the dictionary if it exists we add it to the sum if not we return none """
        sum = 0 

        for i , v in enumerate(cites_list):
            vertex_of_v = Node(v)
            neighbors = self.get_neighbors(vertex_of_v)
            dict = {}
            if i < len(cites_list)-1:
                for j in neighbors:
                    dict[j[0]]= j[1]
                if cites_list[i+1] in dict:
                    sum += dict[cites_list[i+1]]
                else:
                    return None    
        return sum           
    
    def depthFirst(self,start ):
        """this function calls the helper function dfsrecursive with the start vertex in the helper function we add the vertex value to the result and mark it as visted then loop on its edges and check if the edge not visted then we call the dfsrecursive function on it then return the result list """
        result = []
        visited = {}
        def dfsrecusive(vertex):
            if vertex is None: return None
            visited[vertex] = True
            result.append(vertex.value)
            for i in self.adj_list[vertex.value]:
                if i.vertex not in visited:
                    dfsrecusive(i.vertex)
        dfsrecusive(start)

        return result        


# if __name__=='__main__':
#             graph = Graph()

#             a = graph.add_vertex("A")
#             b = graph.add_vertex("B")
#             c = graph.add_vertex("C")
#             d = graph.add_vertex("D")
#             e = graph.add_vertex("E")
#             f = graph.add_vertex("F")
#             g = graph.add_vertex("G")
#             h = graph.add_vertex("H")

#             graph.add_edge(a,b,2)
#             graph.add_edge(a,d,3)
#             graph.add_edge(b,c,3)
#             graph.add_edge(b,d,4)
#             graph.add_edge(c,g,5)
#             graph.add_edge(d,e,5)
#             graph.add_edge(d,h,5)
#             graph.add_edge(d,f,5)
#             graph.add_edge(h,f,5)
            
#             print(graph.depthFirst(a))