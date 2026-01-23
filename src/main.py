import os
import shutil


def main():
    print(os.listdir())

def copy_contents():
    public_path = os.path.abspath("public/")
    static_path = os.path.abspath("static/")
    if os.path.exists("public/"):
        print(public_path)
        shutil.rmtree(public_path)
    os.mkdir(public_path)
    dir_contents = os.listdir(static_path)
    
    for file_name in dir_contents:

        copy_dir = f"{static_path}{file_name}"
        dest_dir = f"{public_path}{file_name}"
        shutil.copy(copy_dir, dest_dir)


if __name__ == "__main__":
    main()
