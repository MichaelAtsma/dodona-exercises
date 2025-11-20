import os
import re

# Pattern or literal to replace
use_regex_for_to_replace = True
to_replace = r"""document.addEventListener\("copy".*</style>"""

# Replacement (can contain backreferences like r"\1" when use_regex is True)
use_regex_for_replacement = False
replacement = r"""document.addEventListener("copy", function(e) {
    e.preventDefault();
    const selection = window.getSelection().toString();
    const modified = selection.length > 75 ? prependText + selection : selection;
    e.clipboardData.setData("text/plain", modified);
  });

  document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll("function").forEach(el => {
      const name = el.getAttribute("name");
      const inputsAttr = el.getAttribute("inputs");
      let html = `<span class="function-name">${name}</span>`;
      if (inputsAttr && inputsAttr.trim() !== "") {
        const inputs = inputsAttr.split(",");
        html += `<span class="functionseparators">(</span>`;
        html += inputs.map((input, i) => {
          const trimmed = input.trim();
          let typeClass = "functioninput-default"; // default to default
          if (/^["'].*["']$/.test(trimmed)) {
            typeClass = "string";
          } else if (/^-?\d+$/.test(trimmed)) {
            typeClass = "functioninput-int";
          } else if (/^-?\d*\.\d+$/.test(trimmed)) {
            typeClass = "functioninput-float";
          }
          return `<span class="${typeClass}">${trimmed}</span>${i < inputs.length - 1 ? '<span class="functionseparators">, </span>' : ''}`;
        }).join('');
        html += `<span class="functionseparators">)</span>`;
      }
      el.outerHTML = `<code>${html}</code>`;
    });
  });

   // Function to wrap strings in <code> elements with a green span
   // Not tested with <pre><code> blocks, and I think it's probably not robust against this.
    function highlightStringsInCode() {
      document.querySelectorAll('code').forEach(function(codeElem) {
        // Replace all "string" or 'string' with a green span, unless already wrapped in a span
        codeElem.innerHTML = codeElem.innerHTML.replace(
          /(["'])(?!<span[^>]*>)([^"'<]*?)(?!<\/span>)(\1)(?![^<]*<\/span>)/g,
            function(match, quote, content) {
              // Only wrap if not already inside a <span>
              if (/<span[^>]*>.*<\/span>/.test(match)) return match;
              return '<span class="string">' + quote + content + quote + '</span>';
            }
        );
      });
    }
  document.addEventListener("DOMContentLoaded", highlightStringsInCode);
</script>

<style>
  .invisible-text {
    /* To use this, put any text like this: 
    <span class="invisible-text">Your invisible text here</span> 
    */
    color: transparent;
    font-size: 0.1em;
    display: inline;
    margin: 0;
    padding: 0;
  }

  table {
    display: table;
    margin: 0 auto;       /* centers table horizontally */
    border-collapse: collapse !important;
    border: 1px solid #444 !important;
    border-style: solid !important;
  }
  .table-scroll {
    /* Enables horizontal scrolling for tables wider than the screen.
    To enable, wrap your table in a <div class="table-scroll"> */
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
  th {
    padding: 0px 10px !important;
    box-sizing: border-box;
    border: 1px solid #8f8f8fff !important;
    border-style: solid !important;
    font-size: 1.2em !important;
    white-space: nowrap;
  }
  th.padding-column {
    padding-left: 20px;
    padding-right: 20px;
  }
  td {
    padding: 4px 10px !important;
    box-sizing: border-box;
    border: 1px solid #8f8f8fff !important;
    border-style: solid !important;
    white-space: nowrap;
  }
  .sub-title-in-table {
    font-size: 0.8em !important;
    font-style: italic !important;
    white-space: normal !important;
    overflow-wrap: normal !important;
    word-wrap: normal !important;
    word-break: normal !important;
    hyphens: none !important;
    -webkit-hyphens: none !important;
    -moz-hyphens: none !important;
    -ms-hyphens: none !important;
  }

  @media (prefers-color-scheme: dark) {
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
    .functioninput-int, .functioninput-float { color: red; }
  }
</style>"""


filename_contains = "description"
directory_contains = ""
directory_does_not_contain = "Test 1 Exercise"
root_dir = "exercises"

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename_contains in filename and directory_contains in dirpath and ((directory_does_not_contain not in dirpath) or directory_does_not_contain == ""):
            file_path = os.path.join(dirpath, filename)
            if directory_does_not_contain in file_path:
                print("\n\n\n\n", dirpath, "\n", dirnames, "\n", filenames, "\n\n\n\n")
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
