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
Maak een functie genaamd <function name="TweetValidatie"></function> die één tekst (<i>string</i>) als invoer neemt (een tweet/post voor Twitter/X), en dan een validatie teruggeeft die aangeeft of de tweet een correcte lengte heeft.
- Als de tweet 5 of minder tekens bevat: <code>"Te korte tweet."</code>
- Als de tweet tussen de 5 en 280 tekens bevat (exclusief 5 en inclusief 280): <code>"Geldige tweet."</code>
- Als de tweet meer dan 280 tekens bevat: <code>"Te lange tweet."</code>


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
      <td><function name="TweetValidatie" inputs='"hoi"'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Te korte tweet."</code></td>
    </tr>
    <tr>
      <td><function name="TweetValidatie" inputs='"Hallo"'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Te korte tweet."</code></td>
    </tr>
    <tr>
      <td><function name="TweetValidatie" inputs='"POV: je leerkracht is cringe met taalgebruik"'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Geldige tweet."</code></td>
    </tr>
    <tr>
      <td style='white-space:normal'><function name="TweetValidatie" inputs='"Dit is een tweet die precies 280 tekens bevat. Zou je niet denken hè? Heb jij het aantal tekens geteld? Let op dat de spaties ook mee doen! We zijn nu ongeveer op de helft. Voeg jij wel eens wat woorden toe aan je verslagen zodat je het minimum aantal woorden behaalt? We zijn er!"'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Geldige tweet."</code></td>
    </tr>
    <tr>
      <td style='white-space:normal'><function name="TweetValidatie" inputs='"Dit is een tweet die meer dan 280 tekens bevat. Lorum ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."'></function></td>
      <td style="text-align: center;">→</td>
      <td><code>"Te lange tweet."</code></td>
    </tr>
  </tbody>
</table>
</div>
</details>