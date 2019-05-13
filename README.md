# html-creator
Python library to dynamically generate html in an etree-like structure

# Docs
***
`Document(title='')`: Your HTML document. 
## Args
- title: The title of your document. This is optional and can be specified later
## Methods
- Using `str()` on this object will return the formatted html content of the Document.
## Properties
- `Document.children`: The direct children of the document
- `Document.head`: The head tag of the document (automatically generated)
- `Document.body`: The body tag of the document (automatically generated)
***
`Element(tag='p',attrs={},content='')`: A single HTML element/tag
## Args
- tag: The tag name, like div, p, or h1
- attrs: The attributes of the element, in a dict
- content: Text content of your tag
## Methods
- Using `str()` on this object will return the formatted html tag, including formatted html versions of all child tags
- Using `len(Element object)` will return the number of children
- Using `Element[index]` will return the element at that index
- Using `Element.append(new Element object instance)` or `Element.add_child(new Element object instance)` adds a child Element to the Element
## Properties
- `tag`, `attrs`, `content`: See Args
- `children`: The direct children on the Element
***
`CSS(Dict={})`: A utility class for generating CSS
## Args
- Dict: Specifies a starting dictionary (Must be in form `{selector: {property: value,property: value,property: value}, selector2: {property: value,property: value,property: value}}`)
## Methods
- `del CSS[selector]` and `CSS[selector]`, respectively, delete and get the specified selector in the CSS object
- `add_sel(selector)`: Adds a selector to add properties to
- `add_property(selector, property, value)`: Adds property `property` with value `value` to selector `selector`
- `del_property(selector, property)`: Deletes property `property` from selector `selector`
- `str(CSS object)`: Returns a formatted CSS string
## Properties
- `dict`: The dictionary used by the CSS object. Can be edited directly, but could cause issues
