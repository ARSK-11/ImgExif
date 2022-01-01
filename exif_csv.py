import csv
     
with open("exifdata.txt", 'r') as infile, open("data.csv", 'w') as outfile:
     stripped = (line.strip() for line in infile)
     lines = (line.split(",") for line in stripped if line)
     writer = csv.writer(outfile)
     writer.writerows(lines)