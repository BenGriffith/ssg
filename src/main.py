from textnode import TextType, TextNode


def main():
    text_node = TextNode("bold", TextType.CODE_TEXT, "https://google.com")
    print(text_node)


if __name__ == "__main__":
    main()