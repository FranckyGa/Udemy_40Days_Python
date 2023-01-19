import zipfile as zip

def extract_archive(archivepath, dest_dir):
    with zip.ZipFile(archivepath, "r") as archive:
        archive.extractall(dest_dir)


#Test if this function works properly
if  __name__ == "__main__":
    extract_archive("06_files/compressed.zip","F:/Dev/Udemy/App1/bonus")