<script>
  document.addEventListener("copy", function(e) {
    e.preventDefault();
    e.clipboardData.setData("text/plain", "");
  });

  document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll("function").forEach(el => {
      const name = el.getAttribute("name");
      const inputsAttr = el.getAttribute("inputs");
      let html = `<span class="function">${name}</span>`;
      if (inputsAttr && inputsAttr.trim() !== "") {
        const inputs = inputsAttr.split(",");
        html += `<span class="functionseparators">(</span>`;
        html += inputs.map((input, i) => {
          const trimmed = input.trim();
          let typeClass = "functioninput-str"; // default to string
          if (/^-?\d+$/.test(trimmed)) {
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
</script>

<style>
  .invisible-text {
    color: transparent;
    font-size: 0.1em;
    display: inline;
    margin: 0;
    padding: 0;
  }
  /* To use this, put any text like this: 
  <span class="invisible-text">Your invisible text here</span> 
  */

  table {
    margin: 0 auto;       /* centers table horizontally */
  }
  th {
    font-size: 1.2em !important;
    white-space: nowrap;
  }
  td {
    white-space: nowrap;
  }

  .functioninput-int, .functioninput-float { color: red; }
  .functioninput-str { color: green; }
  .function { color: #a17702ff; }
  .functionseparators { color: black; }
</style>

# <b>Opdracht</b>
Maak een functie genaamd <function name="ToetsPunt"></function> die <i><b>drie</b></i> getallen als invoer neemt:
<ol>
  <li>Het behaalde aantal punten op de toets</li>
  <li>Het maximaal aantal te behalen punten op de toets</li>
  <li>De maximale score waar het naar omgerekend moet worden</li>
</ol>
De functie rekent dan de score om en geeft het resultaat terug.

<details><summary>Voorbeelden</summary>
<ul>
  <li><function name="ToetsPunt" inputs="4,7,5"></function> geeft <code>2.857142857142857</code> terug (want <code>4</code> op <code>7</code> is gelijk aan <code>2.857142857142857</code> op <code>5</code>).</li>
  <li><function name="ToetsPunt" inputs="6,12,20"></function> geeft <code>10</code> terug (want <code>6</code> op <code>12</code> is gelijk aan <code>10</code> op <code>20</code>).</li>
  <li><function name="ToetsPunt" inputs="3,12,10"></function> geeft <code>2.5</code> terug (want <code>3</code> op <code>12</code> is gelijk aan <code>2.5</code> op <code>10</code>).</li>
</ul>
</details>