import sys
from graph_file_reader import read_from_file

def main():
    # Challenge 1: Create the graph
    filename = sys.argv[1]
    g = read_from_file(filename)

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print(f"The vertices are: {g.get_vertices()} \n")

    # Print edges
    print("The edges are: ")
    for edge in g.get_edges_weighted():
        print(edge)


if __name__ == "__main__":
    main()
