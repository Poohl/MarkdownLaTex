

import marko as m
import logging

class InlineLatex(m.inline.InlineElement):
    pattern = r'%([^%]+)%'
    def __init__(self, match):
        self.latex = match.group(1)
        logging.debug(f"found inline latex {self.latex}")

class InlineLatexRenderMixin(object):
    def render_inline_latex(self, element):
        logging.debug(f"render inline latex {element.latex}")
        return element.latex

class InlineLatexExtension:
    elements = [InlineLatex]
    renderer_mixins = [InlineLatexRenderMixin]
