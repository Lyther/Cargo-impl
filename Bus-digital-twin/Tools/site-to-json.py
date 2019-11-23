import sys
import json

in_file = ''

def convert():
    # process in_file
    if in_file != '':
        f = open(in_file, 'r', encoding='utf-8')
        content = f.read()
        f.close()
    else:
        content = input('Type in json text: ')

    # trim useful data
    js = json.loads(content)
    data = js['obj']
    points = []
    for site in data:
        points.append((site['stationLat'], site['stationLng']))

    # print out
    for point in points:
        print('{lat:', point[0], ',lng:', point[1], '}', sep='', end=',')

if __name__ == "__main__":
    if len(sys.argv) == 2:
        in_file = sys.argv[1].strip()
    else:
        print('Usage: python site-to-json.py <file>')
    convert()