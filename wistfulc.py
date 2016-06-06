sample_code = """\
if only <stdlib.h> were included...
if only <stdio.h> were included...
if only <math.h> were included...
if only int x were 3...
if x were 3...
wish "Hello World" upon a star
*sigh*
if wishes were horses..."""

import re
from functools import reduce
import subprocess
import os
import sys

def add_to_includes(matchobj):
    includes.append("#include " + matchobj.group(1))

SUBS = [
    (r"if wishes were horses\.\.\.", "exit(0);"),
    (r'wish for (.*?) upon a star', r"scanf(\1);"),
    (r"wish (.*?) upon a star", r"puts(\1);"),
    (r"if only (<.*?>) were included\.\.\.", add_to_includes),
    (r"if only ([\w *]+) were (.*?)\.\.\.", r"\1 = \2;"),
    (r"if only I could return (.*?)\.\.\.", r"return \1;"),
    (r"\*sigh\*", "}"),
    (r"if (.*?) ?\.\.\.", r"if(\1) {"),
    (r"wait for (.*?) to change\.\.\.", r"while(\1) {"),
    (r"someday (.*?) ?\.\.\.", r"while(!(\1)) {"),
    (r" +were +", r" == "),
    (r" +will be +", r" == "),
]

includes = ["#include <stdbool.h>"]

def compile_code(code):
    global includes
    
    compiled = reduce(lambda code, sub: re.sub(sub[0], sub[1], code), SUBS, code)
    return "\n".join(includes)+"\nint main() {" + compiled + "}"

def run_code(compiled):
    with open("temp.c", "wt") as source_file:
        source_file.write(compiled)
        
    subprocess.call(["gcc", "-w", "-o", "temp", "temp.c"])
    subprocess.call(["./temp"])
    
    os.remove("temp")
    os.remove("temp.c")

if __name__ == "__main__":
    with open(sys.argv[1]) as code_file:
        run_code(compile_code(code_file.read()))
