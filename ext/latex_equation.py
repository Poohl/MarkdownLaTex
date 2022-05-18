
import marko as m
from ext.math_common import texify_math

class Equation(m.inline.InlineElement):
    pattern = r'\$\$\s([^\n]*)'
    def __init__(self, match):
        self.eq = match.group(1)

class EquationRenderMixin(object):
    def render_equation(self, element):
        return f"\\[\n    {texify_math(element.eq)}\n\\]"

class EquationExtension:
    elements = [Equation]
    renderer_mixins = [EquationRenderMixin]
