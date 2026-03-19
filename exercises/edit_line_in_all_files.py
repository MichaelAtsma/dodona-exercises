import os
import re

# Pattern or literal to replace
use_regex_for_to_replace = False
to_replace = r"""@media (prefers-color-scheme: dark) {
    .functioninput-default { color: white; }
    .functionseparators { color: white; }
    .function-name { color: #daaa28ff; }
    .string { color: #52d1c1; }
    .functioninput-int, .functioninput-float { color: #feb1bf; }
  }
  @media (prefers-color-scheme: light) {
    .functioninput-default { color: black; }
    .functionseparators { color: black; }
    .function-name { color: #a17702ff; }
    .string { color: green; }
    .functioninput-int, .functioninput-float { color: red; }"""

# Replacement (can contain backreferences like r"\1" when use_regex is True)
use_regex_for_replacement = False
replacement = r"""@media (prefers-color-scheme: dark) {
    .functioninput-default { color: white; }
    .functionseparators { color: white; }
    .function-name { color: #daaa28ff; }
    .string { color: #52d1c1; }
    .boolean { color: #9ccaff;}
    .functioninput-int, .functioninput-float { color: #feb1bf; }
  }
  @media (prefers-color-scheme: light) {
    .functioninput-default { color: black; }
    .functionseparators { color: black; }
    .function-name { color: #a17702ff; }
    .string { color: green; }
    .boolean { color: #0061a6;}
    .functioninput-int, .functioninput-float { color: red; }"""


filename_contains = "description"
directory_contains = ""
directory_does_not_contain = ""
root_dir = "dodona-exercises/exercises/"

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename_contains in filename and directory_contains in dirpath and ((directory_does_not_contain not in dirpath) or directory_does_not_contain == ""):
            file_path = os.path.join(dirpath, filename)
            print(f"Checking: {file_path}")
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            if use_regex_for_to_replace:
              pattern = re.compile(to_replace, flags=re.DOTALL)
              if use_regex_for_replacement:
                new_content, count = pattern.subn(replacement, content)
              else:
                new_content, count = pattern.subn(lambda m: replacement, content)
              if count > 0:
                with open(file_path, "w", encoding="utf-8") as f:
                  f.write(new_content)
                print(f"Updated (regex, {count} replacements): {file_path}")
            else:
                count = content.count(to_replace)
                if count > 0:
                    new_content = content.replace(to_replace, replacement)
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated (literal, {count} replacements): {file_path}")
