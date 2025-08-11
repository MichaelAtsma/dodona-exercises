# <b>Opdracht</b>
Schrijf een programma dat de gebruiker om een getal vraagt, en dan het zoveelste Fibonacci getal print.

<details markdown="1"><summary>Wat zijn Fibonacci getallen?</summary>
De Fibonacci getallen vormen een reeks van getallen waarbij elk getal de som is van de vorige twee. Men begint meestal met `1` en `1`, waardoor het derde getal dus `2` is (`1+1=2`). De eerste 20 Fibonacci getallen zijn:

<!-- <style>
  th {
    font-size: 2em;
  }
</style> -->
<table class="table" style="width:60%">
  <thead>
    <tr>
      <th><h3>Index</h3></th>
      <th style="width:40%"><h3>Fibonacci getal</h3></th>
      <th style="width:40%"><h3>Waarom?</h3></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
      <td></td>
    </tr>
    <tr>
      <td>2</td>
      <td>1</td>
      <td></td>
    </tr>
    <tr>
      <td>3</td>
      <td>2</td>
      <td><code>1 + 1 = 2</code></td>
    </tr>
    <tr>
      <td>4</td>
      <td>3</td>
      <td><code>1 + 2 = 3</code></td>
    </tr>
    <tr>
      <td>5</td>
      <td>5</td>
      <td><code>2 + 3 = 5</code></td>
    </tr>
    <tr>
      <td>6</td>
      <td>8</td>
      <td><code>3 + 5 = 8</code></td>
    </tr>
    <tr>
      <td>7</td>
      <td>13</td>
      <td><code>5 + 8 = 13</code></td>
    </tr>
    <tr>
      <td>8</td>
      <td>21</td>
      <td><code>8 + 13 = 21</code></td>
    </tr>
    <tr>
      <td>9</td>
      <td>34</td>
      <td><code>13 + 21 = 34</code></td>
    </tr>
    <tr>
      <td>10</td>
      <td>55</td>
      <td><code>21 + 34 = 55</code></td>
    </tr>
    <tr>
      <td>11</td>
      <td>89</td>
      <td><code>34 + 55 = 89</code></td>
    </tr>
    <tr>
      <td>12</td>
      <td>144</td>
      <td><code>55 + 89 = 144</code></td>
    </tr>
    <tr>
      <td>13</td>
      <td>233</td>
      <td><code>89 + 144 = 233</code></td>
    </tr>
    <tr>
      <td>14</td>
      <td>377</td>
      <td><code>144 + 233 = 377</code></td>
    </tr>
    <tr>
      <td>15</td>
      <td>610</td>
      <td><code>233 + 377 = 610</code></td>
    </tr>
    <tr>
      <td>16</td>
      <td>987</td>
      <td><code>377 + 610 = 987</code></td>
    </tr>
    <tr>
      <td>17</td>
      <td>1597</td>
      <td><code>610 + 987 = 1597</code></td>
    </tr>
    <tr>
      <td>18</td>
      <td>2584</td>
      <td><code>987 + 1597 = 2584</code></td>
    </tr>
    <tr>
      <td>19</td>
      <td>4181</td>
      <td><code>1597 + 2584 = 4181</code></td>
    </tr>
    <tr>
      <td>20</td>
      <td>6765</td>
      <td><code>2584 + 4181 = 6765</code></td>
    </tr>
  </tbody>
</table>


<i>(PS: De eerste twee getallen zijn vrij te kiezen en bepalen hoe de volledige reeks er uit zal zien. In deze opdracht houden we het bij de standaard 1 en 1.)</i>
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
Het 6e Fibonacci getal is: 8.
```
</details>

<details markdown="1"><summary>Voorbeeld 2</summary>
### Invoer
```
10
```

### Uitvoer
```
Het 10e Fibonacci getal is: 55.
```
</details>

<details markdown="1"><summary>Voorbeeld 3</summary>
### Invoer
```
17
```

### Uitvoer
```
Het 17e Fibonacci getal is: 1597.
```
</details>

<details markdown="1"><summary>Voorbeeld 4</summary>
### Invoer
```
20
```

### Uitvoer
```
Het 20e Fibonacci getal is: 6765.
```
</details>