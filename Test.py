from dijkstra import dijkstra

def test_simple_graph():
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("D", 10)],
        "C": [("E", 3)],
        "D": [],
        "E": [("D", 4)],
    }
    distances, prev = dijkstra(graph, "A")
    assert distances["A"] == 0
    assert distances["B"] == 4
    assert distances["C"] == 2
    assert distances["E"] == 5
