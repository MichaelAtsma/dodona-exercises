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
Maak een functie genaamd <function name="KlasUitslag"></function> die twee getallen (<i>integers</i>) als invoer neemt (het aantal leerlingen van de klas die geslaagd zijn voor hun examen, en het totaal aantal leerlingen in de klas), en dan een bericht teruggeeft die aangeeft hoe goed de klas het gedaan heeft.
- Als minder dan 50% van de leerlingen geslaagd is: <code>"Minder dan de helft van de klas is geslaagd voor het examen."</code>
- Als er tussen de 50% en 80% van de leerlingen geslaagd is (inclusief 50% en 80%): <code>"Een voldoende aantal leerlingen is geslaagd voor het examen."</code>
- Als 80% of meer van de leerlingen geslaagd is: <code>"Wow, wat een sterke klas zijn jullie!"</code>


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
      <td><function name="KlasUitslag" inputs='7, 22'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Minder dan de helft van de klas is geslaagd voor het examen."</code></td>
      <td>7 is ongeveer 32% van 22, dus minder dan 50%.</td>
    </tr>
    <tr>
      <td><function name="KlasUitslag" inputs='9, 18'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Een voldoende aantal leerlingen is geslaagd voor het examen."</code></td>
      <td>9 is exact 50% van 18.</td>
    </tr>
    <tr>
      <td><function name="KlasUitslag" inputs='13, 19'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Een voldoende aantal leerlingen is geslaagd voor het examen."</code></td>
      <td>13 is ongeveer 68% van 19, dus tussen 50% en 80%.</td>
    </tr>
    <tr>
      <td><function name="KlasUitslag" inputs='16, 20'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Een voldoende aantal leerlingen is geslaagd voor het examen."</code></td>
      <td>16 is exact 80% van 20.</td>
    </tr>
    <tr>
      <td><function name="KlasUitslag" inputs='20, 21'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Wow, wat een sterke klas zijn jullie!"</code></td>
      <td>20 is ongeveer 95% van 21, dus meer dan 80%.</td>
    </tr>
  </tbody>
</table>
</div>
</details>