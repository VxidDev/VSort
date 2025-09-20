from pathlib import Path 
import shutil , argparse

text_extensions = ["txt","md","rtf","log","csv","json","xml","yaml","yml","tex","ini","cfg","toml"]
video_extensions = ["mp4","mkv","avi","mov","wmv","flv","webm","m4v","mpeg","mpg","3gp","ts","vob","m2ts","ogv"]
audio_extensions = ["mp3","wav","flac","aac","ogg","wma","m4a","alac","aiff"]
image_extensions = ["jpg","jpeg","png","gif","webp","avif","heic","heif","tiff","bmp"]

def create_folders(path):
    folders = ["Images" , "Audios" , "Videos" , "Text files"]
    try:
        for folder in folders:
            Path(f"{path}/{folder}").mkdir()
    except FileExistsError:
        pass
        
def sort(file , path):
    extension = Path(file.name).suffix[1:].lower()
    try:
        if extension in text_extensions:
            shutil.move(file , Path(path) / "Text files")
            print(f"{file} moved to text files.")
        elif extension in video_extensions:
            shutil.move(file , Path(path) / "Videos")
            print(f"{file} moved to videos.")
        elif extension in audio_extensions:
            shutil.move(file , Path(path) / "Audios")
            print(f"{file} moved to audios.")
        elif extension in image_extensions:
            shutil.move(file , Path(path) / "Images")
            print(f"{file} moved to images.")
        else:
            print("file extensions not recognized, skipping...")
    except shutil.Error as error:
        if "already exists" in str(error):
            print(f"{file} already exists in moving folder!")
            choices = ["s" , "r"]
            choice = input("File already exists!\nskip(s) , rename(r): ").lower()
            while choice not in choices:
                choice = input("File already exists!\nskip(s) , rename(r): ").lower() 
            if choice == "s":
                pass 
            else:
                name = input("file name: ")
                sort(Path(file).rename(f"{path}{name}.{extension}") , path)
                
def main():
    parser = argparse.ArgumentParser(prog="vsort" , description="Fast and lightweight script that sorts your files.")

    parser.add_argument("path" , type=str , help="sorting path.")

    args = parser.parse_args()

    create_folders(args.path)

    for file in Path(args.path).iterdir():
        sort(file , args.path)

if __name__ == "__main__":
    main()
