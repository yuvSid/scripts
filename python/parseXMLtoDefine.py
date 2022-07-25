import re
import xml.etree.ElementTree as ElTree

if __name__ == '__main__':    
    tree = ElTree.parse('./WORKER_DIR/IN')
    root = tree.getroot()
    tags = set()
    for element in root.iter():
        tags.add(element.tag)
    
    with open('./WORKER_DIR/OUT', "w") as f_out:
        for element in tags:
            def_name = 'GAD_XML_ELEMENT_' + ('_'.join(filter(None, re.findall('[A-Z]*[^A-Z]*', element)))).upper()
            def_line = f'#define {def_name} "{element}"'
            print(def_line)
            f_out.write(def_line + '\n')
