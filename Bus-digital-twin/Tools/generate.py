import sys
import numpy

dat_file = ''
tot_time = 0
tot_sta = 0

# This file is used to generate time table from routes.


def main():
    bus = numpy.zeros((tot_sta, tot_time), numpy.int)
    for line in dat_file:
        inf = line.split()
        if inf[1] == 'V':
            try:
                bus[int(inf[3])][int(inf[0])] += 1
            except:
                print('[ERROR] Exception at line: %s' % inf)
    print_result(bus)


def print_result(bus):
    tar = open(sys.argv[1].replace('.dat', '.scd'), 'w')
    print('Total time measured %d, total stations considered %d.' % (tot_time, tot_sta), file=tar)
    print('\nStation\tTime\tBuses\n', file=tar)
    for i in range(tot_sta):
        for j in range(tot_time):
            if bus[i][j] != 0:
                print('%d\t%d\t%d' % (i, j, bus[i][j]), file=tar)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        dat_file = open(sys.argv[1])
        tot_time = int(sys.argv[2])
        tot_sta = int(sys.argv[3])
    else:
        print('Usage: python generate.py <target_dat_file> <total_time> <station number>')
        sys.exit(0)
    main()
