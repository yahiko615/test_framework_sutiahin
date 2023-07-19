import json
import xml.etree.ElementTree as ET
from argparse import ArgumentParser


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        data = {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'birth_year': self.birth_year
        }
        return json.dumps(data)

    def convert_to_xml(self):
        root = ET.Element('Human')
        name = ET.SubElement(root, 'name')
        name.text = self.name
        age = ET.SubElement(root, 'age')
        age.text = str(self.age)
        gender = ET.SubElement(root, 'gender')
        gender.text = self.gender
        birth_year = ET.SubElement(root, 'birth_year')
        birth_year.text = str(self.birth_year)

        xml_string = ET.tostring(root, encoding='utf-8').decode('utf-8')
        return xml_string


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('format', choices=['xml', 'json'], help='Output format: json or xml')
    args = parser.parse_args()

    misha = Human("Misha Sutiahin", 22, "Male", 2001)

    if args.format == 'json':
        json_data = misha.convert_to_json()
        with open('task.json', 'w') as file:
            file.write(json_data)

    elif args.format == 'xml':
        xml_data = misha.convert_to_xml()
        with open('task.xml', 'w') as file:
            file.write(xml_data)
