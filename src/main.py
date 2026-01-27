import os
import shutil
from markdown_to_html_node import markdown_to_html_node
from htmlnode import HTMLNode
from extract_title import extract_title


def main():
    static_to_public()
    generate_page("content/index.md", "template.html", "public/index.html")

def static_to_public():
    public_path = os.path.abspath("public/")
    static_path = os.path.abspath("static/")
    print(f"static: {static_path}")
    if os.path.exists("public/"):
        print(public_path)
        shutil.rmtree(public_path)
    os.mkdir(public_path)
    copy_contents(static_path, public_path)

def copy_contents(filepath, destinationpath):
    print(f"copy static: {filepath}")
    dir_contents = os.listdir(filepath)
    for file_name in dir_contents:
        copy_dir = f"{filepath}/{file_name}"
        if os.path.isfile(copy_dir):
            dest_dir = f"{destinationpath}/{file_name}"
            #TODO: this dest_dir needs to respect the file locations from the copy_dir!
            shutil.copy(copy_dir, dest_dir)
            print(f"Copied file {copy_dir}")
        else:
            new_destination = f"{destinationpath}/{file_name}"
            os.mkdir(new_destination)
            copy_contents(copy_dir, new_destination)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    markdown_file = open(from_path)
    template_file = open(template_path)
    markdown_text = markdown_file.read()
    markdown_html = markdown_to_html_node(markdown_text)
    html_text = markdown_html.to_html()
    #TODO: fix this to_html call! getting ValueErrors about leaf nodes!
    page_title = extract_title(markdown_text)
    template_text = template_file.read()
    template_text = template_text.replace("{{ Title }}", page_title)
    template_text = template_text.replace("{{ Content }}", html_text)
    markdown_file.close()
    template_file.close()
    if os.path.exists(dest_path):
        new_file = open(dest_path, "w")
        new_file.write(template_text)
    else:
        newpath = os.path.dirname(dest_path)
        if os.path.exists(newpath) == False:
            os.makedirs(newpath)
        new_file = open(dest_path, "w")
        new_file.write(template_text)

    


if __name__ == "__main__":
    main()
