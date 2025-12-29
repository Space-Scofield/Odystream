from pathlib import Path
import re
import shutil

MOVIES = Path("./srv/media/movies")
SERIES = Path("./srv/media/series")
DOWNLOADS = Path("./srv/downloads")

VIDEO_EXTENSIONS = ["*.mkv","*.mp4", "*.avi"]
SERIES_PATTERN = re.compile(r"\b\d+x\d{2}\b", re.IGNORECASE)

def main():
    scan_directory(DOWNLOADS)
    cleanup_empty_dirs(DOWNLOADS)

if __name__ == "__main__":
    main()

def scan_directory(root: Path):
    for item in root.rglob("*"):
        if is_video(item):
            move_video(item)

def classify(file: Path) -> Path:
    return SERIES if is_series(file) else MOVIES

def is_video(file: Path):
    file.is_file() and file.suffix.lower() in VIDEO_EXTENSIONS

def is_series(file: Path) -> bool:
    return bool(SERIES_PATTERN.search(file.name))
 
def move_video(file: Path):
    destination = classify(file) / file.name
    shutil.move(str(file), destination)

def cleanup_empty_dirs(root: Path):
    for dirpath in sorted(root.rglob("*"), reverse=True):
        if dirpath.is_dir and not any(dirpath.iterdir()):
            dirpath.rmdir()


def main():
    scan_directory(DOWNLOADS)
    cleanup_empty_dirs(DOWNLOADS)

if __name__ == "__main__":
    main()
