# INF237-AlgoritmeEngineering 
Source code of my INF237 homework

[Link to Kattis tasks](https://uib.kattis.com/courses/INF237/spring22)

## Temaer
* 01 	[Introduction](#introduction)
* 02 	[Graphs 1](#graphs-1)
* 03 	[Sliding, searching and sorting](#sliding-searching-and-sorting)
* 04 	[Dynamic programming 1](#dynamic-programming-1)
* 05 	[Graphs 2](#graphs-2)
* 06 	[Segment trees](#segment-trees)
* 07 	[Geometry 1](#geometry-1)
* 08 	[Exponential time algorithms](#exponential-time-algorithms)
* 09 	Dynamic programming 2
* 10 	Graphs 3
* 11 	Geometry 2
* 12 	Strings
* 13 	Mathematics

## Introduction
* [x] TwoSums
* [x] Greetings2
* [x] Tarifa
* [x] EarlyWinter
* [ ] EvenUpSolitaire

## Graphs 1
* [x] ThroughTheGrapevine
* [ ] FaultyRobot
* [x] Hoppers
* [ ] OneWayRoads

## Sliding, searching, and sorting 
* [x] Tired Terry
* [x] Firefly
* [ ] Kayaking Trip
* [ ] Film Critics

## Dynamic Programming 1
* [x] Spiderman's Workout
* [ ] Plane Ticket Pricing
* [x] Restaurant Orders
* [ ] Bridge Automation

## Graphs 2
* [x] Island Hopping
* [ ] Bumped
* [x] Detour
* [ ] Artwork

## Segment trees
* [x] Points of Snow
* [ ] Mega Inversions
* [x] Movie Collection
* [ ] Nekameleoni

## Geometry 1
* [x] Imperfect GPS
* [x] White Water Rafting
* [ ] Pesky Mosquitoes
* [ ] Cleaning Pipes

## Exponential time algorithms
* [ ] .
* [ ] .
* [ ] .
* [ ] .

## Ideas
### Introduction
#### TwoSums
Read two numbers, add them together
#### Greetings2
Check the number of e with count, multiply quantity by two
#### Tarifa
X gigabytes to spent per months, N months
The following months are quantity of data spent
Solution: Multiply (N+1)*X and substract every monthly value 
#### EarlyWinter
n years historical weather data and information d_i for every year about number of days between summer and snow

Find out number of consecutive years before this one with larger summer-snow gap
	
Solution: Enumerate through yearly data
- If number of that year larger than this year, increase counter
- If not, break up and return number of years
- If counter is still zero, then it never snowed that early

### Graphs 1
#### ThroughTheGrapevine
Spread a rumor to as many people as possible.
Every person has skepicism level.
It's number of people from which they want to hear the rumor before spreading it themselves.

One starting person spreads it to all people she knows (represented by graph)
Every day the next people who did hear it the day before spread it
Find out number of people who know the rumors

Solution:
- Generate adjacency list, skepticism dictionary and a dictionary about who told who'm already
- Make list of next spreaders containing only the starter
- Make a loop with amount of days.
- In each iteration, loop through next spreaders and get their neighbours.
- Add their spreader to the told_list and check skepticism level. If it is reached, mark them as a next_round_spreader
	
#### Hoppers
A new virus is spreading only two the neighbours of the neighbours of a infected computer.
Find out how many connections are missing such that one computer infects all
	
Solution:
- Find number of connected components via usage of BFS/DFS
- This needs n-1 links between them
- If the graph contains odd-cycle, it possible to spread all of them
- If there is no odd cycle, one more edge needs to be added to obtain that
- Odd cycle detection via bipartite graph detection, looping through the graph given all nodes colours
	
- In the end, return n or n-1 depending on the odd-cycle thing

### Sliding, searching, and sorting 

#### Tired Terry
Terry has a sleep pattern of size n (repeating) consisting of seconds of sleep (Z) or awakeness (W). Given a period of seconds p, how many seconds i are there for which intervals [i-p+1, i] he was sleeping for less than d seconds?
	
Solution:
- Append the list of letters by the length of p-1 and make a sliding window of size p over it
- Then count the appearences, compare it to d and count how often its less than d

- The pythonic way of fancy slicing does not get accepted due to horrible runtime
- This solution counts number of Z in first window and then just removes the first and adds the next letter to the z-counter

#### Firefly
There is cave with alternating stalagtites and stalagmites all having a length
There is a firefly flying horizontally at a chosen level, destroying all obsticles

Find out what is the minimum number of obsticles to destroy and how many of these levels with that number exist

Solution:
- Initialise two lists upper and lower (stalagtites and stalagmites) counting their length appearences
- Now add them together backwards (`[i-1] += [i]`) to make a cumulative list
- Reverse one of the lists and add them together
- Find the minimum value and how often it appears


### Dynamic Programming 1

#### Restaurant Orders
There are given a list of prices of dishes at a restaurant and a list of bill-sums. The task is to find out if it is possible to combine food to come up with that sum. If that is possible, output which elements are ordered or that this is ambiguous

Solution:
- The solution is knapsack style with weights=values.
- I create one big dynamic programming array with list size of the biggest bill
- Also, there is a data structure saving paths to each node.
- If there are multiple ways, the bill is ambiguous
- I ran into TimeLimit and MemoryLimit error, so there are a lot of weird tricks and data structure alterations to avoid that
- Inserting elements into the sorted path lists (sorted to compare them) happens by binary search
	
#### Spiderman' workout
There is a list of numbers which represent movements either up or down. Spiderman starts at level 0 and he does the moves in order, always going up or down. Find out if its possible to end the workout of movements at zero again, without getting below zero. If it is possible, find the order of moves of the solution with lowest maximum height.

Solution:
- For every testcase there is a dynamic programming table of size (number_of_moves) x (max_possible_height)
- The first column is zero and it loops through every move (column), creating new entries for every possible new height
- The stored value is the maximum observed height on that path
- When two paths merge into one node, we take the lowest maximum
- The solution is impossible if it did not arrive back at zero height
- If it is possible, loop backwards through the table, always taking the lowest maximum and appending "U" or "D" to the final string depending on the direction chosen

### Graphs 2
#### Island Hopping
There are n islands existing on a map and each of them has a coordinate (x,y) where one can start to build a bridge.
All islands should become connected and one needs to search the overall minimum length of all bridges to build.

Solution:
- This is a minimum spannung tree problem
- First we calculate all distances of all pairs and then use the algorithm of Prim to get the sum of bridge lengths

#### Detour
We drive from node 0 to node 1. There are many intersections and for each of them, there is an unique shortest path to 1.
We are not allowed to take any shortest direction at any intersection (node)
Print a path were this is possible or output impossible if there is no such path

Solution:
- Dijkstra to find the shortest edges from each node
- Then removing those nodes, we run a BFS

### Segment trees

#### Points of Snow
We live in a one dimensional country and receive both weather reports telling about falling snow and queries how much snow there is at one place. Snow falls in the range [a,b) (badly described)
Write a programme which stores these values and calculates the amount of snow at different places

Solution:
- Implementation of a segment tree with a range update and a point query
- The query is the sum of the path of a node up to the trees root
- The update goes to the leafs and works iteratively up to the parents depending if it is within the range or not

#### Movie Collection
There is a stack of movies with numbers 1 to n
Each time we are interested in a movie, the programme outputs at which position from the top the movie is situated
It then updates the positions of all movies

Solution:
- Implementation of a segment tree with a point update and a range query
- The original leaf length is the number of movies + number of coming requests
- Each leaf is either 0 or 1 depending if there is a movie there or not
- There is a dictionary (list) telling at which leaf position every movie is situated
- If a movie is requested, it sends a range query how many movies there are between its position and the top
- It then updates at two positions, removing the movie at its old position, putting it into the new one

### Geometry 1

#### Imperfect GPS
There are given coordinates and timestamps when a walker was at these positions.
Also, there is a time intervall at which GPS measures the positions.
Calculate how much the GPS distance differs from the real walking distance

Solution:
- There are four arrays, one for given points, one for the given timestamps
- The same exists for the GPS coordinates and time stamps.
- The GPS timestamps get calculated by the given intervall, the points are calculated given that.
- I loop through the GPS times and look if they have corresponding times in the original time array.
- If this is the case, I copy the points. If not, I use binary search to find the timestamps at the left and the right.
- From that, I calculate the point in between.
- Then, given these two point arrays, I calculate both sums of distances and return the difference of them.

#### White Water Rafting
There are an inner and an outer polygon, which do not touch each other.
Moreover, there is a circular raft which rafts through the inner path between those polygons.
Find the biggest possible radius of the raft s.t. this is possible

Solution:
- Go through each pair of points from one polygon and line segments from the other (2 times for each way around)
- Calculate the distance between them and output the minimum of all
- Calculating the distance is done by known line-to-point-distance formula

- Problem: What if perpendicular intersection point outside of line segment?
- Calculate intersection value (how far from the left boundary is point on line?):
- If < 0, its outside on the left, if > 1, its outside on the right
- In this situation set intersection point to the boundary
- Then return the distance between that intersection point and the original one

### Exponential time algorithms