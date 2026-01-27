import os
import shutil


def main():
    static_to_public()

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


if __name__ == "__main__":
    main()
