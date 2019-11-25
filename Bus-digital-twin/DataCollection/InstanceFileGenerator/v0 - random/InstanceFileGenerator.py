import random
import time

random.seed(time.time())

f = open('dtSchoolBus.instance', 'w')

veh_cnt = 20
cus_cnt = 10_000
capacity = 100

dormitories = [0, 3, 4, 7]
classrooms = [3, 12, 13]
classTime = [
    [], # 8:00 - 9:50
    [], # 10:20 - 12:10
    [], # 14:00 - 15:50
    [], # 16:20 - 18:10
    [], # 19:00 - 20:50
]

# Line 1: (instance name)
f.write('digital-twin-instance\n')
# Line 2: (road network) TAXI
f.write('dtSchoolBus TAXI\n')
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
# all customer have Q = 1
# EARLY and LATE will be generated randomly
for i in range(cus_cnt):
    orig = random.randint(0, 13)
    dest = random.randint(0, 13)
    while orig == dest:                 # no in-place travelling
        dest = random.randint(0, 13)
    early = random.randint(0, 57599)    # 16h -> 57600s
    late = random.randint(early, 57600)
    line = '{}\t{}\t{}\t{}\t{}\t{}\n'.format(id, orig, dest, 1, early, late)
    f.write(line)
    id += 1
f.close()
