

import marko as m
from ext.math_common import texify_math

class Math(m.inline.InlineElement):
    pattern = r'\$([^\$]+)\$'
    def __init__(self, match):
        #print("found math")
        self.math = match.group(1)

class MathRenderMixin(object):
    def render_math(self, element):
        return f"${texify_math(element.math)}$"

class MathExtension:
    elements = [Math]
    renderer_mixins = [MathRenderMixin]
