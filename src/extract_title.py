from markdown_to_blocks import markdown_to_blocks

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    header_block = ""
    for block in blocks:
        if block.startswith("#"):
            header_block = block.strip("# ")
            print(f"header - {header_block}")
            break
    if header_block == "":
        raise Exception("There is no header to extract.")
    return header_block