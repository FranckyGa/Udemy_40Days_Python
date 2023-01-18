import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:          #use "r" to read an existing zipfile and extract it
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname = filepath.name)    #arcname --> extract the name of the file only

if __name__ == "__main__":
    make_archive(filepaths = ["06_files/a.txt","06_files/b.txt"], dest_dir = "bonus")