import csv
from pyproj import Proj, transform

inProj = Proj(init='epsg:2263')
outProj = Proj(init='epsg:4326')

#with open('Locations.csv', 'rb') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         x2,y2 = transform(inProj,outProj,row['X Coord.'],row['Y Coord.'])
#         print (row['X Coord.'], row['Y Coord.'],x2,y2 )

filename='Locations.csv'
output='OUT.csv'
with open(filename) as csvin:
    readfile = csv.reader(csvin, delimiter=',')
    with open(output, 'w') as csvout:
        writefile = csv.writer(csvout, delimiter=',', lineterminator='\n')
        for row in readfile:
            print(row[1],row[2])
            if row[1]=="X Coord.":
                row.extend(["Lng Coord.","Lat Coord."])
            else:
                x2,y2 = transform(inProj,outProj,row[1],row[2])
                row.extend([str(x2),str(y2)])
            writefile.writerow(row)
