# <b>Assignment</b>
Write a program that asks the user for a number, and then prints the Fibonacci number at that index.

<details markdown="1"><summary>What are Fibonacci numbers?</summary>
The Fibonacci numbers form a sequence of numbers where each number is the sum of the previous two. It usually starts with `1` and `1`, which makes the third number `2` (`1+1=2`). The first 20 Fibonacci numbers are:

<style>
  table {
    margin: 0 auto;       /* centers table horizontally */
  }
  th {
    font-size: 1.2em;
    white-space: nowrap;
  }
  td {
    white-space: nowrap;
  }
</style>
<table class="table" style="width:50%">
  <thead>
    <tr>
      <th>Index</th>
      <th>Fibonacci getal</th>
      <th>Waarom?</th>
    </tr>
  </thead>
<table class="table" style="width:50%">
  <thead>
    <tr>
      <th>Index</th>
      <th>Fibonacci number</th>
      <th>Why?</th>
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


<i>(PS: The first two numbers can be chosen freely and decide what the entire sequence will look like. In this assignment we will just condisder the standard 1 and 1.)</i>
</details>
 
<br>
<br> 
 
# <b>Examples</b>
<details markdown="1"><summary>Example 1</summary>
### Input
```
6
```

### Output
```
Fibonacci number 6 is: 8.
```
</details>

<details markdown="1"><summary>Example 2</summary>
### Input
```
10
```

### Output
```
Fibonacci number 10 is: 55.
```
</details>

<details markdown="1"><summary>Example 3</summary>
### Input
```
17
```

### Output
```
Fibonacci number 17 is: 1597.
```
</details>

<details markdown="1"><summary>Example 4</summary>
### Input
```
20
```

### Output
```
Fibonacci number 20 is: 6765.
```
</details>