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

1. Clone the [Homework 1 starter code]() to your local machine.
1. Go to [GitHub.com](https://github.com) and create an _empty_, public repository to contain your code. Do not initialize it with a README.
1. Set the origin remote's URL on your local repo to point to your new repo on GitHub: `git remote set-url origin https://github.com/<your-username>/<your-repo-name>.git`.
1. Push your local repo to your remote GitHub repo to link your master branch to your origin remote: `git push -u origin master`
1. Commit your code to your local repo frequently (each time you've made meaningful progress).
1. Push your commits to your remote GitHub repo when you want to publish and backup your code: `git push` (the -u in the previous command lets you omit origin master afterward).

**Step 2**: Connect your local clone of this course repo to the _upstream_ repo on GitHub.

1. Add the starter code's upstream repo as another remote to your local repo with: `git remote add upstream https://github.com/Make-School-Courses/CS-2.1-Trees-Sorting.git`
1. Verify that you have two remotes: `origin` (with your username in the URL) and `upstream` (with Make-School-Labs) with `git remote -v`
1. When you want to access new starter code for future assignments, first be sure you've committed and pushed your recent work (run `git status` to check) and then pull from the course's upstream repo with: `git pull upstream master`.

## Graph & Vertex Classes _(20 Points)_



After you are done, _manually test_ your code by running the `main.py` file in your terminal. Modify the `main.py` code to test many types of graphs!

Then, run the built-in tests by running the following from your repository's root directory:

```bash
$ python3 -m unittest discover
```

## File Reader _(20 Points)_



## Breadth-first Search

### Find Shortest Distance _(10 Points)_



### Find All Connections of a Given Distance _(10 Points)_



## Discussion Questions _(10 Points)_

In your repository's `README.txt`, answer the following discussion questions:

1. How is Breadth-first Search different in graphs than in trees? Describe the differences in your own words.

2. What is one application of Breadth-first Search (besides social networks)? Describe how BFS is used for that application. If you need some ideas, check out [this article](https://www.geeksforgeeks.org/applications-of-breadth-first-traversal/?ref=rp).

## Submission



## Resources

