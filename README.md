# INF237-AlgoritmeEngineering 
Source code of my INF237 homework
[Link to Kattis tasks](https://uib.kattis.com/courses/INF237/spring22)

## Temaer
* 01 	Introduction
* 02 	Graphs 1
* 03 	Sliding, searching and sorting
* 04 	Dynamic programming 1
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