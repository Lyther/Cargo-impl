# Program to generate organization from customers.
# The input file should be customer information in instance file.
# The output is `organization id` `customer id`.
# The customers have the same source or destination are considered to be in
# the same organization.

target = input('Please input the instance file name (without extension): ')

fin = open(target + '.instance')
fout = open(target + '.organization', 'w')

customers = fin.readlines()
is_visited = []
start = int(customers[2].split()[1]) + 6
for i in range(len(customers)):
    is_visited.append(0)
oid = 0
network = []
for i in customers[start:]:
    info = i.split()
    cid = int(info[0])
    src = info[1]
    dst = info[2]
    typ = info[3]
    ely = info[4]
    lte = info[5]
    if is_visited[cid] == 1:
        continue
    print('Finding neibours of', str(cid), 'src', src, 'dst', dst)
    is_visited[cid] = 1
    org = [cid]
    for j in customers[start:]:
        _info = j.split()
        _cid = int(_info[0])
        _src = _info[1]
        _dst = _info[2]
        _typ = _info[3]
        _ely = _info[4]
        _lte = _info[5]
        if is_visited[_cid] == 1:
            continue
        if _src == src or _dst == dst or _src == dst or _dst == src:
            print('Found', str(_cid), 'src', _src, 'dst', _dst)
            is_visited[_cid] = 1
            org.append(_cid)
    oid += 1
    for j in org:
        network.append(str(oid) + '\t' + str(j))
print('ORGANIZATIONS', oid, file=fout)
print('\nID\tCUSTOMER', file=fout)
for i in network:
    print(i, file=fout)
