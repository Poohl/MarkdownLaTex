
import marko as m

class Equation(m.inline.InlineElement):
    pattern = r'\$\$\s([^\n]*)'
    def __init__(self, match):
        #print("Found Eqation")
        self.eq = match.group(1)

class EquationRenderMixin(object):
    def render_equation(self, element):
        return f"\\[\n    {element.eq}\n\\]"

class EquationExtension:
    elements = [Equation]
    renderer_mixins = [EquationRenderMixin]
