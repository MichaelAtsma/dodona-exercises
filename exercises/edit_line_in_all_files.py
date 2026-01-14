import os
import re

# Pattern or literal to replace
use_regex_for_to_replace = False
to_replace = r"""  document.addEventListener("copy", function(e) {
    e.preventDefault();
    const selection = window.getSelection().toString();
    const modified = selection.length > 75 ? prependText + selection : selection;
    e.clipboardData.setData("text/plain", modified);
  });"""

# Replacement (can contain backreferences like r"\1" when use_regex is True)
use_regex_for_replacement = False
replacement = r"""  document.addEventListener("copy", function(e) {
    e.preventDefault();
    const selection = window.getSelection().toString();
    const modified = selection.length > 75 ? prependText + selection : selection;
    e.clipboardData.setData("text/plain", modified);
  });
  
  // Handle cut event similarly. No need to delete selection, because this only runs in the description, not an editable field.
  document.addEventListener("cut", function(e) {
    e.preventDefault();
    const selection = window.getSelection().toString();
    const modified = selection.length > 75 ? prependText + selection : selection;
    e.clipboardData.setData("text/plain", modified);
  });"""


filename_contains = "description"
directory_contains = ""
directory_does_not_contain = ""
root_dir = "exercises"

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
