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
Maak een functie genaamd <function name="InkomstenBelasting"></function> die één getal (<i>integer</i> of <i>float</i>) als invoer neemt (het jaarlijks inkomen in €), en dan een bericht teruggeeft die aangeeft hoeveel procent belasting je moet betalen en ook hoeveel € dit dan is.
- Als het minder dan 10000 is: <code>"Je moet 10% belasting betalen. Dat is dus €[bedrag]."</code>
- Als het tussen 10000 en 50000 is (inclusief 10000, exclusief 50000): <code>"Je moet 20% belasting betalen. Dat is dus €[bedrag]."</code>
- Als 50000 of meer is: <code>"Je moet 40% belasting betalen. Dat is dus €[bedrag]."</code>

Je hoeft niets met afronden te doen.

<details markdown="1"><summary>input-output verwachtingen</summary>

<div class="table-scroll">
<table>
  <thead>
    <tr>
      <th>Invoer</th>
      <th class="padding-column">→</th>
      <th>Verwachte returnwaarde</th>
      <th>Reden</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><function name="InkomstenBelasting" inputs='5832'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Je moet 10% belasting betalen. Dat is dus €583.2."</code></td>
      <td><code>5832</code> minder is dan <code>10000</code>, en 10% van <code>5832</code> is <code>583.2</code></td>
    </tr>
    <tr>
      <td><function name="InkomstenBelasting" inputs='10000'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Je moet 20% belasting betalen. Dat is dus €2000.0."</code></td>
      <td>20% van <code>10000</code> is <code>2000.0</code></td>
    </tr>
    <tr>
      <td><function name="InkomstenBelasting" inputs='31893'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Je moet 20% belasting betalen. Dat is dus €6378.6."</code></td>
      <td><code>31893</code> zit tussen <code>10000</code> en <code>50000</code>, en 20% van <code>31893</code> is <code>6378.6</code></td>
    </tr>
    <tr>
      <td><function name="InkomstenBelasting" inputs='50000'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Je moet 40% belasting betalen. Dat is dus €20000.0."</code></td>
      <td>40% van <code>50000</code> is <code>20000.0</code></td>
    </tr>
    <tr>
      <td><function name="InkomstenBelasting" inputs='62530.45'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Je moet 40% belasting betalen. Dat is dus €25012.18."</code></td>
      <td><code>62530.45</code> is meer dan <code>50000</code>, en 40% van <code>62530.45</code> is <code>25012.18</code></td>
    </tr>
  </tbody>
</table>
</div>
</details>

<i>*Opmerking: de berekening van de belasting is voor deze opdracht vereenvoudigd. Dit is niet hoe het in het echt berekend wordt.</i>