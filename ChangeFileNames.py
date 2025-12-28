import argparse
from pathlib import Path
import shutil


def process_folders(source_root: Path, destination: Path, new_extension: str, dry_run: bool):
    destination.mkdir(parents=True, exist_ok=True)

    for subfolder in source_root.iterdir():
        if not subfolder.is_dir():
            continue

        files = [f for f in subfolder.iterdir() if f.is_file()]
        if not files:
            continue

        multiple_files = len(files) > 1

        for file in files:
            # Apply Disc naming ONLY if multiple files exist
            if multiple_files:
                disc_number = "2" if "2" in file.stem else "1"
                new_filename = f"{subfolder.name} Disc {disc_number}{new_extension}"
            else:
                new_filename = f"{subfolder.name}{new_extension}"

            destination_file = destination / new_filename

            if destination_file.exists():
                print(f"Skipped (exists): {destination_file.name}")
                continue

            if dry_run:
                print(f"[DRY RUN] Would copy: {file} → {destination_file}")
            else:
                shutil.copy2(file, destination_file)
                print(f"Copied: {file.name} → {destination_file.name}")


def main():
    parser = argparse.ArgumentParser(
        description="Copy files from subfolders and rename them based on folder name and disc rules."
    )

    parser.add_argument(
        "--source",
        required=True,
        help="Root folder containing subfolders"
    )

    parser.add_argument(
        "--dest",
        required=True,
        help="Destination folder"
    )

    parser.add_argument(
        "--ext",
        default=".iso",
        help="New file extension (default: .iso)"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview actions without copying files"
    )

    args = parser.parse_args()

    source_root = Path(args.source)
    destination = Path(args.dest)

    if not source_root.exists():
        raise FileNotFoundError(f"Source folder not found: {source_root}")

    process_folders(
        source_root=source_root,
        destination=destination,
        new_extension=args.ext,
        dry_run=args.dry_run
    )


if __name__ == "__main__":
    main()