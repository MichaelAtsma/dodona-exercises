<script>
  let copiedText = "";

  document.addEventListener("copy", function(e) {
    e.preventDefault();
    copiedText = window.getSelection().toString();
    e.clipboardData.setData("text/plain", "You are not allowed to copy text from this page.");
  });

  document.addEventListener("cut", function(e) {
    e.preventDefault();
    copiedText = window.getSelection().toString();
    e.clipboardData.setData("text/plain", "You are not allowed to copy text from this page.");
  });

  try {
    const targetDoc = window.parent ? window.parent.document : document;
    targetDoc.addEventListener("paste", function(e) {
      e.preventDefault();
      document.execCommand('insertText', false, copiedText);
    }, true);
  } catch (e) {
    // fall-back for when we can't access the parent document
    document.addEventListener("paste", function(e) {
      e.preventDefault();
      document.execCommand('insertText', false, copiedText);
    }, true);
  }

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
</style>

# <b>Opdracht</b>
Maak een functie genaamd <function name="BoekDikte"></function> die één getal (<i>integers</i>) als invoer neemt (het aantal pagina's van een boek), en dan een bericht teruggeeft die aangeeft hoe dik dat boek is.
- Als het boek minder dan 150 pagina's heeft: <code>"Dit is een dun boek."</code>
- Als het boek tussen de 150 en 300 pagina's heeft (inclusief 150 en 300): <code>"Dit is een normaal boek."</code>
- Als het boek meer dan 300 pagina's heeft: <code>"Dit is een dik boek."</code>

<details markdown="1"><summary>input-output verwachtingen</summary>

<div class="table-scroll">
<table>
  <thead>
    <tr>
      <th>Invoer</th>
      <th class="padding-column">→</th>
      <th>Verwachte returnwaarde</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><function name="BoekDikte" inputs='90'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Dit is een dun boek."</code></td>
    </tr>
    <tr>
      <td><function name="BoekDikte" inputs='150'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Dit is een normaal boek."</code></td>
    </tr>
    <tr>
      <td><function name="BoekDikte" inputs='223'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Dit is een normaal boek."</code></td>
    </tr>
    <tr>
      <td><function name="BoekDikte" inputs='300'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Dit is een normaal boek."</code></td>
    </tr>
    <tr>
      <td><function name="BoekDikte" inputs='350'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Dit is een dik boek."</code></td>
    </tr>
  </tbody>
</table>
</div>
</details>