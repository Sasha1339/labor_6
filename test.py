import unittest
import xml.etree.ElementTree as ET
from service import Service




class TestCalculator(unittest.TestCase):
  #setUp method is overridden from the parent class TestCase
    def init(self):
        self.service = Service()
        tree = ET.parse('data.xml')
        root = tree.getroot()
        xmlstr = ET.tostring(root, encoding='unicode')
        print(xmlstr)
        self.service.parsing_xml(xmlstr)
    def test_calculate(self):
        self.service = Service()
        tree = ET.parse('data.xml')
        root = tree.getroot()
        xmlstr = ET.tostring(root, encoding='unicode')
        print(xmlstr)
        self.service.parsing_xml(xmlstr)
        self.assertEqual(round(self.service.calculate(), 3), 0.157)

if __name__ == "__main__":
  unittest.main()