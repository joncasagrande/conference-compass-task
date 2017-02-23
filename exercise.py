import xml.etree.cElementTree as ET
from roadworks import RoadWorks
from printhtml import PrintHtml
 
def printFile(htmlfile):
   f = open("roads.html",'w')   # Trying to create a new file or open one
   f.write(""+htmlfile.printHtml())
   f.close()

tree = ET.ElementTree(file='doc1.xml')
root = tree.getroot()

htmlfile = PrintHtml()
i = 1
for elem in tree.findall('ha_planned_works'):
  planned_works = RoadWorks()
  for attr in elem.getchildren():
	setattr(planned_works, attr.tag, attr.text);
  htmlfile.printLink(planned_works)
  i = i+1
  if(i % 4 == 0):
  	htmlfile.addRow()

htmlfile.closeHtml()

printFile(htmlfile)