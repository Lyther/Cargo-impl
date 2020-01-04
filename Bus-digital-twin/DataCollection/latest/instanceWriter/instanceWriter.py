from excelReader import ExcelReader

er = ExcelReader()
er.decodeItems()

instance_name = 'rs-dt-m1k-c60-d6-s6-x1.0'
dep_label = 'dt'
veh_cnt = 30
capacity = 40

def writeInstanceFile(weekNum, dayNum):
    filename = 'output/{}_{}_{}.instance'.format(instance_name, weekNum, dayNum)
    f = open(filename, 'w')
    
    items = er.items[weekNum][dayNum]
    cus_cnt = len(items)

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
    # now students
    # lots of things have been done in excelReader.py
    for item in items:
        line = '{}\t{}\t{}\t{}\t{}\t{}\n'.format(id, item[0], item[1], 1, item[2], item[3])
        f.write(line)
        id += 1
    
    f.close()
    print('finish writing {}'.format(filename))
    
if __name__ == '__main__':
    for weekKey in er.items:
        for dayKey in er.items[weekKey]:
            writeInstanceFile(weekKey, dayKey)