<script>
  let copyMessage = "";

  document.addEventListener("copy", function(e) {
    e.preventDefault();
    e.clipboardData.setData("text/plain", copyMessage);
  });

  document.addEventListener("cut", function(e) {
    e.preventDefault();
    e.clipboardData.setData("text/plain", copyMessage);
  });

  document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll("function").forEach(el => {
      const name = el.getAttribute("name");
      const inputsAttr = el.getAttribute("inputs");
      let html = `<span class="function-name">${name}</span>`;
      if (inputsAttr) {  // Put only a space in the inputs attribute if you want the function to appear with brackets but no inputs
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
Maak een functie genaamd <function name="RacePrestatie"></function> die één getal (<i>integer</i> of <i>float</i>) als invoer neemt (het aantal uur dat iemand doet over het lopen van de 20km van Brussel), en dan een bericht teruggeeft die aangeeft in welke wave die persoon mag beginnen.
- Als die sneller dan 1.25 uur is: <code>"Elite."</code>
- Als die tussen 1.25 en 1.75 uur loopt (inclusief 1.25, exclusief 1.75): <code>"Wave 1: snelle lopers."</code>
- Als die tussen 1.75 en 2.25 uur loopt (inclusief 1.75, exclusief 2.25): <code>"Wave 2: gemiddelde lopers."</code>
- Als die trager dan 2.25 uur loopt (inclusief 2.25): <code>"Wave 3: overige lopers."</code>

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
      <td><function name="RacePrestatie" inputs='1'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Elite."</code></td>
    </tr>
    <tr>
      <td><function name="RacePrestatie" inputs='1.25'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Wave 1: snelle lopers."</code></td>
    </tr>
    <tr>
      <td><function name="RacePrestatie" inputs='1.5'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Wave 1: snelle lopers."</code></td>
    </tr>
    <tr>
      <td><function name="RacePrestatie" inputs='1.75'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Wave 2: gemiddelde lopers."</code></td>
    </tr>
    <tr>
      <td><function name="RacePrestatie" inputs='2'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Wave 2: gemiddelde lopers."</code></td>
    </tr>
    <tr>
      <td><function name="RacePrestatie" inputs='2.25'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Wave 3: overige lopers."</code></td>
    </tr>
    <tr>
      <td><function name="RacePrestatie" inputs='2.5'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Wave 3: overige lopers."</code></td>
    </tr>
  </tbody>
</table>
</div>
</details>