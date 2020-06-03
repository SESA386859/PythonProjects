import xml.etree.cElementTree as ET
data ='''
<ComponentRoot name="ComponentLayout">
	<Component name="RSBBStartEndCaseButton" style="StartEndCaseButtonStyle">
		<Size name = "Default">
			<Item name = "Group">
				<Width>85.5</Width>
				<Height>50</Height>
				<Radius>2</Radius>
			</Item>
			<Item name="ButtonText" type = "text"  translationProp = "Default">
				<width>85.5</width>
				<Height>50</Height>
				<LeftMargin>0</LeftMargin>
				<TopMargin>0</TopMargin>
				<NumberLines>1</NumberLines>
				<FontSize>10</FontSize>
				<FontType>Normal</FontType>
			</Item>
		</Size>
    </Component>
</ComponentRoot>
'''

myroot =ET.fromstringlist(data)
print(myroot.tag)