import re

def is_disabled_text_input(s):
    pattern_compiled = re.compile("[A-Za-z]")
    search_res = pattern_compiled.search(s)
    if search_res is None:
        return True



strs = ["", " ", " 1", " 1a"]
for s in strs:
    print(is_disabled_text_input(s))