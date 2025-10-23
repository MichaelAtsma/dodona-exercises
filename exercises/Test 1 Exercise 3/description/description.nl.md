<script>
  document.addEventListener("copy", function(e) {
    e.preventDefault();
    e.clipboardData.setData("text/plain", "");
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
</style>

# <b>Opdracht</b>
Maak een variabele <code>uitspraak</code> aan die de inhoud van <code>35</code> liter van de variabele <code>inhoud</code> en het automerk <code>Toyota</code> van de variabele <code>automerk</code> invult in de zin <code>Er past 35 liter benzine in mijn Toyota.</code> met een <i>f-string</i>.