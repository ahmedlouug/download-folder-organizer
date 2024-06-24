import os
import shutil
import json

DOWNLOADS_FOLDER= r"C:\Users\amine\Downloads"

def load_config(config_file):
    with open(config_file,'r') as file :
        return json.load(file)
    
def create_folders(categories):
    for category in categories :
        folder_path = os.path.join(DOWNLOADS_FOLDER, category)
        if not os.path.exists(folder_path) :
            os.makedirs(folder_path)

def move_files(categories):
    for file_name in os.listdir(DOWNLOADS_FOLDER):  
        file_path=os.path.join(DOWNLOADS_FOLDER,file_name)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_name)[1].lower()
            for category,extensions in categories.items():
                if file_extension in extensions :
                    try:
                        shutil.move(file_path, os.path.join(DOWNLOADS_FOLDER,category,file_name))
                        print(f"Moved {file_name} to {category}")
                    except Exception as e :
                        print(f"Failed to move {file_name}:{e}")
                    break 

def main():
    config_file = "config_clean_down.json"
    categories = load_config(config_file)

    create_folders(categories)
    move_files(categories)
    print("Downloads folder cleaned and organized.")

# if __name__ == "__main__":
#     main()