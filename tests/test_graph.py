from graph.graph import Graph
def test_graph_one():
    graph = Graph()

    graph.add_vertex("A")
    actual = str(graph)
    expected = "A -> \n"
    assert actual == expected

def test_graph_two():
    graph = Graph()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    graph.add_edge(a,b,2)
    actual = str(graph)
    expected = "A -> B -----> \nB -> A -----> \n"
    assert actual == expected

def test_graph_three():
    graph = Graph()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")
    actual = graph.get_vertices()
    expected =['A', 'B', 'C', 'D']
    assert actual == expected

def test_graph_four():
    graph = Graph()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")
    graph.add_edge(a,b,2)
    graph.add_edge(a,c,3)
    graph.add_edge(c,b,3)
    graph.add_edge(d,b,4)
    graph.add_edge(d,c,5)
    actual = graph.get_neighbors(d)
    expected =[('B', 4), ('C', 5)]
    assert actual == expected

def test_graph_size():
    graph = Graph()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")
    graph.add_edge(a,b,2)
    graph.add_edge(a,c,3)
    graph.add_edge(c,b,3)
    graph.add_edge(d,b,4)
    graph.add_edge(d,c,5)
    actual = graph.get_size()
    expected =4
    assert actual == expected

def test_graph_five():
    graph = Graph()

    a = graph.add_vertex("A")

    graph.add_edge(a,None,2)
    actual = str(graph)
    expected ="A -> \n"
    assert actual == expected

def test_graph_six():
    graph = Graph()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")

    graph.add_edge(a,b,2)
    graph.add_edge(a,c,3)
    graph.add_edge(c,b,3)
    graph.add_edge(d,b,4)
    graph.add_edge(d,c,5)
    actual = graph.bfs(a)
    expected =['A', 'B', 'C', 'D']
    assert actual == expected


def test_graph_seven():
    graph = Graph()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")
    e = graph.add_vertex("E")


    graph.add_edge(a,b,2)
    graph.add_edge(a,c,3)
    graph.add_edge(c,b,3)
    graph.add_edge(d,b,4)
    graph.add_edge(d,c,5)
    actual = graph.bfs(a)
    expected =['A', 'B', 'C', 'D']
    assert actual == expected

def test_graph_8():
    graph = Graph()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")
    e = graph.add_vertex("E")


    graph.add_edge(a,b,2)
    graph.add_edge(a,c,3)
    graph.add_edge(c,b,3)
    graph.add_edge(b,d,4)
    graph.add_edge(d,c,5)
    actual = graph.business_trip(a,['A','C', 'B', 'D'])
    expected = 10
    assert actual == expected

def test_graph_9():
    graph = Graph()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")
    e = graph.add_vertex("E")


    graph.add_edge(a,b,2)
    graph.add_edge(a,c,3)
    graph.add_edge(c,b,3)
    graph.add_edge(b,d,4)
    graph.add_edge(d,c,5)
    actual = graph.business_trip(a,['A','D', 'B'])
    expected = None
    assert actual == expected

################# DEPTH FIRST SEARCH ##################
def test_graph_13():
    graph = Graph()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")

    graph.add_edge(a,b,2)
    graph.add_edge(a,c,3)
    graph.add_edge(c,b,3)
    graph.add_edge(d,b,4)
    graph.add_edge(d,c,5)
    actual = graph.depthFirst(a)
    expected =['A', 'B', 'C', 'D']
    assert actual == expected

def test_graph_14():
    graph = Graph()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")
   


    graph.add_edge(a,b,2)
    graph.add_edge(a,c,3)
    graph.add_edge(c,b,3)
    graph.add_edge(d,b,4)
    graph.add_edge(d,c,5)
    actual = graph.depthFirst(a)
    expected =['A', 'B', 'C', 'D']
    assert actual == expected

def test_graph_15():
    graph = Graph()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")
    e = graph.add_vertex("E")

    graph.add_edge(a,b,2)
    graph.add_edge(a,c,3)
    graph.add_edge(c,b,3)
    graph.add_edge(d,b,4)
    graph.add_edge(d,c,5)
    actual = graph.depthFirst(e)
    expected =['E']
    assert actual == expected