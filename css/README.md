
## Basics

* HTML defines the structure and meaning of the content whereas CSS controls the appearance of the HTML elements and separates the presentation from content.
* Syntax:
```
Selector {
  property: value;
}
```
* Comments: `/*....*/`
* Colors: can be defined via the following methods
  * RGB: defines colors according to Red, Green and Blue components
  * Hexadecimal: prefixed with number sign followed by six characters
  * The `rgb()` function can be represented by 3 numbers between 0-255 or 0%-100% to set red, green and blue colors.
  * An optional alpha can also be added for Opacity. Use function `rgba()` function in such case.
  * Another function, `hsl()` or `hsla()` is also a color function which defines the color based on hue, saturation and lightness.
* Type selectors: the most basic kind of selector, simple matching pattern. For e.g: 
```
h1 {

}
```
selects all the H1 elements in the document.
* Universal selector: selects every single element in the document. It is represented using the following notation:
```
* {
  properties
}
```
Rarely used. `*` indicates every element in the document.
* Class and ID selectors: 
  * For class selector, add the class attribute to the HTML element. 
  * Class selectors are reusable. 
  * Class selector begin with `.`. 
  * ID selectors are similar to class selector except it begins with `#` and are not reusable (used only once per page)
  * Naming convention: use a hyphen or underscore in names, if it is more than 1 word
* Descendant Selectors: applied to elements specifically nested inside another element.
* CSS Styles can be inherited from the ancestor to descendant elements. Specificity determines how browsers decide which CSS rule takes precedence. Selectors from lowest to highest.
    1. Universal (`*`)
    1. Type (`p`)
    1. class (`.example`)
    1. id (`#example`)
* Specificity calculation:
  * Count the number of ID selectors
  * Count the number of class, attribute and pseudo-class selectors
  * Count the number of type and pseudo-element selectors
  * The universal selector has a value of 0.
* The cascade in Cascading Style Sheets refer to how style rules are applied based on specificity and source order. 
  * Style declarations cascade are read from top to bottom. Declaration loaded last will take precedence in case of duplicates.
  * Source order matters except when the selectors are more specific. Styles with higher specificity will take precedence regardless of the order.
  * The **!important** keyword overrides source order and specificity. Not recommended unless necessary.
* 
