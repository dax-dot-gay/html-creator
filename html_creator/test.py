from __init__ import *

doc = Document(title='boi')
doc.body.append(Element(content='I am potat'))
doc.body.append(Element(tag='div'))
doc.body[1].append(Element(content='in a div :)'))
style = CSS()
style.add_sel('p')
style.add_property('p','color','red')
doc.head.append(Element(tag='style',content=str(style)))
with open('test.html','w') as f:
    print(str(doc),file=f)
