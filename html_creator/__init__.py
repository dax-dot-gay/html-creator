class Element:
    def __init__(self,tag='p',attrs={},content=''):
        self.tag = tag
        self.attrs = attrs
        self.children = []
        self.content = content
    def add_child(self,child):
        self.children.append(child)
    def __str__(self):
        _str = ''
        attrstr = ''
        for a in list(self.attrs.keys()):
            if type(self.attrs[a]) == str:
                attrstr += a + '="' + self.attrs[a] + '" '
            else:
                attrstr += a + '=' + self.attrs[a] + ' '
        _str += '<'+self.tag+' '+attrstr+'>\n\t'+'\n\t'.join(self.content.splitlines())
        for c in self.children:
            _str += '\n\t'+str(c)
        _str += '\n</'+self.tag+'>'
        return _str
    def __getitem__(self,i):
        return self.children[i]
    def append(self,item):
        self.add_child(item)
    def __len__(self):
        return len(self.children)

class Document:
    def __init__(self,title=''):
        self.children = []
        self.children.append(Element(tag='html'))
        self.children[0].add_child(Element(tag='head'))
        self.children[0].add_child(Element(tag='body'))
        self.head = self.children[0][0]
        self.body = self.children[0][1]
        self.head.add_child(Element(tag='title',content=title))
    def __str__(self):
        _str = '<!DOCTYPE html>'
        for c in self.children:
            _str += '\n\t'+str(c)
        return _str

class CSS:
    def __init__(self,Dict={}):
        self.dict = Dict
    def __getitem__(self,item):
        return self.dict[item]
    def add_sel(self,sel):
        self.dict[sel] = {}
    def __delitem__(self,key):
        del self.dict[key]
    def add_property(self,key,property,value):
        self.dict[key][property] = value
    def del_property(self,key,property):
        del self.dict[key][property]
    def __str__(self):
        ret = ''
        for k in self.dict.keys():
            ret += k + ' {'
            for p in self.dict[k].keys():
                ret += '\n\t' + p + ': ' + self.dict[k][p] + ';'
            ret += '\t\n}'
        return ret
