# INF237-AlgoritmeEngineering 
Source code of my INF237 homework<br/>
[Link to Kattis tasks](https://uib.kattis.com/courses/INF237/spring22)

## Temaer
* 01 	[Introduction](#introduction) ([Problems](#introduction-1))
* 02 	[Graphs 1](#graphs-1) ([Problems](#graphs-1-1))
* 03 	[Sliding, searching and sorting](#sliding-searching-and-sorting) ([Problems](#sliding-searching-and-sorting-1))
* 04 	[Dynamic programming 1](#dynamic-programming-1) ([Problems](#dynamic-programming-1-1))
* 05 	[Graphs 2](#graphs-2) ([Problems](#graphs-2-1))
* 06 	[Segment trees](#segment-trees) ([Problems](#segment-trees-1))
* 07 	[Geometry 1](#geometry-1) ([Problems](#geometry-1-1))
* 08 	[Exponential time algorithms](#exponential-time-algorithms) ([Problems](#exponential-time-algorithms-1))
* 09 	[Dynamic programming 2](#dynamic-programming-2) ([Problems](#dynamic-programming-2-1))
* 10 	[Graphs 3](#graphs-3) ([Problems](#graphs-3-1))
* 11 	[Geometry 2](#geometry-2) ([Problems](#geometry-2-1))
* 12 	[Strings](#strings) ([Problems](#strings-1))
* 13 	[Mathematics](#mathematics) ([Problems](#mathematics-1))

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
* [x] Social Advertising
* [x] Map Colouring
* [ ] Holey N-Queens (Batman)
* [ ] Rubik's Revenge in ... 2D!? 3D?

## Dynamic Programming 2
* [x] The Citrus Intern
* [ ] Pokemon Go Go
* [ ] Allergy Test
* [ ] Mag
* [x] Wildcard

## Graphs 3
* [x] Paintball
* [x] Piano Lessons
* [x] Water
* [ ] The Darkness

## Geometry 2
* [x] Dart Scoring
* [ ] Finding Lines
* [ ] Closest Pair
* [x] Robert Hood

## Strings
* [ ] 
* [ ] 
* [ ] 
* [ ] 

## Mathematics
* [ ] 
* [ ] 
* [ ] 
* [ ] 

## Ideas
### Introduction
#### TwoSums
Read two numbers, add them together
#### Greetings2
Check the number of e with count, multiply quantity by two
#### Tarifa
X gigabytes to spent per months, N months<br/>
The following months are quantity of data spent

Solution: Multiply (N+1)*X and substract every monthly value 
#### EarlyWinter
n years historical weather data and information d_i for every year about number of days between summer and snow<br/>
Find out number of consecutive years before this one with larger summer-snow gap
	
Solution: Enumerate through yearly data
- If number of that year larger than this year, increase counter
- If not, break up and return number of years
- If counter is still zero, then it never snowed that early

### Graphs 1
#### ThroughTheGrapevine
Spread a rumor to as many people as possible.<br/>
Every person has skepicism level.<br/>
It's number of people from which they want to hear the rumor before spreading it themselves.<br/>
One starting person spreads it to all people she knows (represented by graph)<br/>
Every day the next people who did hear it the day before spread it<br/>
Find out number of people who know the rumors

Solution:
- Generate adjacency list, skepticism dictionary and a dictionary about who told who'm already
- Make list of next spreaders containing only the starter
- Make a loop with amount of days.
- In each iteration, loop through next spreaders and get their neighbours.
- Add their spreader to the told_list and check skepticism level. If it is reached, mark them as a next_round_spreader
	
#### Hoppers
A new virus is spreading only two the neighbours of the neighbours of a infected computer.<br/>
Find out how many connections are missing such that one computer infects all
	
Solution:
- Find number of connected components via usage of BFS/DFS
- This needs n-1 links between them
- If the graph contains odd-cycle, it is possible to spread to all of them
- If there is no odd cycle, one more edge needed to be added to obtain that
- Odd cycle detection via bipartite graph detection, looping through the graph given all nodes colours
	
- In the end, return n or n-1 depending on the odd-cycle thing

### Sliding, searching, and sorting 

#### Tired Terry
Terry has a sleep pattern of size n (repeating) consisting of seconds of sleep (Z) or awakeness (W).<br/> 
Given a period of seconds p, how many seconds i are there for which intervals [i-p+1, i] he was sleeping for less than d seconds?
	
Solution:
- Append the list of letters by the length of p-1 and make a sliding window of size p over it
- Then count the appearences, compare it to d and count how often its less than d

- The pythonic way of fancy slicing does not get accepted due to horrible runtime
- This solution counts number of Z in first window and then just removes the first and adds the next letter to the z-counter

#### Firefly
There is cave with alternating stalagtites and stalagmites all having a length<br/>
There is a firefly flying horizontally at a chosen level, destroying all obsticles<br/>
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
There are n islands existing on a map and each of them has a coordinate (x,y) where one can start to build a bridge.<br/>
All islands should become connected and one needs to search the overall minimum length of all bridges to build.

Solution:
- This is a minimum spannung tree problem
- First we calculate all distances of all pairs and then use the algorithm of Prim to get the sum of bridge lengths

#### Detour
We drive from node 0 to node 1. There are many intersections and for each of them, there is an unique shortest path to 1.<br/>
We are not allowed to take any shortest direction at any intersection (node)<br/>
Print a path were this is possible or output impossible if there is no such path

Solution:
- Dijkstra to find the shortest edges from each node
- Then removing those nodes, we run a BFS

### Segment trees

#### Points of Snow
We live in a one dimensional country and receive both weather reports telling about falling snow and queries how much snow there is at one place. Snow falls in the range [a,b) (badly described)<br/>
Write a programme which stores these values and calculates the amount of snow at different places

Solution:
- Implementation of a segment tree with a range update and a point query
- The query is the sum of the path of a node up to the trees root
- The update goes to the leafs and works iteratively up to the parents depending if it is within the range or not

#### Movie Collection
There is a stack of movies with numbers 1 to n<br/>
Each time we are interested in a movie, the programme outputs at which position from the top the movie is situated<br/>
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
There are given coordinates and timestamps when a walker was at these positions.<br/>
Also, there is a time intervall at which GPS measures the positions.<br/>
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
There are an inner and an outer polygon, which do not touch each other.<br/>
Moreover, there is a circular raft which rafts through the inner path between those polygons.<br/>
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

#### Social Advertising
There are n people and each of them has a list of friends.<br/>
We would like to post advertisements on their social media wall which all of their friends are going to see (including themselves)<br/>
Find the minimum amount of people to post advertisement to such that all peopel are reached

Solution:
- After reading friend lists, one converts friend lists into binary strings (integers)
- Person x is 2**(x-1), e.g. {1,4,5} is 1+8+16=25
- If we have n people, we need to reach to number 2**n-1 by logical OR on an amount of subsets (represented by integer)
- At first I prune duplicates (same friend lists) and go through pairs of them and remove numbers which are subsets of others
- In the end, I loop through each size from 2 to n and try for each combination if they output 2**n-1 after logical or
- If this is the case, the loop breaks and the minimum number is found

#### Map Colouring
Colour a map. Determine how many colours are needed. If more than 4 are needed, just output "many"

Solution:
- There are some initial if conditions to make things easier
- If there are no edges, only one colour is needed
- If graph is fully connected, it needs as many colours as nodes
- I reused my bipartite matching algorithm to check if something is 2-colourable
- If nothing of these works, it checks if the graph is 3 colourable or 4 colourable
- If none of these work, it returns "many"

Functionality of the {3,4}-colourable algorithm:
- The algorithm takes five arguments, which are the adjacency list, the colour list, the number of colours and the number of nodes
- The fifth one changes in each recursion step, which is the number of the current node going up
- The base case is that the current node number is bigger than the number of nodes, so every node got colours
- Otherwise, the algorithm goes through all colours and tries each of them on the node
- If a neighbour has the same colour, this recursion step gets trashed, if there is an success, the algorithm continues recursively with the next node

### Dynamic programming 2
#### The Citrus Intern
A companies structure is built up like a tree with every person having up to one boss and several subordinates<br/>
We want every person in the company to be controlled by either being bribed or having a "talk" to a bribe boss or subordinate<br/>
Every bribed person talks to his/her boss and the subordinates<br/>
No two people talking with each other should be bribed at the same time and the money spend on bribery should be minimised<br/>
<br/>
Indendent Set & Dominating Set, see INF234 weighted independent set on trees<br/>
<br/>
Solution:
- First: Find the root node and the postorder of the tree structure.
- Finding root: Start at the leafes and go up until one does not have a boss anymore
- Postorder: Using DFS, returning a stack of postorder. This way, one can start dynamic programming at the leafes going up

- Now, its a dynamic programming problem. There are three 1D-lists being:
- m_bribe[u]: The money spent until u if u gets bribed
- m_notbribed[u]: The money spent until u if u is not bribed
- m_notbribed_butchild[u]: The money spent until u if u is not bribed but at least one of the child
- The latter one is relevant such that there is no hole in the tree where one person is not bribed
 
- Base case: For every leaf u: m_bribed[u] = m_notbribed_butchild[u] = w_u; m_notbribed[u] = 0
- Recurrance:
- m_bribed[u] = sum of all neighbours v not being bribed + bribing money of u
- m_notbribed[u] = sum of all neighbours v with value of the minimum of v being bribed or a child of v behind bribed
- m_notbribed_butchild[u] = minimum bribing value of neighbour which is sum of not bribing u but bribing v + the minimum of bribing v or not bribing v but its children
- It is basically not taking u and then calculating which child to take
- The best child is that one which has minimum cost of taking it, it is a merging of branches

- The final output is the minimum of bribing v or one of its children

### Graphs 3
#### Paintball
There are people playing Paintball and we are given pairs of people who can see (shoot) each other<br/>
Every player has one bullet, find out of everyone can take a bullet

Solution:
- Bipartite matching via flow networks
- Read in every person two times, one for each bipartite set (because everybody shoots and gets shot)
- Connect one set with a new node called "s" and one with a new node called "t"
- Run Ford-Fulkerson (Edmonds-Karp) from "s" to "t"
- Then go through all original edges and look if the opposite edge exists in the residual graph
- If so it means that this is an edge in the bipartite matching
- Give out "Impossible" if maxflow is not number of players

#### Piano Lessons
There are people wanting to take piano lessons and each has n time slots working for them.<br/>
Each timeslot only accepts one student.<br/>
Find the maximum number of students who can get piano lessons<br/>
<br/>
Solution:
- Bipartite matching via flow networks
- The people are set A and the piano lessons set B
- Connect one set with a new node called "s" and one with a new node called "t"
- Run Ford-Fulkerson (Edmonds-Karp) from "s" to "t"
- Then go through all original edges and look if the opposite edge exists in the residual graph
- If so it means that this is an edge in the bipartite matching
- Output the maximum flow

#### Water
There is a flow network existing, using pumping stations.<br/>
This means flow can go in both directions in each edge.<br/>
Calculate the maximum flow from node 1 to node 2<br/>
There will be k "improvements" which means that the edge capacities will increase (or start to exist)<br/>
Give out k more numbers being the new network flows after each improvement<br/>

Solution:
- Straight forward Ford-Fulkerson (Edmonds-Karp) from 1 to 2
- Difference is that we initialise each edge in both directions and also each residual edge in both
- Then run the flow network and output the maxflow
- Each improvement just adds the extra capacity to both the two edges and two residual edges
- For every improvement, run the maxflow algorithm again (will only run for one bfs?)
- The new maxflow is the sum of the maxflow from before and the new one

### Geometry 2
#### Dart Scoring
The task is to find the length of the hull of a big number of points and then calculate a fancy point sum by a given formula.<br/>
<br/>
Solution:<br/>
- This makes use of the Graham Scan algorithm. 
- One sorts all points by x-value (break tie by y-value)
- Then we calculate both an upper hull and a lower hull both times through the same process
- In the first one, we go through the sorted points and in the second one through the reversed order
- We add all points to the hull with have certain properties.
- We try to find out of three points are in a left angle which is the same as finding out if they are inner points or outside hull points
- Finally, we calculate the length of the hull by going around the hull and add distances and put them into the formula
- This is possible since Graham scan adds points to the hull in order

#### Robert Hood
The task is to find the maximum distance of two points in a big number of points.<br/>
<br/>
Solution:<br/>
- This makes use of the Graham Scan algorithm. 
- One sorts all points by x-value (break tie by y-value)
- Then we calculate both an upper hull and a lower hull both times through the same process
- In the first one, we go through the sorted points and in the second one through the reversed order
- We add all points to the hull with have certain properties.
- We try to find out of three points are in a left angle which is the same as finding out if they are inner points or outside hull points
- Finding the two points with maximum distance is the same as finding two points with maximum distance in the hull of that set

- Finding the maximum distance inside the hull works with two for-loops
- Go through hull with two for-loops with points being on "opposite" position
- If the inner distance for point 2 gets bigger than what we current have, we break that inner loop and continue with next outer point

### Strings


### Mathematics

