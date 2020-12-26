

## Basics

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
* Three types of functions: `Named functions`, `Anonymous functions` and `immediately invoked function expressions`.
```
function <name>(<parameters>) {
    Do something
}
```
* Object constructor definition:
```
function <ClassName-first letter uppercase>(<parameters>) {
    <assignments and methods>
}
```
* Dot and bracket notation: in order to access properties of an object, either of these can be used. For e.g:
```
function Course(title, instructor) {
    this.title = title;
    this.instructor = instructor;
}
course1 = new Course("JavaScript", "xyz")
```
Here course1.title or course1.instructor can be used whereas, if Course has another attribute, say `count-of-students`. This is when it gets tricky.
If you try to get value of `count-of-students` using course1.count-of-students, JS tries to do an arithmetic operation and throws an error in which case, it is recommended to use course1["count-of-students"].
* A **closure** is a feature in JavaScript where an inner function has access to the outer (enclosing) function’s variables — a scope chain. The closure has three scope chains:
        * it has access to its own scope — variables defined between its curly brackets
        * it has access to the outer function’s variables
        * it has access to the global variables


## DOM Basics

* The document inside the browser window has its own object model called DOM (Document Object Model). DOM is the model that forms the current webpage.
* Target elements in the DOM:
        * Properties: document.title, document.body, document.url etc.
        * Methods: `document.getElementById()`, `document.getElementByClassName()`, `document.getElementByTagName()`, `document.getElementByTagNameNS()`.
        * The above methods are not efficient and become cumbersome in order to retrieve deeper elements. The following two methods addresses that issue: `document.querySelector()` and `document.querySelectorAll()`.