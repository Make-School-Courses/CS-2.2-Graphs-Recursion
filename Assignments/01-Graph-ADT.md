# Homework 1: Graph Abstract Data Type (ADT)

In this assignment, you'll build out the **Graph** and **Vertex** classes, which we'll use throughout the course to model many different scenarios and build out algorithms to analyze those scenarios in various ways. You'll also get a bit of practice with using **Breadth-first Search** to solve various problems.

## Purpose (Why should I do this?)

There are many ways to represent a graph in code. We'll be getting up close and friendly with the **Adjacency List** implementation. Building out the code will give you a better understanding of how the **Graph** and **Vertex** classes work together, which will build up a foundation for tackling more complex graph algorithms.

Scoring is as follows:

| Criteria | Possible |
| :------: | :------: |
| Graph & Vertex classes | 20 |
| File Reader | 20 |
| Breadth-first Search & Find Neighbors | 20 |
| Discussion Questions | 10 |
| **TOTAL** | **70** |

## Instructions

### Getting Started

Follow the steps below to set up your GitHub repository for this course. 

**Important**: Please follow these instructions exactly to correctly set up your clone of this repository. If you skip a step or do them out of order, it may not work.

**Step 1**: Set up your local clone of the starter code repo on your computer.

1. Clone the [Homework 1 starter code](https://github.com/Make-School-Labs/Graph-ADT-Starter-Code) to your local machine.
1. Go to [GitHub.com](https://github.com) and create an _empty_, public repository to contain your code. Do not initialize it with a README.
1. Set the origin remote's URL on your local repo to point to your new repo on GitHub: `git remote set-url origin https://github.com/<your-username>/<your-repo-name>.git`.
1. Push your local repo to your remote GitHub repo to link your master branch to your origin remote: `git push -u origin master`
1. Commit your code to your local repo frequently (each time you've made meaningful progress).
1. Push your commits to your remote GitHub repo when you want to publish and backup your code: `git push` (the -u in the previous command lets you omit origin master afterward).

**Step 2**: Connect your local clone of this course repo to the _upstream_ repo on GitHub.

1. Add the starter code's upstream repo as another remote to your local repo with: `git remote add upstream https://github.com/Make-School-Labs/Graph-ADT-Starter-Code.git`
1. Verify that you have two remotes: `origin` (with your username in the URL) and `upstream` (with Make-School-Labs) with `git remote -v`
1. When you want to access new starter code for future assignments, first be sure you've committed and pushed your recent work (run `git status` to check) and then pull from the course's upstream repo with: `git pull upstream master`.

## Graph & Vertex Classes _(20 Points)_

Open the `graphs/graph.py` file and take a look at the code. The `Vertex` class contains a _dictionary_ of its neighbors. The _keys_ of the dictionary are the neighbor vertices' IDs, and the _values_ of the dictionary are the corresponding neighbor objects. If two vertices `A` and `B` are connected (i.e. if there is an edge between them), then `A` will be in `B`'s neighbors, and vice versa. Similary, the `Graph` class contains a dictionary of its vertices that maps a vertex id to a `Vertex` object.

**Complete the code for** the `Vertex` method `add_neighbor`, and the `Graph` methods `add_vertex` and `add_edge`.

After you are done, _manually test_ your code by running the `main.py` file in your terminal. Modify the `main.py` code to test many types of graphs!

Then, run the built-in tests by running the following from your repository's root directory. The first two test cases should pass.

```bash
$ python3 -m unittest discover
```

## File Reader _(20 Points)_

Open the `util/file_reader.py` file. Your goal is to write a function that takes in the name of a text file, and returns a `Graph` object with vertices and edges as specified by the file.

The files you read in will have the following format:

- The first line is either `G` (for undirected graph) or `D` (for digraph)
- The second line is a list of vertices separated by commas
- The remaining lines are one vertex pair per line representing the edges (x, y).

Here is an example of a graph file:

```
G
A,B,C,D
(A,B)
(A,D)
(B,C)
(B,D)
```

If you need a refresher on File I/O in Python, check out [this guide](https://www.programiz.com/python-programming/file-operation).

After you are done, _manually test_ your code by running the `main.py` file in your terminal. Modify the `main.py` code to test many types of graphs!

Then, run the built-in tests by running the following from your repository's root directory. The first two test cases should pass.

```bash
$ python3 -m unittest discover
```

## Breadth-first Search Traversal

Take a look at the `bfs_traversal` method in the `Graph` class. This method "visits" every vertex in the graph, one at a time, in breadth-first-search order. This means that vertices that are closest to the start node (in terms of number of edges away) will be visited first, and the vertices that are furthest away from the start node will be visited last.

The pseudocode of the function is roughly as follows:

- Create a 'seen' set to hold the vertices we visit along the way. This step is necessary in order to avoid entering an infinite loop! If we've already 'seen' a vertex, we don't want to visit it again.
- Create a queue to hold the vertices we'll be visiting next. Using a queue ensures that the vertices closest to the start (which are added to the queue first) are visited first.
- While the queue is not empty, do the following:
  - Pop a vertex `v` from the queue (that is, remove it)
  - Process vertex `v` by printing it to the console (In some cases, "processing" a vertex could mean something different; in this case, we're just printing it.)
  - Put each of `v`'s unvisited neighbors into the queue.

Run the method on a graph by running `main.py` and make sure it works as intended. If it doesn't, you may need to go back and fix your code for the `Vertex` and/or `Graph` classes.

### Find Shortest Path _(10 Points)_

Complete the `find_shortest_path` method in the `Graph` class. This method uses a similar methodology to the `bfs_traversal` method, but now there's more that we need to keep track of! Instead of merely "visiting" each vertex, we need to know each vertex's shortest path from the start vertex. So, we can utilize the "seen" data structure to serve a dual purpose: It can keep track of what we've seen so far (so that we don't enter any infinite loops!), _and_ it can store each vertex's shortest path from the start.

The pseudocode of the function is roughly as follows:

- Create a `vertex_id_to_path` dictionary. This keeps track of the vertices we've seen so far, _and_ stores their shortest paths.
- Create a queue to hold the vertices we'll be visiting next.
- While the queue is not empty, do the following:
  - Pop a vertex `v` from the queue
  - If `v` is the target, quit early (this saves us some runtime, since we no longer care about the rest of the graph!)
  - Do the following for each of `v`'s unvisited neighbors `n`:
    - Extend `v`'s path by one vertex to form `n`'s path (that is, if the old path was `A -> B -> V`, it will now be `A -> B -> V -> N`)
    - Put `n` into the queue
- After the queue is empty, return the path for the target vertex, or `None` if it was not found.

Run the method on a graph by running `main.py` and make sure it works as intended. You can then run the provided unit tests with `python3 -m unittest discover`.

### Find All Connections of a Given Distance _(10 Points)_

Complete the `find_vertices_n_away` method in the `Graph` class. This method should use breadth-first search to find all vertices that are `n` away from the start vertex, for some `n`.

<img src="Lessons/assets/graph.png" width="500px">

For example, using the graph above:

- `find_vertices_n_away('A', 0)` should return `['A']`
- `find_vertices_n_away('A', 1)` should return `['B', 'C']`
- `find_vertices_n_away('A', 2)` should return `['D', 'E']`
- `find_vertices_n_away('A', 3)` should return `['F']`

Your solution should be similar to the `find_shortest_path` method. You may want to start by writing pseudocode, then writing real code.

To test your code, make sure you run `main.py` to test manually, and run the provided unit tests with `python3 -m unittest discover`.

## Discussion Questions _(10 Points)_

In your repository's `README.txt`, answer the following discussion questions:

1. How is Breadth-first Search different in graphs than in trees? Describe the differences in your own words.

2. What is one application of Breadth-first Search (besides social networks)? Describe how BFS is used for that application. If you need some ideas, check out [this article](https://www.geeksforgeeks.org/applications-of-breadth-first-traversal/?ref=rp).

## Submission

Submit your code for Assignment 1 using [Gradescope](https://gradescope.com) using the GitHub integration feature. If you are unable to submit for any reason, please reach out to your instructor.

## Resources

1. [A Gentle Introduction to Graph Theory](https://medium.com/basecs/a-gentle-introduction-to-graph-theory-77969829ead8)
1. [Breadth-First Search for a Graph](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
1. [Shortest Path in an Unweighted Graph](https://www.geeksforgeeks.org/shortest-path-unweighted-graph/)
1. [File I/O in Python](https://www.programiz.com/python-programming/file-operation)
