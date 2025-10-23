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
      const codeEl = document.createElement("code");
      codeEl.innerHTML = html;
      el.replaceWith(codeEl);
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
1. Maak een variabele <code>a</code> aan die een <i>float</i> opslaat met een waarde die je zelf goed moet kiezen (zie stap 2). Je mag echter NIET exact dezelfde waarde kiezen als die bij <code>b</code> verwacht wordt.
2. Maak een variabele <code>b</code> aan die de waarde van <code>a</code> omgezet naar een <i>geheel getal</i> opslaat. Zorg dat de waarde van <code>b</code> uitkomt op <code>15</code>. Kies de waarde van <code>a</code> dus correct. Natuurlijk zonder de (verwachte) waarde van <code>a</code> opnieuw op te schrijven.
3. Maak een variabele <code>c</code> aan die de waarde van <code>b</code> omgezet naar een <i>tekst</i> opslaat. Natuurlijk zonder de (verwachte) waarde van <code>a</code> of <code>b</code> opnieuw op te schrijven.