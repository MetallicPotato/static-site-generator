import os
import shutil


def main():
    copy_contents()

def copy_contents():
    public_path = os.path.abspath("public/")
    src_path = os.path.abspath("src/")
    if os.path.exists("public/"):
        print(public_path)
        shutil.rmtree(public_path)
    #TODO: finish!


if __name__ == "__main__":
    main()
