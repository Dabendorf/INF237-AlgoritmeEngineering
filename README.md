# INF237-AlgoritmeEngineering 
Source code of my INF237 homework

[Link to Kattis tasks](https://uib.kattis.com/courses/INF237/spring22)

## Temaer
* 01 	[Introduction](#introduction)
* 02 	[Graphs 1](#graphs-1)
* 03 	[Sliding, searching and sorting](#sliding-searching-and-sorting)
* 04 	[Dynamic programming 1](#dynamic-programming-1)
* 05 	Graphs 2
* 06 	Segment trees
* 07 	Geometry 1
* 08 	Exponential time algorithms
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
* [ ] Plane Ticket Pricing
* [ ] Spiderman's Workout
* [x] Restaurant Orders
* [ ] Bridge Automation

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
	