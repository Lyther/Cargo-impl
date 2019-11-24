### The architecture of our model

This may be helpful for you to write report.

----

## Abstract

To solve the problem: time arrangement doesn't work well.

There would be several parts in our project:
- problem definition
- digital-twin based architecture
- data from real world
- algorithm to arrange schedule
- simulator
- database
- Cargo test result
- summary
Add more math denotions may be better.

Be aware in this report, we should introduce our task distribution!

----

## Problem Definition

I name our problem of bus schedule problem (BSP), there would be several differences between BSP and RSP, but they still have a lot of commons.

Differences:

- the schedule of the vehicle (bus route) is static.
- vehicles don't have time window
- bus capacity is much larger than other vehicle
- edge weight doesn't equal in different directions
- not every can get in the bus, penalty is needed to measure the quality of the problem solver.

Graph of vertices as stations and edges as route is the same as RSP. This problem also needs online algorithms to solve.



### Formalization

The route of the buses is fixed. To simplify the problem, every bus use the same route. If a bus arrives at the destination, then it will turn back along with the reverse route, and it will back to the destination when this bus arrives at the origin again.

A customer have a time window $[e, l]$, a customer cannot be picked up before time $e$ and cannot arrives after $l$ (which means if this customer cannot arrive at destination on time, he/she would not get in the bus).

The objective is to maximize the number of satisfactory requests. In another words, we should do our best to meet the expectation of customers as many as possible.



The problem can be formalized as:
$$
\max_{\tau \subseteq T }\sum_{t \in \tau}P(t)
$$
where $T$ is a set of time that a bus can depart from its origin, $\tau$ is a set of time we choose to let the bus depart from its origin, while $|\tau| = \#\ of\ buses$. $P$ is the profit function relating to the number of customers that the bus can pick up if a bus depart from time $t$. 

Calculating the profit function is $\#P$. Choosing the time of the first departure time of buses is NP hard.

----

## Digital-twin based architecture

The goal of BSP is to arrange time schedule according to already known information.
The algorithm should plan: `whether or not send a bus`, `which direction of bus`, `*the bus is normal or peak*`, `*how long would bus stops at each station*`.
The basic concept of algorithm is:

```Algorithm
get buses status
get students number
analyze and make decision
update database```

To measure the quality of arrangement, there would be several targets.
​```Total time cost
Percentage students arrive in time
Total bus arrange number
Average students number on bus```

The simulator is based on real data and communicates with algorithm through in-memory database, the architecture of simulator thread is:
​```Simulator
increase time counter
move buses
move students
handle pick up & drop off
update database```

All the communications are through in-memory database, the data stored and their types are:
​```Database
buses: id integer, position integer, load integer, capacity integer, status integer, waiting integer array, direction integer, type integer
students: id integer, position integer, early_time integer, late_time integer, destination integer```
Here is some description. ID of buses and students is unique identifier. Bus position is an integer indicates the station it here or left, the exact position is unknown, but we can judge the bus can handle pick up or not by using 'status' column. Load is the current number of students on bus, which should not exceed upper bound capacity.
Status -1 means bus doesn't work now, 0 means running on the way, and 1 means it stops at station and waiting. Waiting is an integer array means how long would this bus stops at each station. Direction 0 means Joy Highland to RB1, while 1 means RB1 to Joy Highland. Type 0 means the bus is normal line, and 1 means the bus is peak line.
Then position of student is the exact number of station the student is. Early_time of student is the earliest time the student can arrive the station, while late_time is the latest time the student should arrive destination. The destination is the number of station the student should go to.
Note that all the time is denoted by integer. Time starts from 0, and increase along with simulation, in unit of second. The integer array cannot store directly into database, so dumps may used to store array.

----

## Data from real world

Data is based on real dataset, which collected from SUSTech school bus. The data we need to know is `station information and routes`, `edge weight between stations`, `number of students waiting at station`, `*students' destination, time window*`.
In one word, all the data in database should be in consideration.

The difficulties in the data collection is that:
- how to find destination and time window
- how to calculate current number of students waiting at station

One solution is to use course timetable, then we would know how many students will appear in specific station, and guess their destination and time window. But this doesn't good enough, so we should find more ways to collect data.

----

## Algorithm to arrange schedule

The data the algorithm can know:
- current buses status
- how many studetns are waiting at each station (but without time window or destination)
- course schedule (optional)

----

## Simulator

Simulator, algorithm, and database are running parallel as multi-thread. The simulator would read in data and then send them to database. After that, threads are running parallel until the simulation finish.
I will give a pseudo code here later, the current one is:
​```Simulator
initial & read / write data
loop:
	start threads
	wait all tasks finish
write result to file```
The pseudo code for each thread is shown above (digital-twin based architecture).

Simulator would construct in C++ to achieve more efficiency. For the current tests, we use Cargo ridesharing system to simulate school bus.

----

## Database

Based on read data, but we are trying to communicate with the university, and current data is half real and half pseudo real. 

----

## Cargo test result

Use Cargo system to run tests in our campus map and data. 12 RSP algorithms are used to run the test, and conpare results.

----

## Summary

Our task distribution and future plans:
- build up our simulation platform
- collect data from real bus
- design algorithm to fit BSP
```