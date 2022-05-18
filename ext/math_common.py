
replace_dict = {
    "==>": "\\Rightarrow ",
    "<==": "\\Leftarrow ",
    "<=": "\\le ",
    ">=": "\\ge ",
    "->": "\\rightarrow ",
    "<-": "\\leftarrow ",
    "*": "\\cdot "
}

def texify_math(m: str):
    for (o,n) in replace_dict.items():
        m = m.replace(o,n)
    return m
