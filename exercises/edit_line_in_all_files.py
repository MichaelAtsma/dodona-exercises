import os

to_replace = '</script>'
replacement = """
   // Function to wrap strings in <code> elements with a green span
   // Not tested with <pre><code> blocks, and I think it's probably not robust against this.
    function highlightStringsInCode() {
      document.querySelectorAll('code').forEach(function(codeElem) {
        // Replace all "string" or 'string' with a green span, unless already wrapped in a span
        codeElem.innerHTML = codeElem.innerHTML.replace(
          /(["'])(?!<span[^>]*>)([^"'<]*?)(?!<\\/span>)(\\1)(?![^<]*<\\/span>)/g,
            function(match, quote, content) {
              // Only wrap if not already inside a <span>
              if (/<span[^>]*>.*<\/span>/.test(match)) return match;
              return '<span style="color: green;">' + quote + content + quote + '</span>';
            }
        );
      });
    }
  document.addEventListener("DOMContentLoaded", highlightStringsInCode);
</script>"""
filename_contains = "description"
root_dir = "exercises"

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename_contains in filename:
            file_path = os.path.join(dirpath, filename)
            print(f"Checking: {file_path}")
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            changed = False
            new_lines = []
            for line in lines:
                if to_replace in line:
                    line = line.replace(
                        to_replace,
                        replacement
                    )
                    changed = True
                new_lines.append(line)
            if changed:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.writelines(new_lines)
                print(f"Updated: {file_path}")
