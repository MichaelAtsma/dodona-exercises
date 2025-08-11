# <b>Opdracht</b>

Schrijf een programma dat de gebruiker om een positief geheel getal vraagt, en dan de volledige Collatz-reeks (ook wel <code>3n + 1</code>-reeks genoemd) afdrukt, beginnend bij dat getal en eindigend bij 1.

<details markdown="1"><summary>Wat is de Collatz Conjecture?</summary>  
De Collatz Conjecture stelt dat je, voor elk positief geheel getal, steeds het volgende getal kunt berekenen volgens deze regels:  

1. **Is het getal even?** Deel het door 2.
2. **Is het getal oneven?** Vermenigvuldig het met 3 en tel er 1 bij op.

Herhaal deze stappen steeds opnieuw. Volgens de hypothese kom je uiteindelijk altijd bij het getal 1, ongeacht welk positief geheel getal je kiest.

Hieronder zie je enkele voorbeelden:

<style>
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

<table class="table" style="width:50%">
  <thead>
    <tr>
      <th>Startgetal</th>
      <th>Collatz-reeks</th>
      <th>Waarom?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>6</td>
      <td>6, 3, 10, 5, 16, 8, 4, 2, 1</td>
      <td>
        <code>6 / 2 = 3</code><br>
        <code>3 × 3 + 1 = 10</code><br>
        <code>10 / 2 = 5</code><br>
        ...
      </td>
    </tr>
    <tr>
      <td>11</td>
      <td>11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1</td>
      <td>
        <code>11 × 3 + 1 = 34</code><br>
        <code>34 / 2 = 17</code><br>
        ...
      </td>
    </tr>
    <tr>
      <td>19</td>
      <td>19, 58, 29, 88, 44, 22, 11, ... , 2, 1</td>
      <td>
        <code>19 × 3 + 1 = 58</code><br>
        <code>58 / 2 = 29</code><br>
        ...
      </td>
    </tr>
  </tbody>
</table>

<i>(PS: Hoewel deze hypothese nog niet wiskundig bewezen is, heeft niemand tot nu toe een positief geheel getal gevonden dat niet eindigt op 1.)</i>

</details>  

<br>  
<br>  

# <b>Voorbeelden</b>

<details markdown="1"><summary>Voorbeeld 1</summary>  
### Invoer  
```
6
```  

### Uitvoer

```
Collatz-reeks: 6, 3, 10, 5, 16, 8, 4, 2, 1.
```

</details>  

<details markdown="1"><summary>Voorbeeld 2</summary>  
### Invoer  
```
11
```  

### Uitvoer

```
Collatz-reeks: 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.
```

</details>  

<details markdown="1"><summary>Voorbeeld 3</summary>  
### Invoer  
```
19
```  

### Uitvoer

```
Collatz-reeks: 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.
```

</details>  
