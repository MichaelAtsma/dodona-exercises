<script>
  let copyMessage = "";

  document.addEventListener("copy", function(e) {
    e.preventDefault();
    const selection = window.getSelection().toString();
    if (selection.includes("€")) {
      e.clipboardData.setData("text/plain", "€");
    } else {
      e.clipboardData.setData("text/plain", copyMessage);
    }
  });

  document.addEventListener("cut", function(e) {
    e.preventDefault();
    const selection = window.getSelection().toString();
    if (selection.includes("€")) {
      e.clipboardData.setData("text/plain", "€");
    } else {
      e.clipboardData.setData("text/plain", copyMessage);
    }
  });

  function splitInputsTopLevel(inputText) {
    const parts = [];
    let current = "";
    let inQuote = false;
    let quoteChar = "";
    let bracketDepth = 0;
    let escapeComma = false;

    for (let i = 0; i < inputText.length; i++) {
      const ch = inputText[i];

      if (escapeComma) {
        current += ch;
        escapeComma = false;
        continue;
      }

      if (ch === "\\" && inputText[i + 1] === ",") {
        current += ch;
        escapeComma = true;
        continue;
      }

      if ((ch === '"' || ch === "'") && inputText[i - 1] !== "\\") {
        if (!inQuote) {
          inQuote = true;
          quoteChar = ch;
        } else if (quoteChar === ch) {
          inQuote = false;
          quoteChar = "";
        }
        current += ch;
        continue;
      }

      if (!inQuote) {
        if (ch === "[" || ch === "(" || ch === "{") bracketDepth++;
        if (ch === "]" || ch === ")" || ch === "}") bracketDepth = Math.max(0, bracketDepth - 1);
        if (ch === "," && bracketDepth === 0) {
          parts.push(current.trim());
          current = "";
          continue;
        }
      }

      current += ch;
    }

    if (current.trim().length > 0) parts.push(current.trim());
    return parts;
  }

  document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll("function").forEach(el => {
      const name = el.getAttribute("name");
      const inputsAttr = el.getAttribute("inputs");
      let html = `<span class="function-name">${name}</span>`;
      if (inputsAttr) {  // Put only a space in the inputs attribute if you want the function to appear with brackets but no inputs
        const inputs = splitInputsTopLevel(inputsAttr);
        html += `<span class="functionseparators">(</span>`;
        const formatValue = (value) => {
          const trimmed = value.trim();
          if (/^\[.*\]$/.test(trimmed)) {
            const inner = trimmed.slice(1, -1).trim();
            const items = inner.length ? splitInputsTopLevel(inner) : [];
            const renderedItems = items.map((item, idx) => {
              return `${formatValue(item)}${idx < items.length - 1 ? '<span class="functionseparators">, </span>' : ''}`;
            }).join('');
            return `<span class="functionseparators">[</span>${renderedItems}<span class="functionseparators">]</span>`;
          }

          let typeClass = "functioninput-default"; // default to default
          if (/^["'].*["']$/.test(trimmed)) {
            typeClass = "string";
          } else if (/^-?\d+$/.test(trimmed)) {
            typeClass = "functioninput-int";
          } else if (/^-?\d*\.\d+$/.test(trimmed)) {
            typeClass = "functioninput-float";
          }
          const renderedValue = typeClass === "string" ? trimmed.replace(/\\,/g, ",") : trimmed;
          return `<span class="${typeClass}">${renderedValue}</span>`;
        };

        html += inputs.map((input, i) => {
          return `${formatValue(input)}${i < inputs.length - 1 ? '<span class="functionseparators">, </span>' : ''}`;
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

  .prevent-select {
    -webkit-user-select: none; /* Safari */
    -ms-user-select: none; /* IE 10 and IE 11 */
    user-select: none; /* Standard syntax */
  }

  .enable-select {
    -webkit-user-select: text; /* Safari */
    -ms-user-select: text; /* IE 10 and IE 11 */
    user-select: text; /* Standard syntax */
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
    padding-left: 20px !important;
    padding-right: 20px !important;
  }
  th.medium-padding-column {
    padding-left: 50px !important;
    padding-right: 50px !important;
  }
  th.big-padding-column {
    padding-left: 100px !important;
    padding-right: 100px !important;
  }
  th.huge-padding-column {
    padding-left: 200px !important;
    padding-right: 200px !important;
  }
  td {
    padding: 4px 10px !important;
    box-sizing: border-box;
    border: 1px solid #8f8f8fff !important;
    border-style: solid !important;
    white-space: normal;
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
    .boolean { color: #9ccaff;}
    .functioninput-int, .functioninput-float { color: #feb1bf; }
  }
  @media (prefers-color-scheme: light) {
    .functioninput-default { color: black; }
    .functionseparators { color: black; }
    .function-name { color: #a17702ff; }
    .string { color: green; }
    .boolean { color: #0061a6;}
    .functioninput-int, .functioninput-float { color: red; }
  }
</style>

<div markdown="1" class="prevent-select">

# <b>Opdracht</b>
Maak een functie <function name="Kassa"></function> die een lijst als invoer neemt. De lijst bevat de prijzen van de producten in de winkelwagen, en ergens in de lijst staat het woord "subtotaal". De functie moet de som van de prijzen berekenen en deze afdrukken op het scherm. Er kan meerdere keren het woord "subtotaal" voorkomen, en je moet iedere keer dat je dit woord tegenkomt de som van de prijzen tot dan toe afdrukken, en daarna verder gaan met het optellen van de volgende prijzen. Nadat je klaar bent met het optellen van alle prijzen, moet je de totale prijs op het scherm afdrukken. Je drukt de prijzen af in het volgende formaat:

<ul>
  <li><code class="string">Het subtotaal van de eerste X producten is <span class="enable-select">€</span>YY.YY</code>, waarbij <code>X</code> het aantal producten is dat je tot dan toe hebt opgeteld, en <code>YY.YY</code> het subtotaal is van die producten.</li>
  <li><code class="string">De totale prijs van de winkelmand is <span class="enable-select">€</span>ZZ.ZZ</code>, waarbij <code>ZZ.ZZ</code> het totaal is van alle producten in de winkelmand.</li>
</ul>

<details markdown="1"><summary>input-output verwachtingen</summary>

<div class="table-scroll">
<table>
  <thead>
    <tr>
      <th>Invoer</th>
      <th class="padding-column">→</th>
      <th>Verwachte output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><function name="Kassa" inputs='[2, 5]'></function></td>
      <td style="text-align: center;">→</td>
      <td>De totale prijs van de winkelmand is €7.00</code></td>
    </tr>
    <tr>
      <td><function name="Kassa" inputs='[10, 20, "subtotaal", 30, 40]'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>Het subtotaal van de eerste 2 producten is €30.00<br>De totale prijs van de winkelmand is €100.00</code></td>
    </tr>
    <tr>
      <td><function name="Kassa" inputs='[1.49, 0.95, "subtotaal", 2, "subtotaal", 5.11]'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>Het subtotaal van de eerste 2 producten is €2.44<br>Het subtotaal van de eerste 3 producten is €4.44<br>De totale prijs van de winkelmand is €9.55</code></td>
    </tr>
    <tr>
      <td><function name="Kassa" inputs='[1.234, "subtotaal", 6.413]'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>Het subtotaal van de eerste 1 producten is €1.23<br>De totale prijs van de winkelmand is €7.65</code></td>
    </tr>
    <tr>
      <td><function name="Kassa" inputs='[]'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>De totale prijs van de winkelmand is €0.00</code></td>
    </tr>
    <tr>
      <td><function name="Kassa" inputs='["subtotaal"]'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>Het subtotaal van de eerste 0 producten is €0.00<br>De totale prijs van de winkelmand is €0.00</code></td>
    </tr>
  </tbody>
</table>
</div>

</details> <!-- End of input-output verwachtingen -->

<br>
<hr>

<details markdown="1"><summary>Tip (twee voorwaarden tegelijk)</summary>

Je kan in een if-statement meerdere voorwaarden tegelijk controleren door gebruik te maken van <code>and</code>. Bijvoorbeeld:

```python
if x > 2 and x < 10:
    print("x is tussen 2 en 10.")
```

of

```python
if x > 0 and y > 0:
    print("x en y zijn allebei positief.")
```

</details> <!-- End of tip (twee voorwaarden tegelijk) -->

</div>