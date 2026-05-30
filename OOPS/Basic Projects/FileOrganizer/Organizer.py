import os
import shutil
import logging
import schedule
import time


SOURSE_FOLDER=r"D:\TestFolder"

logging.basicConfig(
    filename="Organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

FILETYPE={
    "Images":[".jpg",".jpeg",".png",".gif"],
    "Documents":[".pdf",".docx",".txt",".pptx"],
    "Videos":[".mp4",".mkv",".avi"],
    "Audio":[".mp3",".wav"],
    "Archives":[".zip",".rar"]
}

def organize_files():
    print("Checking Folder...")

    for file in os.listdir(SOURSE_FOLDER):
        sourse_path=os.path.join(SOURSE_FOLDER,file)

        if os.path.isdir(sourse_path):
            continue

        file_extension=os.path.splitext(file)[1].lower()
        moved=False

        for folder_name,extension in FILETYPE.items():

            if file_extension in extension:

                destination_folder=os.path.join(
                    SOURSE_FOLDER,
                    folder_name
                )

                os.makedirs(
                    destination_folder,
                    exist_ok=True
                )

                destination_path=os.path.join(
                    destination_folder,
                    file
                )

                shutil.move(
                    sourse_path,
                    destination_path
                )

                logging.info(
                    f"Moves {file} to {folder_name}"
                )

                print(
                    f"Moved {file} -> {folder_name}"
                )

                moved=True
                break

        if not moved:
            logging.warning(
                f"Unknown file type:{file}"
            )
            print(
                f"Skipped {file} (unknown Type)"
            )

schedule.every(1).minutes.do(organize_files)

print("File Organizer started...")
print(f"Monitering:{SOURSE_FOLDER}")

organize_files()

while True:
    schedule.run_pending()
    time.sleep(1)

        

