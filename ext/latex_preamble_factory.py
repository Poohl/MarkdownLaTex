
class PreambleRenderMixin(object):
    def render_document(self, element):
        # should come first to collect needed packages
        for p in self.packages:
            self._packages.add(p)
        children = self.render_children(element)
        # create document parts
        items = [f"\\documentclass{{{self.documentclass}}}"]
        # add used packages
        items.extend(f"\\usepackage{{{p}}}" for p in self._packages)
        # preamble before document starts
        items.append(self.preamble)
        # add inner content
        items.append(self._environment("document", self.header + children))
        return "\n".join(items)

class PreambleExtension(object):
    def __init__(self, header="", preamble="", documentclass="article4", packages=[]):
        PreambleRenderMixin.documentclass = documentclass
        PreambleRenderMixin.preamble = preamble
        PreambleRenderMixin.header = header
        PreambleRenderMixin.packages = packages
        self.renderer_mixins = [PreambleRenderMixin]

