# Cargo: RSP Benchmark - Handbook

latest update : 2019/11/23

----

raw references

Cargo source code :  https://github.com/jamjpan/Cargo 

Cargo benchmark data : https://github.com/jamjpan/Cargo_benchmark 

-----

## Outline

1. Read Data From File
2. Use `gnuplot` to Draw The Network
3. RSAlgotithm Development









## 1. Read Data From File

### Read Nodes and Edges

file extension : `*.edges`

The content of the file should be like this:

```json
<# of nodes> <# of edges>
0 1 60
1 2 125
2 0 300
...
```

The first line will be skipped by the reading function. (read_edges() in src/file.cc) 

For the rest of the lines below, the first number is the node id of `node_1`, the second number of the node id of `node_2` and the third number is the weight of this edge.

 

### Read Network

file extension : `*.rnet`

The content of the file should be like this:

```json
<edge id> <node_1> <node_2> <lng1> <lat1> <lng2> <lat2>
<edge id> <node_1> <node_2> <lng1> <lat1> <lng2> <lat2>
<edge id> <node_1> <node_2> <lng1> <lat1> <lng2> <lat2>
....
```

`edge id` : a 0-indexed ID for the edge

`node_1`   : the ID of node_1 from edges file

`node_2`   : the ID of node_2 from edges file

`lng1`       : longitude of node_1

`lat1`       : latitude of node_1

`lng2`       : longitude of node_2

`lat2 `       : latitude of node_2 











## 2. Use gnuplot to Draw The Network

### Install gnuplot

Find the latest version and suitable installer for your OS:  http://gnuplot.sourceforge.net/ 

(For windows users, click `Add gnuplot to environment` when during installation setting.)



### Draw network by using gnuplot command

Input the command below to draw `bj5.rnet` network.

`gnuplot -persist -e "plot 'bj5.rnet' u 4:5:($6-$4):($7-$5) w vectors nohead"`











## 3. RSAlgorithm Development

### Data structure 

*g-tree,* *grid.*

Basic idea : Use *g-tree* to accelerate the shortest path query, and use *grid* to store vehicles and query speed up candidate filtering process. 

The hash value of a vehicle in the grid is computed by its last visited node.



### Framework

```C++
while(active):
	listen();
	for each vehicle():
		handle_vehicle();
	for each customer():
		handle_customer();
	match:
		//Match logic
	Sleep until next batch
```

There are four virtual function may need to be override

##### listen

```C++
virtual void listen(bool skip_assigned = true, bool skip_delayed = true);
```

Polls for active vehicles and waiting customers at a configurable interval, storing them locally.



##### handle_customer

```C++
virtual void handle_customer(const Customer &);
```

Executed automatically on every customer that is polled via **listen()**.



**handle_vehicle**

```C++
virtual void handle_vehicle(const Vehicle &);
```

Executed automatically on every vehicle that is polled via **listen()**.



**match**

```C++
virtual void match();
```

Executed at the end of every **listen()** and can be used for join-based assignment.



**end**

```C++
virtual void end();
```

Execute after the simulation finishes.



### Candidate Filtering

Candidates Filtering example:

```C++
void NearestNeighbor::handle_customer(const Customer& cust) {
  this->reset_workspace();                  // reset workspace variables
  this->candidates =                        // collect candidates
    this->grid_.within(pickup_range(cust), cust.orig()); // (functions.h, grid.h)
  
  ...
}
```

Function pick_range() is used to calculate the least time that the vehicle need to move **from the origin of the customer to the destination of the customer**. Here is the source code of pick_range() (src/functions.cc):

```C++
DistInt pickup_range(const Customer& cust) {
  return Cargo::vspeed() * cust.late() - Cargo::basecost(cust.id()) -
         Cargo::vspeed() * Cargo::now();
}
```



### Customer Insertion

Simple Customer Insertion example:

```C++
sop_insert(*cand, cust, sch, rte, Cargo::gtree())
```

