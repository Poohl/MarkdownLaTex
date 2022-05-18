

import marko as m
from ext.math_common import texify_math
import logging

class Math(m.inline.InlineElement):
    pattern = r'\$([^\$]+)\$'
    def __init__(self, match):
        self.math = match.group(1)
        logging.debug(f"found math {self.math}")

class MathRenderMixin(object):
    def render_math(self, element):
        logging.debug(f"render math {element.math}")
        return f"${texify_math(element.math)}$"

class MathExtension:
    elements = [Math]
    renderer_mixins = [MathRenderMixin]
