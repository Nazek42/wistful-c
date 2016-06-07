# WistfulC
A version of C that has seen better days...

### Usage
`python3 wistfulc.py [FILE]`

Alternatively, add this alias to your `.bashrc`:

    alias wistful_c='python3 /<path to wistful-c>/wistfulc.py'


### Substitutions
| Statement | Translation |
|-----------|-------------|
|`if only [LIB] were included...`|`#include LIB` (at beginning of generated code)|
|`if wishes were horses...`|`exit(0);`|
|`wish for [FORMAT], [VARS] upon a star`|`scanf(FORMAT, VARS);`|
|`wish [STR] upon a star`|`puts(STR);`|
|`if only [VAR] were [VALUE]...`|`VAR = VALUE;`|
|`if only I could return [VALUE]...`|`return VALUE;` (VALUE is optional)|
|`if [EXPR]...`|`if(EXPR) {`|
|`wait for [EXPR] to change...`|`while(EXPR) {`|
|`someday [EXPR]...`|`while(!(EXPR)) {`|
|`*sigh*`|`}`|
|`were`|`==`|
|`will be`|`==`|

When combined, these wistful and longing substitutions create depressing programs like this simple prime-checker:

    if only <stdio.h> were included...
    if only int n were 0...
    wish "Please enter a number:" upon a star
    wish for "%d", &n upon a star
    if n < 1 were true...
        wish "Not a whole number" upon a star
        if wishes were horses...
    *sigh*
    if only int i were 2...
    someday i will be n...
        if n % i were 0...
            wish "not prime" upon a star
            if wishes were horses...
        *sigh*
        if only i were i + 1...
    *sigh*
    wish "prime" upon a star
    if wishes were horses...
