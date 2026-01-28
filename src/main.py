import os
import shutil
import sys
from markdown_to_html_node import markdown_to_html_node
from pathlib import Path
from extract_title import extract_title


def main():
    args = sys.argv[1:]
    base_path = ""
    if len(args) == 0:
        base_path = "/"
    base_path = args[0]
    static_to_public()
    generate_pages_recursive("content/", "template.html", "docs/", base_path)

def static_to_public():
    public_path = os.path.abspath("docs/")
    static_path = os.path.abspath("static/")
    print(f"static: {static_path}")
    if os.path.exists("docs/"):
        print(public_path)
        shutil.rmtree(public_path)
    os.mkdir(public_path)
    copy_contents(static_path, public_path)

def copy_contents(filepath, destination):
    print(f"copy static: {filepath}")
    dir_contents = os.listdir(filepath)
    for file_name in dir_contents:
        copy_dir = f"{filepath}/{file_name}"
        if os.path.isfile(copy_dir):
            dest_dir = f"{destination}/{file_name}"
            shutil.copy(copy_dir, dest_dir)
            print(f"Copied file {copy_dir}")
        else:
            new_destination = f"{destination}/{file_name}"
            os.mkdir(new_destination)
            copy_contents(copy_dir, new_destination)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    markdown_file = open(from_path)
    template_file = open(template_path)
    markdown_text = markdown_file.read()
    markdown_html = markdown_to_html_node(markdown_text)
    html_text = markdown_html.to_html()
    page_title = extract_title(markdown_text)
    template_text = template_file.read()
    template_text = template_text.replace("{{ Title }}", page_title)
    template_text = template_text.replace("{{ Content }}", html_text)
    template_text = template_text.replace('href="/', f'href="{basepath}')
    template_text = template_text.replace('src="/', f'src="{basepath}')
    markdown_file.close()
    template_file.close()
    if os.path.exists(dest_path):
        new_file = open(dest_path, "w")
        new_file.write(template_text)
    else:
        new_path = os.path.dirname(dest_path)
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        new_file = open(dest_path, "w")
        new_file.write(template_text)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)
    


if __name__ == "__main__":
    main()
