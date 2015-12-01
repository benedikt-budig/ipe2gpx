import sys
import csv
import xml.etree.ElementTree as ET

# print usage if we don't have the right number of arguments
if len(sys.argv) != 3:
  print "Usage: ipe2gpx.py [file.ipe] [file.gpx]"
  sys.exit(1)

# parse IPE xml file and get root node
root = ET.parse(sys.argv[1]).getroot()

# get the first path on the first page of the document
path = root.find('page').find('path').text

# extract coordinates from each non-empty line
coords = []
for line in path.splitlines():
  if line != "":
    coords.append((line.split(" ")[0], line.split(" ")[1]))

# create new GPX xml structure
root = ET.Element("gpx")
trkseg = ET.SubElement(ET.SubElement(root, "trk"), "trkseg")

# add coordinates as trackpoints
for coord in coords:
  trkpt = ET.SubElement(trkseg, "trkpt", lon=coord[0], lat=coord[1])

# write GPX file
tree = ET.ElementTree(root)
tree.write(sys.argv[2], encoding="utf-8", xml_declaration=True)

