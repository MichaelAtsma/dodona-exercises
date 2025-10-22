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
Maak een variabele <code>Felicitatie</code> aan die een score van <code>6.66667</code> van de variabele <code>score</code> afgerond op drie decimalen invult in de tekst <code>Als je de oefeningen tot en met deze correct hebt, dan heb je al een 6.667/10 behaald voor je toets!</code> met een <i>f-string</i>.