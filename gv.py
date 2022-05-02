
import marko as m
from marko.ext.latex_renderer import LatexRenderer as r
import sys
from ext.latex_equation import EquationExtension
from ext.latex_math import MathExtension
from ext.latex_quickfile import FileExtension
from ext.latex_preamble_factory import PreambleExtension

t = m.Markdown(
    renderer=r, extensions=[
        EquationExtension,
        MathExtension,
        FileExtension,
        PreambleExtension(
            packages=["inputenc", "babel", "amsmath,amssymb,amsthm", "xcolor", "enumitem,setspace,graphicx", "mathtools"],
            preamble="""
\\DeclarePairedDelimiter\\set{\\{}{\\}} % usage: $\\set{1, 2, 3}$
\\DeclarePairedDelimiter\\abs{\\lvert}{\\rvert}
\\DeclarePairedDelimiter\\norm{\\lVert}{\\rVert}
\\DeclarePairedDelimiter\\ceils{\\lceil}{\\rceil}
\\DeclarePairedDelimiter\\floor{\\lfloor}{\\rfloor}
\\DeclarePairedDelimiter\\angles{\\langle}{\\rangle}
\\def\\then{\\ensuremath{\\Rightarrow}} % =>;
\\def\\iff{\\ensuremath{\\Leftrightarrow}} % if and only if &lt;=&gt;
\\def\\to{\\ensuremath{\\rightarrow}} % ->;
\\def\\Oh{\\ensuremath{\\mathcal{O}}} % Big-O like $\\Oh(n)$
\\def\\sheetNumber{1}
\\def\\names{NAMES}
\\def\\sumPoints{20}
            """,
            documentclass="scrartcl",
            header="""
\\begin{doublespace} % header
\\noindent \\textbf{\\Large{Exercise sheet \\sheetNumber}}
\\hfill  {\\large Points: $\\boxed{\\qquad  /\\; \\sumPoints}$}\\\\
{\\Large \\textbf{Visualization of Graphs (Summer Term 2022)}\\\\
Submission by: \\textbf{\\names}\\\\
\\today}
\\end{doublespace}
            """
            )
        ]
    )

with open(sys.argv[1]) as f:
    print(t.convert(f.read()))

