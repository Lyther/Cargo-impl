import sys
import numpy

dat = []
sol = []
als = None
scd = None


def main():
    veh_num = int(sol[2].split()[-1].strip())
    total_time = int(dat[-1].split()[0]) + 1
    table = numpy.zeros((veh_num, total_time), numpy.int)
    for i in dat:
        inf = i.split()
        if inf[1] == 'V':
            table[int(inf[2]) - 1][int(inf[0])] = int(inf[3])
    analyze(table)


def analyze(table):
    print('==== Analysis Result ====', file=als)
    print('==== Time Schedule ====', file=scd)
    for i in range(len(table)):
        print('\n================================================\n', file=als)
        print('\n================\n', file=scd)
        start = False
        last_time = 0
        last_station = 0
        for j in range(len(table[i])):
            if table[i][j] != 0 and table[i][j] > last_station:
                if start:
                    print('[WAITED] Vehicle %d waited at station %d for %d seconds.'
                          % (i + 1, last_station, j - last_time), file=als)
                    print('[STATION %d] Wait %d minutes.' % (last_station, (j - last_time) // 60), file=scd)
                    print('[MOVE] Vehicle %d moves to station %d at time %d.' % (i + 1, table[i][j], j), file=als)
                    last_time = j
                    last_station = table[i][j]
                else:
                    print('[START] Vehicle %d starts to move at time %d.' % (i + 1, j), file=als)
                    print('[SCHEDULE %d] Start time %s.' % (i + 1, get_time(j)), file=scd)
                    start = True


def get_time(t):
    s = ''
    if t >= 3600:
        s = s + str(t // 3600) + ':'
        t = t % 3600
    else:
        s = '0:'
    if t >= 60:
        s = s + str(t // 60)
    return s


if __name__ == '__main__':
    if len(sys.argv) == 2:
        dat = open(sys.argv[1]).readlines()
        sol = open(sys.argv[1].replace('.dat', '.sol')).readlines()
        als = open(sys.argv[1].replace('.dat', '.als'), 'w')
        scd = open(sys.argv[1].replace('.dat', '.scd'), 'w')
        main()
        als.close()
        scd.close()
    else:
        print('Usage: python analysis.py <dat_file>')
