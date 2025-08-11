# <b>Assignment</b>

Write a program that asks the user for a positive integer, and then prints the complete Collatz sequence (also called the <code>3n + 1</code> sequence), starting from that number and ending at 1.

<details markdown="1"><summary>What is the Collatz Conjecture?</summary>  
The Collatz Conjecture states that for any positive integer, you can calculate the next number using the following rules:  

1. **If the number is even**, divide it by 2.
2. **If the number is odd**, multiply it by 3 and add 1.

Repeat these steps over and over. According to the hypothesis, you will always eventually reach the number 1, no matter which positive integer you start with.

Here are some examples:

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
      <th>Starting number</th>
      <th>Collatz sequence</th>
      <th>Why?</th>
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

<i>(PS: While this hypothesis has not been mathematically proven, no one has yet found a positive integer that does not end at 1.)</i>

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
Collatz sequence: 6, 3, 10, 5, 16, 8, 4, 2, 1.
```

</details>  

<details markdown="1"><summary>Example 2</summary>  
### Input  
```
11
```  

### Output

```
Collatz sequence: 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.
```

</details>  

<details markdown="1"><summary>Example 3</summary>  
### Input  
```
19
```  

### Output

```
Collatz sequence: 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.
```

</details>