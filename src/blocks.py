from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block):
    lines = block.split("\n")
    first_line = lines[0]
    last_line = lines[-1]
    if first_line.startswith("# ") or first_line.startswith("## ") or first_line.startswith("### ") or first_line.startswith("#### ") or first_line.startswith("##### ") or first_line.startswith("###### "):
        return BlockType.HEADING
    elif first_line.startswith("```") and last_line.endswith("```"):
        return BlockType.CODE
    elif first_line.startswith("> "):
        return BlockType.QUOTE
    unordered_list_lines = 0
    ordered_list_lines = 0
    for i in range(len(lines)):
        if lines[i].startswith("- "):
            unordered_list_lines += 1
        elif lines[i].startswith(f"{i+1}. "):
            ordered_list_lines += 1
    if unordered_list_lines == len(lines):
        return BlockType.UNORDERED_LIST
    elif ordered_list_lines == len(lines):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
