from pathlib import Path
import re
import shutil
import logging

MOVIES = Path("./srv/media/movies")
SERIES = Path("./srv/media/series")
DOWNLOADS = Path("./srv/downloads")

VIDEO_EXTENSIONS = {".mkv",".mp4", ".avi"}
SERIES_PATTERN = re.compile(r"\b\d+x\d{2}\b", re.IGNORECASE)

def is_video(file: Path) -> bool:
    return file.is_file() and file.suffix.lower() in VIDEO_EXTENSIONS

def is_series(file: Path) -> bool:
    return bool(SERIES_PATTERN.search(file.name))
 
def classify(file: Path) -> Path:
    return SERIES if is_series(file) else MOVIES

def move_video(file: Path):
    destination = classify(file) / file.name
    shutil.move(str(file), destination)
    if classify is SERIES: logging.info(f"The file {file.name} is a series")
    else: logging.info(f"The file {file.name} is a movie")

def scan_directory(root: Path):
    for item in root.rglob("*"):
        if is_video(item):
            logging.info(f"The file {item} is a multi-media file, it will be moved")
            move_video(item)

def cleanup_files(root: Path):
    for dirpath in sorted(root.rglob("*"), reverse=True):
        if dirpath.iterdir:
            dirpath.unlink

def cleanup_empty_dirs(root: Path):
    for dirpath in sorted(root.rglob("*"), reverse=True):
        logging.info(f"The founded directories are:{dirpath}")
        if dirpath.is_dir() and not any(dirpath.iterdir()):
            dirpath.rmdir()
        else:
            logging.info(f"No files found, deleting directories...")


    
def main():
# Logging
    logging.basicConfig(
        filename='logs.txt',
        level=logging.DEBUG,
        format='%(asctime)s | %(levelname)s | %(message)s'
    )
# Program
    scan_directory(DOWNLOADS)
    logging.debug(f"The scan has started in {DOWNLOADS}")
    cleanup_files(DOWNLOADS)
    cleanup_empty_dirs(DOWNLOADS)
    logging.debug(f"The cleanup process has started in {DOWNLOADS}")

if __name__ == "__main__":
    main()
