# codesize

**CLI to identify the largest code files in a project and show their number of lines.**

*Time-stamp: <Friday 2025-07-18 10:54:11 +1000 Jess Moore>*

*Authors: Jess Moore*

*License: GNU GPL V3*

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://raw.githubusercontent.com/jesscmoore/codesize/main/LICENSE)


[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://raw.githubusercontent.com/jesscmoore/codesize/main/LICENSE)
[![Last Updated](https://img.shields.io/github/last-commit/jesscmoore/codesize?label=last%20updated)](https://github.com/jesscmoore/codesize/commits/main/)
[![GitHub commit activity (main)](https://img.shields.io/github/commit-activity/w/jesscmoore/codesize/main)](https://github.com/jesscmoore/codesize/main)

This package is useful to identify large files for clean up to reduce technical debt and make code easier to maintain. Writing short readable modular single purpose methods and easy to interpret code files is supported by this package which shows large files. Good practice is to limit files to less than 400-500 lines.


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
