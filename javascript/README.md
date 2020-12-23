

## Things to know

* Javascript is Case sensitive
* Use camelCase for variables and function names
    * Variables start with lowercase letter
    * Objects and Classes start with uppercase letter
    * Constants are all-caps
*  Recommended to end each statement with a semicolon
* Add comments as needed: single line(`//`) and multi-line comments (`/* */`)
* To avoid global scope, always declare variables using _var_ prefix
* Data Types in JavaScript:
    * Numeric: any integers
    * String: strings of letters and symbols
    * Boolean: binary true or false
    * null: intentional absence of a value. E.g: var a = null;
    * undefined: you create a variable but don't set it to anything. E.g: var a;
    * Symbol
* Use _typeof_ to determine what type of variable it is
* JS uses standard Arithmetic operators and Algebra rules while evaluations (braces evaluated first in expression)
    * Unary operator: `++`, `--`
    * Logical operator: `&&`, `||`. XOR: `if ( ( a == b || c == d ) ) && ( a == b ) != ( c == d ) ){}` or `if (x ? !y : y) {}`
    * Ternary operator: `? :`
    * In JS, the `==` is to check if the variables on both sides of the sign are same or not. 
    * **NOTE:** "5" == 5 is true in JS. To avoid this, use `===`. "5" === 5 returns false.
* If condition:
```
if (condition) {
  Do something
} else {
  Do something else
}
```
* Each value in the JS Array can be of different data type. Index start with 0.
    * Length of an array: `<array-name>.length`
    * Reverse an array: `<array-name>.reverse()`
    * Remove first value in an array: `<array-name>.shift()`
    * Add new items to front of array: `<array-name>.unshift(<comma-separated-elements-to-be-added>)`
    * Remove last value in an array: `<array-name>.pop()`
    * Add new items at end of array: `<array-name>.push(<comma-separated-elements-to-be-added>)`
    * Remove a set of items in an array (at any other location; neither first nor last): `<array-name>.splice(<start-pos>, <number-of-elements>)`
    * Copy of an array: `<array-name>.slice()`
    * Index of an element: `<array-name>.indexOf(<element-t-search>, <index-to-start-searching>)`
    * Join elements in array: `<array-name>.join(<separator>)`