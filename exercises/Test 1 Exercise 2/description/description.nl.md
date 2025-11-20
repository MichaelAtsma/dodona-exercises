<script>
  document.addEventListener("copy", function(e) {
    e.preventDefault();
    e.clipboardData.setData("text/plain", "");
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
              return '<span style="color: green;">' + quote + content + quote + '</span>';
            }
        );
      });
    }
  document.addEventListener("DOMContentLoaded", highlightStringsInCode);
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
</style>

# <b>Opdracht</b>
1. Maak een variabele <code>getal1</code> die de waarde <code>5</code> opslaat.
2. Maak een variabele <code>getal2</code> die de waarde <code>-9</code> opslaat.
3. Maak een variabele <code>woord</code> die het woord <code>octopus</code> opslaat.
4. Maak een variabele <code>som</code> die de som van <code>getal1</code> en <code>getal2</code> opslaat.
5. Maak een variabele <code>product</code> die het product van <code>getal1</code> en <code>getal2</code> opslaat.
6. Maak een variabele <code>quotient</code> die het resultaat van <code>getal1</code> gedeeld door <code>getal2</code> opslaat.
7. Maak een variabele <code>meerdere_woorden</code> die <code>getal1</code> keer <code>woord</code> opslaat.