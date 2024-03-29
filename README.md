# codesize

*Author: Jess Moore*

A simple library to print the number of lines of the largest code files in a project.

This package is useful to identify large files which generally should be reduced to make code easier to maintain. Writing short readable modular single purpose methods and easy to interpret code files is supported by this package which shows large files. Good practice is to limit files to less than 400-500 lines.


## Table of Contents
- [Installation](#install)
- [Demo](#demo)


## Installation  <a name="install"></a>
<font size="1">[Back](#top)</font>


Clone and install:
```
$ git clone https://github.com/jesscmoore/codesize.git
$ cd codesize
$ pip install -e .
```

Or import package directly from git:
```
pip install git+https://github.com/jesscmoore/codesize.git
python3 -c "from codesize import files; files.large(limit=50)"
```

To install this package in your project, add below to your requirements list
```
"codesize @ git+https://github.com/jesscmoore/codesize.git"
```
and then rebuild your package with:
```
pip install -e .
```

## Demo  <a name="demo"></a>
<font size="1">[Back](#top)</font>

List dart files greater than 400 lines

```
from codesize import files

files.large(limit=400, ext="dart")
```

Or on command line, list dart files larger than 400 lines

```
python3 examples/print_large_files.py 400
```


Alternatively use the make rule

The default is limit of 500 lines and file extension `py`.

```
make prep_large LIMIT=400 EXT=dart
```

Good practice is limiting file size to 400-500 lines.



**Ruff on command line**

Our makefile also has several `ruff` linter commands. The errors that are safely fixable with --fix option are marked with `*`

1. `make prep FILE=[file]` - List lint issues of a specific file or for whole project use `make prep`.
2. `make prep_stats FILE=[file]` - Show summary of issues of a specific file or for whole project with `make prep_stats`.
3. `make prep_fix FILE=[file]` - Automatically fix the safely fixable issues  of a specific file or for whole project with `make prep_fix`.
4. `make prep_rules RULE=E501` - Show summary of number of a specific rule violation in files with issues for a specific rule e.g. E501 (long lines), or for the default D1 (all docstring) rules with `make prep_rules`.
