from textnode import TextNode, TextType


def main():
    node = TextNode("Hello World", TextType.BOLD, "https://www.boot.dev")
    print(node)


main()
