
import marko as m

class File(m.inline.InlineElement):
    pattern = r'<\s+([^\r\n]+)\.([^\r\n\s.]+)( [^\n]+)?'
    def __init__(self, match):
        self.path = match.group(1) + '.' + match.group(2)
        self.type = match.group(2)
        self.args = match.group(3).split(" ") if match.group(3) else []

class FileRenderMixin(object):
    def render_file(self, element):
        if element.type == 'tex':
            with open(element.path) as f:
                return f.read()
        elif element.type in ('png', 'jpg', 'jpeg'):
            self._packages.add("graphicx")
            filename = os.path.basename(element.path[:-len(element.type)-1])
            i = 0
            if len(element.args) > i and element.args[i].isdigit():
                width = "0." + element.args[i]
                i += 1
            else:
                width = "1"
            caption = " ".join(element.args[i:]) if len(element.args) > i else filename
            return f"\\begin{{figure}}\n\\centering\n\\includegraphics[width={width}\\textwidth]{{{element.path}}}\\caption[{caption}]{{{caption}}}\\label{{fig:{filename}}}\\end{{figure}}"
        elif element.type in ("py", "c", "cpp"):
            self._packages.add("listings")
            return f"\\lstinputlisting{{{element.path}}}"
        else:
            return "ERROR: unknown filetype included"

class FileExtension:
    elements = [File]
    renderer_mixins = [FileRenderMixin]
