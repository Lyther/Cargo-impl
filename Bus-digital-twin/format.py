def main():
    f = open('example.dat', 'r')
    content = f.readlines()
    f.close()
    f = open('example.js', 'w')
    for i in content:
        coordinate = i.split('  ')
        lat = coordinate[1].strip()
        lng = coordinate[0].strip()
        f.write('{lat: ' + lat + ',lng: ' + lng + '},')
    f.close()

if __name__ == '__main__':
    main()