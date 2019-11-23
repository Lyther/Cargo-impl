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
    data = js['obj']['allPoint']
    points = data.split(';')

    # print out
    for point in points:
        cache = point.split(',')
        print('{lat:', cache[1], ',lng:', cache[0], '}', sep='', end=',')

if __name__ == "__main__":
    if len(sys.argv) == 2:
        in_file = sys.argv[1].strip()
    else:
        print('Usage: python pos-to-json.py <file>')
    convert()