# codesize

A simple library to print the number of lines of the largest code files in a project.

This is useful to identify large files which generally should be reduced to make code easier to maintain.

Writing short readable modular single purpose methods and easy to interpret code files is supported by this package which shows large files and how to use ruff (Limit files to < 500 lines)*

Demonstrator: [https://anuco.au](https://anuco.au)

## Table of Contents
- [Installation](#install)
- [Demo](#demo)


## Installation  <a name="install"></a>
<font size="1">[Back](#top)</font>

```
$ git clone https://github.com/anusii/travelco2e.git
$ cd travelco2e
$ make install
```

Note that newer python installations are moving to `pipx` and some
requisite packages are also required. However I had to still use
`--break-system-packages` for the dash packages to be found. Might be
my (gjw) setup.

```
$ pip install dash dash_mantine_components --break-system-packages
$ sudo apt install python3-dotenv
$ pipx install -e .
```

Run locally in development mode (supports hot reload). This will create `.env` with development settings and the dashboard at https://127.0.0.1:[PORT]

```
$ make app
```

You can use option SKIP_LOGIN=True environment variable in `.env` to skip the login authentication and directly access the dashboard after click the 'Login' button. This is useful for testing the dashboard locally outside the ANU when VPN service is not available and LDAP server cannot be connected.


## Demo  <a name="demo"></a>
<font size="1">[Back](#top)</font>

List files larger than some number of lines, usually 400-500 lines with

```
make prep_large
```

which uses the default 500 lines limit.

Or provide specify your preferred number of lines threshold with

```
make prep_large LIMIT=400
```

## Dev practice

Using this package for large file detection and `ruff` for linting and formatting provides a good setup for most needs. Ruff can be setup with a pre-commit hook and as an extension in VSCode. This project uses `ruff` for linting and formatting. The ruff configuration of rules and style conventions is set in `pyproject.toml`.


**Vscode ruff extension:**

- The VScode ruff extension will identify the lint and formatting issues configured in pyproject.toml `[tool.ruff*]` tables.
- Adding below to .vscode/settings.json will configure vscode to format on save using ruff

```
$ cat .vscode/settings.json
{
    "notebook.formatOnSave.enabled": true,
    "[python]": {
        "editor.formatOnSave": true,
        "editor.defaultFormatter": "charliermarsh.ruff"
    },
}
```

**Pre-commit hooks:**

- A ruff [pre-commit](https://pre-commit.com/) hook in `.pre-commit-config.yaml` will check for all linting and formatting issues when a user runs commits changed files. `git commit`.
- To setup `pre-commit`:
  + Install pre-commit with pip/brew/other. Eg. `pipx install pre-commit`
  + Install the project git hook scripts in `.pre-commit-config.yaml` into your project by running `pre-commit install`
- To run pre-commit:
  + Edit your files, `git add ...` as usual, and `git commit ...` as usual. During the commit, ruff will run to fix the safely fixable files and report any remaining issues.
  + Manually fix any remaining identified issues, then git add, commit and push as usual to send your changes to remote. As ruff lint and format fixes can be applied sequentially, you may need several git commits to resolve the ruff issues in a file.

**Ruff on command line**

- Ruff can also be used on commandline. Here are some useful examples. The errors that are safely fixable with --fix option are marked with `*`

1. List lint issues of a specific file with `make prep FILE=[file]` or for whole project with `make prep`.
2. Show summary of issues of a specific file with `make prep_stats FILE=[file]` or for whole project with `make prep_stats`.
3. Automatically fix the safely fixable issues  of a specific file with `make prep_fix FILE=[file]` or for whole project with `make prep_fix`.
4. Show summary of number of a specific rule violation in files with issues for a specific rule e.g. E501 with `make prep_rules RULE=E501` or for the default D1 (all docstring) rules with `make prep_rules`.
