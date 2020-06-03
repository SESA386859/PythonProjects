import xml.etree.cElementTree as ET
myTree=ET.parse('Component.xml')
myroot=myTree.getroot()
# print(myroot.tag)
# print(myroot[0].tag)
# print(myroot[0].attrib)
# for x in myroot[0][0]:
#    print(x.tag,x.attrib)
# for x in myroot[0][0][0]:
#    print(x.text)
for x in myroot.findall('Component'):
  for y in x.findall('Size'):
     for z in y.findall('Item'):
         if (z.attrib['name'] == 'ButtonText'):
             w=z.find('Width').text
             h=z.find('Height').text
             print('Width:'+w)
             print('Height:'+h)

# ET.SubElement(myroot[0],'Testing')
# for x in myroot.iter('Testing'):
#     b='added new tag'
#     x.text=str(b)
# myTree.write('newcomponent.xml')
# for x in myroot.iter('Item'):
#     a = "items description"
#     x.text=str(a)
#     x.set('updated','yes')
# myTree.write("UpdatedComponent.xml")



