
## Basics

* `<b>` and `<i>` are explicit meaning they specify bold and italic respectively whereas `<strong>` and `<em>` are semantic. They specify that the enclosed text should be "strong" or "emphasised" in some way, usually bold and italic, but allow for the actual styling to be controlled via CSS. Hence these are preferred in modern web pages.
* Three kinds of lists: `Unordered`, `Ordered` and `Definition`.
* Inline Elements: `<q>` (to put quotes), `<b>`, `<i>`, `<em>` and `<strong>`. These are usually wrapped around phrases of text.
* Block-Level Elements: `<blockquote>`, `<p>`, `<ul>`, `<ol>` etc. They start a new block.
* The `<time>` element with its `datetime` attribute is how date & time are communicated so that browsers can display the proper date & time.
* `<pre>` element represents preformatted text which is to be presented exactly as written in the HTML file. If you don't want the intentional spacing or new lines by HTML, this is the tag to be used.
* `<sub>` and `<sup>` represent the subscript and superscript.
* `<small>` can be used to convey something that has very little prominence (like a copyright).
* Most commonly used Global attributes (can be used on all HTML elements):
    * `class`: allows to target all elements with that class in CSS or JS
    * `id`: allows to target a unique element with that id in CSS or JS
    * `contenteditable`: provides user a way to edit content
    * `lang`: language used to display the content
    * `dir`: direction in which the text flows
* Entity and characters: `&lt;` stands for `<`, `&gt;` stands for `>` and `&amp;` stands for `&`. Use ` &ndsp;` for non breaking space. HTML will know to not break the words around it.
* To link, use the anchor tag: `<a>` with the attribute `href` - hypertext reference; where you want to go when the text is clicked.
* The images can be displayed using `<img>` tag. There are four attributes: `src`, `alt`, `width` and `height`.
    * `src`: which image file to load
    * `alt`: substitute whenever image cannot be seen
* Image formats:
  * GIF
    * Does well compressing large areas of a single color
    * Limited color space of 256 colors
    * Can do transparency, with jagged edges
    * Can have multiple frames, and make a little movie
  * SVG (Scalable Vector Graphic) - best and recommended
    * Logos, icons etc
    * Vector file
  * JPG
    * image format for compressing photos
    * can be compressed
    * Size vs quality
  * PNG
    * Images that need transparency
    * Good at compression
    * Photos and Images
    * Depends on use case
* The `<img>` tag's `srcset` attribute allows to specify multiple files to be used based on either viewport width or image pixel width. The `sizes` attribute lists which size image to use at which media query.
* The `<picture>` tag with `source` and `srcset` can be used to download different images based on the viewport.
* The `<figure>` element is for anything that appears as a figure, illustrating something. The `<figcaption>` is for demonstrating a concept which needs a caption.
* The `<audio>` element is used to place audio. The `src` attribute is used to provide location of the audio.
    * `controls` attribute (with no value) is used to display controls in the browser
    * `loop` will loop the audio when done
    * `autoplay` will cause the audio to play as soon as the browser is loaded (at least in some browsers)
    * The `<source>` tag can be used inside `<audio>` element to specify multiple `src` attributes
* The `<video>` tag is used to embed video into browsers. Like `<audio>`, it also has `src` and `controls` attributes.
    * `<track>` element is placed inside a video element to provide captions for the video with `kind` attribute set to "captions"
* **Embedding** is placing content from one site into the body of a page on another site.
* Use the `charset` attribute in `<meta>`element (included in `<head>` section) to define the alphabet or set of characters for the script language. The old ASCII encoding standard is limited to 128 chars, focused on needs of certain European languages whereas the Unicode (utf-8) encoding standard has characters encompassing many languages.
* Use `<div>` and `<span>` as less as possible. Former is a block element and latter is an inline element.
* The html file must start with _doctype_. This is the declaration which indicates from which era the HTML file is from.
```
<!doctype html>
<html lang="en-US" dir="ltr">
    <head>
        ...
    </head>
    <body>
        ...
    </body>
</html>
```
* The `head` element contains information the browser needs to know, though it won't be displayed on the page. The `body` contains the information and content that will be displayed on the page.
* What goes inside `head`:
    * The `meta` element. Use only inside the head. Conveys the metadata about the page.
    * The `link` element. Links to a range of other assets we want to load.
        * The `rel` attribute tells the browser which kind of asset it is.
        * The `href` attribute provides the URL to the asset.
* What usually goes inside `body`:
    * The `main` element wraps around the main content of the page
    * The `header` and `footer` elements are used to mark places on the page where the content is header or a footer.
    * The `article` element is wrapped around any instance of an article.
    * The `section` element wraps around sections of content.
    * The `aside` marks content that is off to the side or not the main attraction.
* The `<table>` tag is used to create tables
    * The `<tr>` indicates a table row. Attributes: `colspan`, `rowspan` and `headers`
    * The `<th>` indicates a table header. Attributes: `colspan`, `rowspan` and `scope`
    * The `<td>` indicates table data