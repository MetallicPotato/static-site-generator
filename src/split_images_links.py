from extract_links import extract_markdown_links, extract_markdown_images
from split_delimiter import split_nodes_delimiter
from textnode import TextType, TextNode


def split_nodes_image(old_nodes):
    if not old_nodes:
        raise ValueError("Cannot split empty list of nodes")
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            matches = extract_markdown_images(node.text)
            if matches:
                text_to_split = node.text
                for match in matches:
                    split_text = text_to_split.split(f"![{match[0]}]({match[1]})")
                    if split_text[0] != "":
                        new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                    text_to_split = split_text[1]
                    if match[0] != "" and match[1] != "":
                        new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
                if text_to_split != "":
                    new_nodes.append(TextNode(text_to_split, TextType.TEXT))
            else:
                if node.text != "":
                    new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    if not old_nodes:
        raise ValueError("Cannot split empty list of nodes")
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            matches = extract_markdown_links(node.text)
            if matches:
                text_to_split = node.text
                for match in matches:
                    split_text = text_to_split.split(f"[{match[0]}]({match[1]})")
                    if split_text[0] != "":
                        new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                    text_to_split = split_text[1]
                    if match[0] != "" and match[1] != "":
                        new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
                if text_to_split != "":
                    new_nodes.append(TextNode(text_to_split, TextType.TEXT))
            else:
                if node.text != "":
                    new_nodes.append(node)
    return new_nodes