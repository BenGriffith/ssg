import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_eq_normal(self):
        node = TextNode("Normal", TextType.NORMAL_TEXT, "http://google.com")
        node2 = TextNode("Normal", TextType.NORMAL_TEXT, "http://google.com")
        self.assertEqual(node, node2)

    def test_eq_italic(self):
        node = TextNode("Italic", TextType.ITALIC_TEXT, "http://nba.com")
        node2 = TextNode("Italic", TextType.ITALIC_TEXT, "http://nba.com")
        self.assertEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode("Code", TextType.CODE_TEXT)
        self.assertIsNone(node.url)

    def test_ne(self):
        node = TextNode("Bold", TextType.BOLD_TEXT, "http://yahoo.com")
        node2 = TextNode("Bold", TextType.BOLD_TEXT, "http://apple.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()