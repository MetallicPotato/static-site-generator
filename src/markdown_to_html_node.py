from htmlnode import LeafNode, ParentNode
from markdown_to_blocks import markdown_to_blocks
from blocks import block_to_block_type, BlockType
from text_to_textnodes import text_to_text_nodes
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_blocks = []
    for block in blocks:
        block_type = block_to_block_type(block)
        new_node = None
        match block_type:
            case BlockType.HEADING:
                new_node = LeafNode("h1", block)
            case BlockType.QUOTE:
                new_node = LeafNode("blockquote", block)
            case BlockType.CODE:
                code = LeafNode("code", block)
                new_node = ParentNode("pre", [code])
            case BlockType.ORDERED_LIST:
                new_node = _list_iterate(block, True)
            case BlockType.UNORDERED_LIST:
                new_node = _list_iterate(block, False)
            case BlockType.PARAGRAPH:
                new_node = LeafNode("p", block)
            case _:
                raise ValueError(f"invalid block type: {block_type}")
        html_blocks.append(new_node)
    #TODO: more stuff!
    #TODO: new_node might need to be a parent node



def _list_iterate(block, ordered: bool):
    ordered_string = "ol" if ordered else "ul"
    parent_node = ParentNode(ordered_string, [])
    for line in block.splitlines():
        parent_node.children.append(LeafNode("li", line))
    return parent_node

def _text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes