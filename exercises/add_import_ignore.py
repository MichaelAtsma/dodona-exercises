import os

root_dir = "exercises"

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename == "oracle_test.py":
            file_path = os.path.join(dirpath, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            changed = False
            new_lines = []
            for line in lines:
                if (
                    line.strip().startswith("from evaluation_utils import")
                    and "# type: ignore" not in line
                ):
                    # Remove any trailing newline before appending the comment
                    line = line.rstrip("\n") + " # type: ignore\n"
                    changed = True
                new_lines.append(line)
            if changed:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.writelines(new_lines)
                print(f"Updated: {file_path}")