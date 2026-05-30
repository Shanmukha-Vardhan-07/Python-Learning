import os
import shutil
import logging
import schedule
import time


SOURCE_FOLDER = r"D:\TestFolder"


logging.basicConfig(
    filename="Organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}


def organize_files():
    print("\nChecking folder...")

    
    for file in os.listdir(SOURCE_FOLDER):

        source_path = os.path.join(SOURCE_FOLDER, file)

        
        if os.path.isdir(source_path):
            continue

        
        file_extension = os.path.splitext(file)[1].lower()

        moved = False

        
        for folder_name, extensions in FILE_TYPES.items():

            if file_extension in extensions:

                destination_folder = os.path.join(
                    SOURCE_FOLDER,
                    folder_name
                )

                
                os.makedirs(
                    destination_folder,
                    exist_ok=True
                )

                destination_path = os.path.join(
                    destination_folder,
                    file
                )

                
                shutil.move(
                    source_path,
                    destination_path
                )

                logging.info(
                    f"Moved {file} to {folder_name}"
                )

                print(
                    f"Moved {file} -> {folder_name}"
                )

                moved = True
                break

        if not moved:
            logging.warning(
                f"Unknown file type: {file}"
            )

            print(
                f"Skipped {file} (Unknown Type)"
            )



schedule.every(1).minutes.do(organize_files)

print("File Organizer Started...")
print(f"Monitoring: {SOURCE_FOLDER}")


organize_files()


while True:
    schedule.run_pending()
    time.sleep(1)