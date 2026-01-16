from markdown_to_blocks import markdown_to_blocks
from blocks import block_to_block_type, BlockType

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        