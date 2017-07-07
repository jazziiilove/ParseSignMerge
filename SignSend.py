"""
 " " " " " " " " " " " " " " " " " " " " " " "
 " Assignment: ParseSignMerge                "
 " Programmer: Baran Topal                   "
 " File name: SignSend.py                    "
 "                                           "
 " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " "
 "	                                                                                         "
 "  LICENSE: This source file is subject to have the protection of GNU General               "
 "	Public License. You can distribute the code freely but storing this license information. "
 "	Contact Baran Topal if you have any questions. barantopal@barantopal.com                 "
 "	                                                                                         "
 " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " "
"""

#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import Sign
#import Merge
#fname = input("Enter file name: ")
fname= "my.xml"
fh = open(fname)
inp = str(fh.read())
#print(inp)

#with open(fname) as f:
 #   content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
#content = [x.strip() for x in content]
#/Personnel/Employee[2]/Name

#/timeSeriesResponse/timeSeries/@name


tree = ET.parse(fname)
result = ''

doc = tree.getroot()

'''works
thingy = doc.find('Employee')
if(thingy.attrib!= None):
    print (thingy.attrib)
'''
listIds = list()
listCvs = list()
values = doc.findall('Employee/Id')
for value in values:
    print (value.text)
    listIds.append(value.text)


values = doc.findall('Employee/CV')
for value in values:
    print (value.text)
    listCvs.append(value.text)

dictionary = dict(zip(listIds, listCvs))
print(dictionary)

sign = Sign.Sign("3674", '1.pdf')
sign.hello()
print("Id:", sign.id)

sign.watermark()

sign.send()

'''
Not works
#for elem in root.findall('.//child/grandchild'):
for elem in root.findall('Personnel/Employee[1]/Name'):

  #  if elem.attrib.get('type') == 'contract':
    result = elem.text
    print("the answsdfer is:", result)
    break
print("done")

'''
