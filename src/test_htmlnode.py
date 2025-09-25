import unittest

from htmlnode import HTMLNode

props1 = {"href":"https://www.google.com/",
          "target":"_blank"}
props2 = {"href":"https://www.dn.se/",
          "target":"somethingsomething"}

testnode = HTMLNode("a", "This is the text value",None,props1)
testnode2 = HTMLNode("a", "This is the text value",None,props2)

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "This is the text value",None,props1)
        node2 = HTMLNode("a", "This is the text value",None,props1)
        self.assertEqual(node,node2)

    def test_notprops(self):
        node = HTMLNode("a", "This is the text value",None,props1)
        node2 = HTMLNode("a", "This is the text value",None,props2)
        self.assertNotEqual(node,node2)
    
    def test_children(self):
        node = HTMLNode("a", "This is the text value",testnode,None)
        node2 = HTMLNode("a", "This is the text value",testnode,None)
        self.assertEqual(node,node2)

    def test_notchildren(self):
        
        node = HTMLNode("a", "This is the text value",testnode,None)
        node2 = HTMLNode("a", "This is the text value",testnode2,None)
        self.assertNotEqual(node,node2)

if __name__ == "__main__":
    unittest.main()