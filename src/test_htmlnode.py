import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_prop_to_html(self):
        node = HTMLNode(
            tag="a", 
            value="click here", 
            children=None,
            props={"href": "https://www.google.com"}
        )
        html = node.props_to_html()
        self.assertEqual(html, 'href="https://www.google.com"')

    def test_props_to_html(self):
        node = HTMLNode(
            tag="a",
            value="google",
            children=None,
            props={
                "href": "https://www.google.com",
                "target": "_blank"
            }
        )
        html = node.props_to_html()
        self.assertEqual(html, 'href="https://www.google.com" target="_blank"')

    def test_repr(self):
        child = HTMLNode(
            tag="p",
            value="dynamite"
        )
        parent = HTMLNode(
            tag="h1",
            value="boom goes the dynamite",
            children=[child]
        )
        parent_repr = "HTMLNode(h1, boom goes the dynamite, ['HTMLNode(p, dynamite, None, None)'], None)"
        self.assertEqual(parent.__repr__(), parent_repr)