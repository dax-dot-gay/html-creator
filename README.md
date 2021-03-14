# html-creator
Python library to dynamically generate html in an etree-like structure

## Installation
Run `pip install html-creator` or download zip/clone
***
## Example
```py
from html_creator import *
doc = Document(title='Demo HTML Script')  # Title Of the page [ <title> ]
doc.body.append(Element(tag='h1')) # Having List Index as 0
doc.body[0].append(Element(content='Demo Header with tag h1 ( hover the mouse to see magic ) ')) # Assigning the value to 0
doc.body.append(Element(tag = 'br')) # Index 1
doc.body.append(Element(tag='div')) # Index 2
doc.body[2].append(Element(content='This is the content added in div tag (font bold)'))
doc.body.append(Element(tag = 'a')) # Index 3 
doc.body[3].append(Element(content= "Example Paragraph ( turns blue )"))
style = CSS()  # CSS() Class
style.add_sel('h1') 
style.add_property('h1', 'text-transform',' uppercase')
style.add_sel('h1:hover')
style.add_property('h1:hover', 'font-size', '60px')
style.add_sel('div')
style.add_property('div', 'font-weight', 'bold')
style.add_sel('a')
style.add_property('a','color','blue')
doc.head.append(Element(tag='style',content=str(style)))
with open('test.html','w') as f:
    print(str(doc),file=f)
```

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
