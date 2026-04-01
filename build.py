import os
import argparse

BUILD_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BUILD_DIR, ".."))

SRC_DIR = os.path.join(PROJECT_ROOT, "src")
DEFAULT_ENTRY = os.path.join(SRC_DIR, "main.pnml")

included_files = set()

def expand_includes(file_path, out_file):
    file_path = os.path.normpath(file_path)

    if file_path in included_files:
        return
    included_files.add(file_path)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Include file not found: {file_path}")

    with open(file_path, encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()

            if stripped.startswith("#include"):
                start = stripped.find('"') + 1
                end = stripped.rfind('"')
                include_target = stripped[start:end]

                include_path = os.path.join(os.path.dirname(file_path), include_target)
                expand_includes(include_path, out_file)
            else:
                out_file.write(line)

def merge(entry_file, output_name):
    output_path = os.path.join(PROJECT_ROOT, output_name)

    if not os.path.exists(entry_file):
        raise FileNotFoundError(f"Entry PNML not found: {entry_file}")

    print(f"Entry PNML : {entry_file}")
    print(f"Output NML : {output_path}")

    with open(output_path, "w", encoding="utf-8") as out:
        expand_includes(entry_file, out)

    print("PNML merge completed successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Merge PNML includes into a single NML file"
    )

    parser.add_argument(
        "--entry",
        default=DEFAULT_ENTRY,
        help="Top-level PNML file (default: src/main.pnml)"
    )

    parser.add_argument(
        "--merge",
        default="generated.nml",
        help="Output merged NML file name (created in project root)"
    )

    args = parser.parse_args()
    merge(args.entry, args.merge)