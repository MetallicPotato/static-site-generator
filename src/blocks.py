from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block):
    if block[:1] == "#":
        is_heading = False
        for i in block[:7]:
            if i == " ":
                is_heading = True
        return BlockType.HEADING

print(block_to_block_type("## Heading 1"))
