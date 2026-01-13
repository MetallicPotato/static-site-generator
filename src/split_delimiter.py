from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not old_nodes:
        raise ValueError("Cannot split empty list of nodes")
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            split_text = node.text.split(delimiter)
            inside_split = False
            for t in split_text:
                if inside_split:
                    new_nodes.append(TextNode(t, text_type))
                else:
                    new_nodes.append(TextNode(t, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes
