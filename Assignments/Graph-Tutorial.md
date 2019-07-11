# Your Social Network - Graph Tutorial

## Chapter 0: Set up
How many social network platforms are you currently on? Each of those is an example of graph theory being applied to solve the problem of finding connections – and recommending appropriate ones.

In this tutorial, you'll build a graph of your nine closest friends and use graph theory to figure out interesting data about them.

### Learning Outcomes
By the end of this tutorial, you will be able to...

1. Implement a graph in code.
1. Use a variety of neighbor lookup algorithms for a given graph
1. Traverse a graph through various search methods


### Using Git/GitHub
Much like we've done in earlier tutorials, make sure you're committing your code as you complete milestones. At a minimum, you should make a commit whenever the tutorial prompts you.

Let's get your repo set up!

1. Go to the [Graph Tutorial](https://github.com/Make-School-Labs/CS-2.2-Labs) and clone the repo locally.
1. Now we need to change the remote so that you can commit/push/pull the changes you make to your own repo. **It is very important you do the below steps in order to get everything working properly.**
1. Go to GitHub and create an _empty_, public repository called Graph-Tutorial, and now associate it as a remote for your cloned starter code, and then push to it.
1. Go to your repo on GitHub and make sure your previously empty repo is now full with starter code! Now when you add/commit/push, it'll be to your repo!

## Chapter 1: Who do you know?
This tutorial will focus on properties of a social network.  To begin with, we'll need to define a network as a set of people (vertices) and the people they know.  If person *A* knows person *B* then there is an edge between them.  We will begin by assuming that if person *A* knows person *B* then the reverse is also true. (So the edge is undirected).

1. Draw a graph with you at the center connected by and edge to another 9 people you know.  Do any of these 9 know each other? If so draw an edge between them.  This will be your "Social Graph" to use as a sample in the rest of this tutorial.  Your graph must have the following properties:
- Every person knows at least 2 other people.  
- No person knows more than 5 people.

**Challenge** Add a diagram (or hand drawn image) of your friend network to the readme of your tutorial code.  Label the nodes with you and your 9 friends names.  If you don't want to use your real friends, feel free to use [Faker](https://faker.readthedocs.io/en/master/) to give fake names.

### Implement in code

Throughout this tutorial we will build up a *graph data structure* that will implement our graph and graph algorithms in python.

We will be building onto the basic Graph Abstract Data Type (ADT) which is defined as follows:

```python

Graph() #creates a new, empty graph.
addVertex(vert) #adds an instance of Vertex to the graph.
addEdge(fromVert, toVert) #Adds a new, directed edge to the graph that connects two vertices.
addEdge(fromVert, toVert, weight) #Adds a new, weighted, directed edge to the graph that connects two vertices.
getVertex(vertKey) #finds the vertex in the graph named vertKey.
getVertices() #returns the list of all vertices in the graph.

```

**Challenge:** Implement the `Graph` class in the file *graph.py* and input your personal Social Graph with vertices and edges matching the diagram you drew of your friends.  Note: Initially we'll create a `Vertex` class as a helper class to the `Graph` class. 

## Chapter 2: Won't you Be My Neighbor?
Have you ever had that moment where you find out a friend knows another one of your friends? Having one of those "worlds collide" moments can be exciting, scary, or a whole mixture of emotions. Instead of having that situation surprise us, what if we had a way to look know this information. in advanced?

### Find Your Neighbors
Turns out we do! We can utilize a **neighbor lookup** for a given node in our graph to see what other nodes it is connected with. If you and a friend are connected, you two share a friendship. How do we know if two nodes are connected? _They share an edge!_

**Challenge:** Write a method `getNeighbors` in the `Vertex` class that outputs all nodes connected to the current node.

```python
def getNeighbors(self):
    # Make sure the input node is actually in the graph
    # Find all edges for the input node
    # See what nodes are connected to the input node via the edge
    # return the connected nodes
```

### Down The Friend Chain We Go
Alright, no more surprise connections for us! But what if we want to go even _further_ than one connection? Onward!


## Chapter 3: Breadth of Fresh Neighbors

How does Facebook or LinkedIn know what friends to recommend to you? They look at who your friends are friends with, and who their friends are friends with, and so on

![two friends](https://media1.giphy.com/media/r73emnWNwTWRq/giphy.gif)

_Source: [Giphy](https://giphy.com/gifs/saturday-night-live-waynes-world-r73emnWNwTWRq)_

### Friends of Friends
The function you just wrote is great for finding your immediate friends, but what if we want to see their friend's friends?

Think back to CS 1.3: what's an algorithm at your disposal we could use here?

Since we want to find _all_ friends at a certain connection level away (friend's friend would be 2 connections from you), this sounds like a perfect application of **Breadth First Search (BFS)**. Check out the [Tree Traversals lesson](https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Lessons/TreeTraversals.md) from CS 1.3 if you want a refresher.

**Challenge:** Write a method `BFS(vertex, n)`in the `Graph()` class that takes in a node, and `n` (an integer) as input, and outputs all nodes that are exactly `n` connections away from the input node.


```python
def BFS(self, vertex, n):
# Make sure the input node is actually in the graph
# Run BFS starting from the input node and going `n` levels deep
# Return all nodes found at the `n`th level
```

### A More Granular Approach
Great application of BFS! But as with anything related to BFS, specificity isn't a strong suite. Having _all_ of your 3rd, 4th, 5th degree connections is daunting. What if we just want to see how two _specific_ people are connected? We'll solve this in the next chapter!

## Chapter 4: Friends Along the Way
There's this idea of [six degrees of separation](https://en.wikipedia.org/wiki/Six_degrees_of_separation): take two people in the world, and they are at most six social connections away from each other. You may be more familiar with the [Six Degrees of Kevin Bacon](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon) as an example of this.

![kevin bacon](https://res.cloudinary.com/teepublic/image/private/s--NvWG-b6R--/t_Preview/b_rgb:ffffff,c_limit,f_jpg,h_630,q_90,w_630/v1558890523/production/designs/4930303_0.jpg)

_Source: [MisterDressup](https://www.teepublic.com/t-shirt/4930303-kevin-bacon-bacon-lover-funny-t-shirt)_

You may not know Kevin Bacon (or _do_ you?), but we can still apply this to our graph of friends to find the connections that create a chain between two people. This is an application of **path finding**

### Finding the Path
Think of a graph as a neighborhood, each house as a node, and immediate neighbors as nodes that share an edge. If you wanted to figure out how to get from one house to another, you'd walk to that house, passing other houses along the way. _You'd be walking a path, walking from one node to another via edges!_

**Challenge:** Write a method `findPath()` that takes in two nodes (A and B) as input, and outputs the list of nodes that must be traversed to get from A to B. The output list of nodes _must be in order of nodes visited starting from A and ending at B._

**Hint:** BFS or it's familiar friend **Depth First Search (DFS)** could be useful here. Again if you need a refresher, here's that [Tree Traversals lesson](https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Lessons/TreeTraversals.md) from CS 1.3

```python
def findPath(self, fromVert, toVert):

# Make sure that both nodes A and B are actually in the graph
# Run BFS or DFS starting from A
# Figure out a way to keep track of each path you take
# Once you find B, end the search.
# Since you've been tracking the paths, find the path that goes from A to B
# Return the path, in the order of nodes visited starting with A and ending with B
```

### Optimizing our Path
This works, but what if there are multiple paths between two nodes? What if one of those paths is significantly longer than the other? Do you know Veronica from high school from your cousin Ricky, who went to college with Sarah, who dated Jane, who is friends with Billy, who was on the swim team with Veronica? Or do you know Veronica from your friend Tom who also is friends with Veronica? In the next chapter, we'll learn how to differentiate paths in order to optimize our route.

## Chapter 5: Closest of Friends
If you were trying to show how two people are socially connected, you would want to do so in the least number of connections possible. Can you imagine if LinkedIn couldn't determine if someone was a 2nd or 20th degree connection?

### Shortest Path

In order to solve this problem, we want to find the **shortest path** between two nodes in a graph.

**Challenge 1:** Write a method `findShortestPath()` that takes two nodes (A and B) as input, and outputs the list of nodes that make up the _shortest path_ from A to B. The output list of nodes _must be in order of nodes visited starting from A and ending at B._

```python
def findShortestPath(self, fromVert, toVert):
# Make sure that both nodes A and B are actually in the graph
# Run BFS starting from A
# Figure out a way to keep track of each path you take
# Once you find B, end the search.
# Since you've been tracking the paths, find the shortest path that goes from A to B
# Return the shortest path, in the order of nodes visited starting with A and ending with B
```


### The Long and Short of it is...
Now we can handle the shortest path for  unweighted graphs! Great work!  When it comes to weighted graphs, we need a stronger algorithm which we'll explore in later tutorials.  If you're feeling curious, you can read about [Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) and even implement it in your class.


 It's great to find the _shortest_ path, but sometimes we want to know more about a graph. There's a lot of properties around distance we can measure, and we'll dive into another one of them in the next chapter!

## Chapter 6: Long-Distance Friendships

We know you're six degrees away from Kevin Bacon, but who are you the _furthest_ away from? Not your pen pal in Bhutan (that would still be a neighbor!), but someone you _don't_ know, and who you in fact know the least!

### Graph Diameter
One concept around graph distance that helps us solve this problem is finding the **diameter** of a graph. The diameter of a graph is the calculated by _finding the shortest path between every possible pair of nodes, and then selecting the longest of those paths._

**Challenge:** Write a method  `diameter` that outputs the diameter of the graph

```python
def diameter(self):
# For every node, find the shortest path from it to every other node in the graph and track the paths and their length
# From your list of path/length pairs, pick the one with the largest length and return the length.
```
**Stretch Challenges:** Find other properties of a graph! See if you can calculate the center or radius of a weighted graph. Keep these notes in mind:

- A radius of a graph _must_ also have a diameter.
- Radius can be calculated by finding the minimum distance among all the maximum distances between a node to all other nodes
- The center of a graph is the set of all nodes where the greatest distance to other nodes is the shortest.
    - Read up on [eccentricity](https://en.wikipedia.org/wiki/Distance_(graph_theory) to help with this!


### Becoming an Influencer
We've seen a lot of social network applications with our graph so far, but there are other real applications of graph theory throughout the industry! One of the biggest applications is in the tool you use every day...


## Chapter 7: How to Win Friends and Influence Users
Google's [PageRank](https://en.wikipedia.org/wiki/PageRank) algorithm is what they use to show you the most relevant search results for your query. Through this, Google influences what you see on that first page every single time you search something (and how often are you going past the first page?)


### PageRank Your Friends

PageRank is currently implemented using concepts from graph theory, assigning scores of "relevance" to links. We're going to model that by doing the same thing to our social networks (what, you've never ranked your friends before?). _This is how social media influence is calculated!_ Let's find out which of our friends have the most influence in the network:

**Note:** For the below challenge, you'll be using a _directed_ weighted graph.

**Challenge:** Write a method  `influencer()` that uses the PageRank algorithm to rank your friends according to their influence.

```python
def influencer(self):
# walk through implementing page rank on the graph, step by step
```

### Clique through

So now you've ranked your fake friends (do they feel real, yet?), but as with any large group of people, smaller groups start to form within the larger ones. We can find these cliques through graph theory! One more chapter to go, you _got this!_

## Chapter 8: On Wednesdays We Wear Pink
Find “cliques” of friends (small groups of tightly-connected users), etc…

The [clique problem](https://en.wikipedia.org/wiki/Clique_problem) is a popular computational problem in computer science. Contrary to popular belief, this problem was not caused by people being personally victimized by Regina George.

![mean girls](https://media.giphy.com/media/3otPowYz6GbeQdvda8/giphy.gif)

_Source: [Giphy](https://giphy.com/gifs/filmeditor-mean-girls-movie-3otPowYz6GbeQdvda8)_

While we are confident that we're not bound by wearing pink on Wednesdays, solving clique problems is a whole other issue. These problems tend to be challenging, but it's nothing we can't take on!

### Clique Discovery

Among other applications, the clique problem can arise in a social network. With our social network, a clique will represent a subset of people (nodes) who all know each other (share edges), and we can use various algorithms to find these cliques.

**Challenge:** Write a method `cliqueNumber()` that finds the largest clique in a graph.


```python
def cliqueNumber(self):
# walk through clique algorithm, step by step
```


**Congrats on completing your journey through the Faker Network!**

### Feedback and Review - 2 minutes

**We promise this won't take longer than 2 minutes!**

Please take a moment to rate your understanding of the learning outcomes from this tutorial, and how we can improve it via our [tutorial feedback form](https://forms.gle/Wva3u51vBiDQHBAw9)

This allows us to get feedback on how well the students are grasping the learning outcomes, and tells us where we can improve the tutorial experience.
