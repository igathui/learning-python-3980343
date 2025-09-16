# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing XML

import xml.dom.minidom 

# XML FUNCTIONS - Using Python to work with XML, a Popular Markup Language
# XML stands for eXtensible Markup Language

# Use the parse() function to load and parse an XML file
print("Parsing the XML file data:")
doc = xml.dom.minidom.parse("samplexml.xml")

# Print out the document node and the name of the first child tag
print(doc.nodeName)
print(doc.firstChild.tagName)

# Get a list of XML tags from the document and print each one
print("\nListing elements by tagName:")
skills = doc.getElementsByTagName("skill")
print(f"The number of skills are: {skills.length}")

for skill in skills:
    print(skill.getAttribute("name"))

# Create a new XML tag and add it into the document
print("\nCreating new XML tags:")
newskill = doc.createElement("skill")
newskill.setAttribute("name", "Next.js")
doc.firstChild.appendChild(newskill)

skills = doc.getElementsByTagName("skill")
print(f"The number of skills are: {skills.length}")
for skill in skills:
    print(skill.getAttribute("name"))
