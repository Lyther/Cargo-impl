import random
import time
import math

random.seed(time.time())

total_students_cnt = 8000
students_take_bus_rate = 0.5
avg_bus_takes_per_student = 4
bus_takes_freq = avg_bus_takes_per_student / 7

instance_name = 'rs-dt-m1k-c100-d6-s6-x1.0'
dep_label = 'dt'
veh_cnt = 25
# actual requests -> among all students, some of them take buses, 
# each student takes some times a day
cus_cnt = int(total_students_cnt * students_take_bus_rate * avg_bus_takes_per_student)
capacity = 40

# 7:00 - 23:00
minTime = 0
maxTime = 57600    # 16h -> 57600s

all_locations = [i for i in range(0, 14)]
dormitories = [0, 3, 4, 7]
classrooms = [3, 12, 13]
classTime = [
    [3600, 10200], # 8:00 - 9:50
    [12000, 18600], # 10:20 - 12:10
    [25200, 31800], # 14:00 - 15:50
    [33600, 40200], # 16:20 - 18:10
    [43200, 49800], # 19:00 - 20:50
    [50400, 53400], # 21:00 - 21:50
]
passageWindows = [
    [0, 3600],
    [10200, 12000],
    [18600, 25200],
    [31800, 33600],
    [40200, 43200],
    [49800, 50400],
    [53400, 57600]
]

f = open('{}.instance'.format(instance_name), 'w')

# Line 1: (instance name)
f.write(instance_name + '\n')
# Line 2: (road network) TAXI
f.write('{} TAXI\n'.format(dep_label))
# Line 3: VEHICLES (number of vehicles)
f.write('VEHICLES ' + str(veh_cnt) + '\n')
# Line 4: CUSTOMERS (number of customers)
f.write('CUSTOMERS ' + str(cus_cnt) + '\n')
# Line 5: (blank line)
f.write('\n')
# Line 6: (header row)
f.write('ID\tORIGIN\tDEST\tQ\tEARLY\tLATE\n')
# Line 7-end: vehicles and customers
# now some other things...
id = 1  # id starts from 1
# All of the buses begin their journey at JH (ORIGIN=0), 
# and they do not necessarily have a destination(DEST=-1)
# All school buses can take `capacity` people, so (Q=-capacity) for all these buses
# we assume all buses can leave at the beginning (EARLY = 0), 
# and they do not have service finish time (LATE = -1)
while id <= veh_cnt:
    line = '{}\t{}\t{}\t{}\t{}\t{}\n'.format(id, 0, -1, -capacity, 0, -1)
    f.write(line)
    id += 1
# we assume people are distributed uniformly at these places at first: [JH, LH, NSD, EA]
# there are several classrooms: [LH, G7, RB]
# consider the time students are not taking courses, there are 7 time windows for travelling
# all customer have Q = 1
# EARLY and LATE will be generated randomly
# For students travelling by bus, if they take the bus at a certain time window:
# 30% from classrooms to classrooms, 30% from classrooms to dorms, 30% from dorms to classrooms, 10% random travel
# 1. Initially, all students are uniformly distributed in all dormitory areas
#    In this occasion, 75% from dorms to classrooms, 10% random travel
piece = int(cus_cnt / len(passageWindows))
left = cus_cnt % len(passageWindows)
for i in range(piece + math.floor(left / 2)):
    orig = dormitories[i % len(dormitories)]
    dest_choices = classrooms if random.random() <= 0.75 else all_locations
    dest = random.choice(dest_choices)
    while orig == dest:
        dest = random.choice(dest_choices)
    early = random.randint(passageWindows[0][0], passageWindows[0][1]-1)
    late = random.randint(early, passageWindows[0][1])
    line = '{}\t{}\t{}\t{}\t{}\t{}\n'.format(id, orig, dest, 1, early, late)
    f.write(line)
    id += 1
# 2. for the rest time windows except the final one, the rules apply as general occasions
for i in range(1, len(passageWindows)-1):
    for j in range(piece):
        judge_val = random.random()
        if judge_val <= 0.3:
            orig_choices = classrooms
            dest_choices = classrooms
        elif judge_val <= 0.6:
            orig_choices = classrooms
            dest_choices = dormitories
        elif judge_val <= 0.9:
            orig_choices = dormitories
            dest_choices = classrooms
        else:
            orig_choices = all_locations
            dest_choices = all_locations
        orig = random.choice(orig_choices)
        dest = random.choice(dest_choices)
        while orig == dest:
            dest = random.choice(dest_choices)
        early = random.randint(passageWindows[i][0], passageWindows[i][1]-1)
        late = random.randint(early, passageWindows[i][1])
        line = '{}\t{}\t{}\t{}\t{}\t{}\n'.format(id, orig, dest, 1, early, late)
        f.write(line)
        id += 1
# 3. In the last time window, there destinations should be dormitories, 
#    and of course, uniformly distributed.
#    In this occasion, 75% from classrooms to dorms, 10% random travel
for i in range(piece + math.ceil(left / 2)):
    orig_choices = classrooms if random.random() <= 0.75 else all_locations
    dest_choices = dormitories
    orig = random.choice(orig_choices)
    dest = random.choice(dest_choices)
    while orig == dest:
        dest = random.choice(dest_choices)
    lastWindow = passageWindows[len(passageWindows)-1]
    early = random.randint(lastWindow[0], lastWindow[1]-1)
    late = random.randint(early, lastWindow[1])
    line = '{}\t{}\t{}\t{}\t{}\t{}\n'.format(id, orig, dest, 1, early, late)
    f.write(line)
    id += 1

f.close()
