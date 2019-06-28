# CS 2.2 Graph Modeling Project

## Project Description
It's your turn to tackle a real world problem using your graph theory skills.  You will chose a problem and a set of solutions to implement, using a similar approach to the [Graph Modeling Tutorial]().  You will implement graph theory solutions in python for small amounts of data within your problem scope and then innovate towards solutions when working with data at scale.  

## Project Timeline
- **Due Date 1:** Problem choice submitted and approved.
- **Due Date 2:** Graph Implementation complete.
- **Due Date 3:** Blog or Presentation complete.

## Project requirements
- **Choose the problem:** Choose a problem from the provided list or a different problem that can be modeled and a graph and has solutions that can be implemented with graph algorithms from this class. You must use at least 3 different algorithms to define at least 3 different solutions.
    - **Example:** Given a network of friends, find the biggest influencer, the largest group of friends who all know each other, and the longest time it would take for a message to pass from person A to person B via friends.
- **Model the problem:** Represent the problem and the desired solutions using graphs and graph theory.
    - **Example:** The network of friends is modeled with each person being a vertex in a graph and an edge between any two people if they are friends.  
        - The biggest influencer is the maximum degree of the graph.
        - The largest group of friends is the maximal clique number in the graph.  This can be approximated by Turán's theorem.
        - The time to send a message is the shortest path which can be found via Dikstra's Algorithm.
- **Implement Graph and Algorithms in Python:** Create a python program (from scratch not using graph libraries) that can read in a small (n < 30) version of your problem from a text file and solve the algorithms above. Your code should be fully documented, tested and meet [PEP8](https://realpython.com/python-pep8/) standards. Your code should work on any data set with (n < 30) defined to meet problem specifications as defined in your documentation (README).  Your code should be available as a separate project on GitHub.
- **Discuss Scale:** What happens with your solutions at scale? (n >>> 30).  Is your problem still solvable? Discuss in your GitHub README and associated Summary.  If possible, implement a scalable solution.   
- **Blog or Present:** Create a presentation or blog post of your project according to the [Presentation Rubric]() or [Blog Post Rubric]().


## Stretch Project Requirements
- Implement a common graph algorithm that was not covered in class on your program.
- Use graph libraries to refactor your code implementations, benchmark and compare results.

## List of possible problem choices:
- Airplane Scheduling
- Knights on a Chessboard
- The Internet
- ... More to Come 
