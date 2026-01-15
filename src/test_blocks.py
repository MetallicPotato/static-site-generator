import unittest
from blocks import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_heading1(self):
        block = "# This is a heading!"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, block_type)

    def test_heading2(self):
        block = "## This is a heading!"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, block_type)
    
    def test_heading3(self):
        block = "### This is a heading!"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, block_type)
    
    def test_heading4(self):
        block = "#### This is a heading!"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, block_type)
    
    def test_heading5(self):
        block = "##### This is a heading!"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, block_type)
    
    def test_heading6(self):
        block = "###### This is a heading!"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, block_type)
    
    def test_paragraph1(self):
        block = "###This ain't a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)
    
    def test_code(self):
        md = "```\nThis is a code block.\n```"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.CODE, block_type)
    
    def test_paragraph2(self):
        md = "``Not a code block```"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.PARAGRAPH, block_type)
    
    def test_quote(self):
        md = "> This is a quote!"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.QUOTE, block_type)
    
    def test_paragraph3(self):
        md = ">This is not a quote"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_unordered_list(self):
        block = "- List Item 1\n- List item 2\n- List item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.UNORDERED_LIST, block_type)
    
    def test_paragraph4(self):
        block = "- List Item 1\n - Extra Space here!\n- List item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_ordered_list(self):
        block = "1. First Item\n2. Second Item\n3. Third Item"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.ORDERED_LIST, block_type)

    def test_paragraph5(self):
        block = "1.First Item\n2.Second Item\n3.Third Item"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)
