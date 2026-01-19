from htmlnode import LeafNode, ParentNode
from markdown_to_blocks import markdown_to_blocks
from blocks import block_to_block_type, BlockType
from text_to_textnodes import text_to_text_nodes
from textnode import text_node_to_html_node, TextNode, TextType


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_node = ParentNode("div", [])
    for block in blocks:
        block_type = block_to_block_type(block)
        new_node = None
        match block_type:
            case BlockType.HEADING:
                new_node = ParentNode("h1", _text_to_children(block))
            case BlockType.QUOTE:
                new_node = ParentNode("blockquote", _text_to_children(block))
            case BlockType.CODE:
                code = LeafNode("code", block[4:-3])
                new_node = ParentNode("pre", [code])
            case BlockType.ORDERED_LIST:
                new_node = _list_iterate(block, True)
            case BlockType.UNORDERED_LIST:
                new_node = _list_iterate(block, False)
            case BlockType.PARAGRAPH:
                lines = block.split("\n")
                paragraph = " ".join(lines)
                new_node = ParentNode("p", _text_to_children(paragraph))
            case _:
                raise ValueError(f"invalid block type: {block_type}")
        if new_node is not None:
            html_node.children.append(new_node)
    return html_node

def _list_iterate(block, ordered: bool):
    ordered_string = "ol" if ordered else "ul"
    parent_node = ParentNode(ordered_string, [])
    for line in block.splitlines():
        parent_node.children.append(ParentNode("li", _text_to_children(line)))
    return parent_node

def _text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes