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
Gebruik de juiste datatypen (soorten gegevens) om de fouten uit de gegeven code te halen.

<details><summary>Originele code</summary>
```python
geheel_getal = 8.0
kommagetal = 6,1
zin = Dit is een zin

```
</details>