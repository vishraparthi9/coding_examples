
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

