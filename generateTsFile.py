import xml.etree.cElementTree as ET
filehandler=open('English.ts','w+')
filehandler.write('<?xml version="1.0" encoding="utf-8"?>\n'
                  '<!DOCTYPE TS>\n'
                  '<TS version="2.1" language="en_US">'
                  '\n<context>\n')

#parsing the component xml
ComponentXmlTree=ET.parse('Component.xml')
myComponentXMLRoot=ComponentXmlTree.getroot()

#parsing the group xml
GroupXmlTree= ET.parse('Group.xml')
myGroupXMLRoot=GroupXmlTree.getroot()
translations = 'translations here'
extracomment = 'extracomment here'

for groups in myGroupXMLRoot:
    for items in groups:
        component_name=items.attrib['componentName']
        for stringids in items[0]:
            itemname=items[0].attrib['name']
            str_Id = str(stringids.text) + '_' + component_name
            for component in myComponentXMLRoot.findall('Component'):
                if(component.attrib['name']==component_name):
                    for size in component:
                        sizename=size.attrib['name']
                        for itemComp in size:
                            if(itemComp.attrib['name']==itemname):
                               if(sizename!='Default'):
                                   str_Id=str_Id+'_'+str(sizename)
                               width = itemComp.find('Width').text
                               Height = itemComp.find('Height').text
                               NumberLines = itemComp.find('NumberLines').text
                               FontSize = itemComp.find('FontSize').text
                               extracomment='width='+width+' Height='+Height+' No of lines='+NumberLines+' FontSize='+FontSize



                        extra_comment = 'for '+component_name
                        filehandler.write('<message id="'+str(str_Id)+'"'+'>\n')
                        filehandler.write('<source>'+translations+'</source>'+'\n')
                        filehandler.write('<extracomment>'+extracomment+'<extracomment>\n')
                        filehandler.write('<translation type="unfinished"></translation>\n')
                        filehandler.write('<extra-Comment>'+extra_comment+'</extra-Comment>\n')
                        filehandler.write('</message>\n')
filehandler.write('</context>\n')
filehandler.write('</TS>\n')



