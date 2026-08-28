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
  th.bigger-padding-column {
    padding-left: 150px !important;
    padding-right: 150px !important;
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
    white-space: nowrap !important;
    overflow-wrap: nowrap !important;
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

  pre code { /* give extra space to each line of code block */
    display: block;
    padding: 10px;
    overflow-x: auto;
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

De website [numberfacts.one](https://numberfacts.one/) is een website die allerlei interessante feiten over getallen laat zien. De website is gemaakt door de wiskundige en programmeur Matt Parker. Je kan er bijvoorbeeld de volgende informatie vinden:

<img src="media/numberfactsone.png" alt="numberfacts.one/1337 screenshot">

In deze opdracht ga je dit een heel klein beetje nabootsen.

# <b>Opdracht</b>
Maak een functie <function name="NummerAnalyse"></function> die twee getallen als invoer neemt.
- Het eerste getal <code>n</code> is het getal dat geanalyseerd moet worden.
- Het tweede getal <code>d</code> komt hieronder meer informatie over.

De functie moet 2 dingen op het scherm afdrukken:
<ol>
  <li>Het product van de cijfers van het eerste getal vergeleken met de som van de cijfers van het eerste getal. 
  <ul>
    <li>Als het product van de cijfers gelijk is aan de som van de cijfers, druk dan af: <code class="string">Het product en de som van de cijfers zijn allebei gelijk aan <span style="color: red">X</span>.</code></li>
    <li>Als het product van de cijfers groter is dan de som van de cijfers, druk dan af: <code class="string">Het product van de cijfers (<span style="color: red">X</span>) is groter dan de som van de cijfers (<span style="color: red">Y</span>).</code></li>
    <li>Als het product van de cijfers kleiner is dan de som van de cijfers, druk dan af: <code class="string">Het product van de cijfers (<span style="color: red">X</span>) is kleiner dan de som van de cijfers (<span style="color: red">Y</span>).</code></li>
  </ul>
  </li>
  <li>De deling van het eerste getal door het tweede getal.
  <ul>
    <li>Als het eerste getal deelbaar is door het tweede getal, druk dan af: <code class="string"><span style="color: red">n</span> is een veelvoud van <span style="color: red">d</span>.</code></li>
    <li>Als het eerste getal niet deelbaar is door het tweede getal, druk dan af: <code class="string"><span style="color: red">n</span> is niet deelbaar door <span style="color: red">d</span>, het resultaat is ongeveer <span style="color: red">Z</span>.</code></li>
  </ul>
  </li>
</ol>

waarbij <span style="color: red">X</span> het product van de cijfers is, <span style="color: red">Y</span> de som van de cijfers is, en <span style="color: red">Z</span> het resultaat van de deling is afgerond op 2 decimalen.

<details markdown="1"><summary>input-output verwachtingen</summary>

<div class="table-scroll">
<table>
  <thead>
    <tr>
      <th>Invoer</th>
      <th class="padding-column">→</th>
      <th>Verwachte output</th>
      <th>Uitleg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><function name="NummerAnalyse" inputs='123,7'></function></td>
      <td style="text-align: center;">→</td>
      <td><pre><code>Het product en de som van de cijfers zijn allebei gelijk aan 6.     <br>123 is niet deelbaar door 7, het resultaat is ongeveer 17.57.</code></pre></td>
      <td>Het product van de cijfers van <code>123</code> is $$1 \cdot 2 \cdot 3 = 6$$.<br>De som van de cijfers van <code>123</code> is $$1 + 2 + 3 = 6$$.<br>Het product en de som zijn dus gelijk.<br>$$123 / 7 \approx 17.57$$</td>
    </tr>
    <tr>
      <td><function name="NummerAnalyse" inputs='456,2'></function></td>
      <td style="text-align: center;">→</td>
      <td><pre><code>Het product van de cijfers (120) is groter dan de som van de cijfers (15).     <br>456 is een veelvoud van 2.</code></pre></td>
      <td>Het product van de cijfers van <code>456</code> is $$4 \cdot 5 \cdot 6 = 120$$.<br>De som van de cijfers van <code>456</code> is $$4 + 5 + 6 = 15$$.<br>Het product is dus groter dan de som.<br>$$456 / 2 = 228$$, dus <code>456</code> is exact een veelvoud van <code>2</code>.</td>
    </tr>
    <tr>
      <td><function name="NummerAnalyse" inputs='111112,3'></function></td>
      <td style="text-align: center;">→</td>
      <td><pre><code>Het product van de cijfers (2) is kleiner dan de som van de cijfers (7).     <br>111112 is niet deelbaar door 3, het resultaat is ongeveer 37037.33.</code></pre></td>
      <td>Het product van de cijfers van <code>111112</code> is $$1 \cdot 1 \cdot 1 \cdot 1 \cdot 1 \cdot 2 = 2$$.<br>De som van de cijfers van <code>111112</code> is $$1 + 1 + 1 + 1 + 1 + 2 = 7$$.<br>Het product is dus kleiner dan de som.<br>$$111112 / 3 \approx 37037.33$$</td>
    </tr>
  </tbody>
</table>
</div>

</details> <!-- End of input-output verwachtingen -->

</div>