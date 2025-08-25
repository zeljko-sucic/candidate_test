import xml.etree.ElementTree as ET
import json
from pathlib import Path


def load_mappings(mapper_file: str):
    """Parse mapper.xml and extract mapping rules."""
    tree = ET.parse(mapper_file)
    root = tree.getroot()

    mappings = []
    for mapper in root.findall("mapper"):
        source = mapper.find("source").text.strip()
        target = mapper.find("target").text.strip()
        mappings.append((source, target))
    return mappings


def generate_transformer(mappings, output_file="transformer.py"):
    """Generate a Python script based on mappings."""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("import json\n")
        f.write("import xml.etree.ElementTree as ET\n\n")

        f.write("def get_value(data, path):\n")
        f.write("    keys = path.strip('/').split('/')\n")
        f.write("    for k in keys:\n")
        f.write("        if k in data:\n")
        f.write("            data = data[k]\n")
        f.write("        else:\n")
        f.write("            return ''  # missing value\n")
        f.write("    return data\n\n")

        f.write("def transform(json_input):\n")
        f.write("    data = json.loads(json_input)\n")
        # get root element name from first mapping
        root_element = mappings[0][1].strip("/").split("/")[0]
        f.write(f"    root = ET.Element('{root_element}')\n")

        for source, target in mappings:
            target_path = target.strip("/").split("/")
            element_name = target_path[-1]
            f.write(f"    value = get_value(data, '{source}')\n")
            f.write(f"    ET.SubElement(root, '{element_name}').text = str(value)\n")

        f.write("    return ET.tostring(root, encoding='unicode')\n\n")

        f.write("if __name__ == '__main__':\n")
        f.write("    import sys\n")
        f.write("    json_file = sys.argv[1]\n")
        f.write("    with open(json_file, 'r', encoding='utf-8') as jf:\n")
        f.write("        json_input = jf.read()\n")
        f.write("    output_xml = transform(json_input)\n")
        f.write("    print(output_xml)\n")


if __name__ == "__main__":
    mappings = load_mappings("mapper_v01.xml")
    generate_transformer(mappings, "transformer.py")
    print("✅ Generated transformer.py based on mapper_v01.xml")
