import unittest
from graph import Graph
from vertex import Vertex

class GraphTest(unittest.TestCase):
    def test_add_vertex(self):
        graph = Graph()
        graph.add_vertex("apple")
        graph.add_vertex("banana")

        self.assertEqual(2, graph.get_num_vertices())
        self.assertIsInstance(graph.get_vertex("apple"), Vertex)


    def test_add_edge(self):
        graph = Graph()
        graph.add_vertex("apple")
        graph.add_vertex("banana")
        graph.add_vertex("coconut")

        graph.add_edge("apple", "banana")
        graph.add_edge("apple", "coconut", 3)

        self.assertEqual(3, graph.get_num_vertices())
        self.assertEqual(2, graph.get_num_edges())

        graph.add_edge("pineapple", "strawberry")

        self.assertEqual(5, graph.get_num_vertices())
        self.assertEqual(3, graph.get_num_edges())
        self.assertCountEqual(
            ["apple", "banana", "coconut", "pineapple", "strawberry"],
            graph.get_vertices())

if __name__ == "__main__":
    unittest.main()