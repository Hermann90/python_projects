import xml.etree.ElementTree as ET
import os

# Parse XML into Element Tree
ns = "http://maven.apache.org/POM/4.0.0"
tree = ET.parse('pom.xml')
root = tree.getroot()

print(root.tag)
p = tree.getroot().find("{%s}version" % ns)
version = root.find(p.tag)
# Root

print(p.tag)
print(version.text)

os.environ['VERSIONAPP'] = version.text
#Export VERSIONAPP=version.text

os.system('echo $VERSIONAPP')

def get_pom_version():
    import xml.etree.ElementTree as ET

    ns = "http://maven.apache.org/POM/4.0.0"
    tree = ET.parse('pom.xml')
    root = tree.getroot()
    version = tree.getroot().find("{%s}version" % ns)
    return version


v = get_pom_version().text
print(v)
