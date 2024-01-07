########################################################################
#
# Makefile for travelco2e app
#
# Time-stamp: <Thursday 2024-01-07 16:21:35 +1000 Jess Moore>
#
# Copyright (c) jessclaremoore@gmail.com
#
# License: Creative Commons Attribution-ShareAlike 4.0 International.
#
########################################################################

# App version numbers
#   Major release
#   Minor update
#   Trivial update or bug fix

APP=codesize
VER=0.0.1
DATE=$(shell date +%Y-%m-%d)

########################################################################
# HELP
#
# Help for targets defined in this Makefile.

define HELP
$(APP) cli:

  install                          Developer install $(APP) locally (only needed once)
  prep                             Run ruff linter in check mode on full project `make prep` or specific file
                                   `make prep FILE=[file]`
  prep_rules                       Format ruff output to show each file and issue occurance for specific
                                   rule. Default `D1` to show all missing doc strings. Eg. for D1 rules
                                   `make prep_rules` or for E501 rule `make prep_rules RULE=E501`
  prep_stats                       Show statistics of ruff in check mode on full project `make prep_stats` or
                                   specific file `make prep_stats FILE=[file]`
  prep_large                       Show files with greater than default limit with `make prep_large` or
                                   supply custom limit `make prep_large LIMIT=400`
  prep_fix                         Run ruff linter in fix mode on full project `make prep_fix` or specific file
                                   `make prep_fix FILE=[file]`

endef
export HELP

help::
	@echo "$$HELP"

########################################################################
# DEFAULTS
#

# File path used by ruff to constrain scope
FILE?=.

# Ruff rule of interest or rule prefix, default `D1` which is all
# ruff rules for missing docstrings
RULE?=D1

# Default large file threshold
LIMIT?=500


########################################################################
# LOCAL TARGETS
#

# Install in dev mode (-e) so changes here are immediately deployed.

install:
	python -m pip install -e .

prep:
	ruff check $(FILE)

prep_rules:
	ruff check . |grep $(RULE) | cut -d':' -f1,3 | sort | uniq -c | sort -r

prep_stats:
	ruff --statistics check $(FILE)

prep_large:
	python support/print_large_files.py $(LIMIT)

prep_fix:
	ruff --fix check $(FILE)
