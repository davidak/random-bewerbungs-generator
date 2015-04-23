#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# Copyright (C) 2015 davidak
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see {http://www.gnu.org/licenses/}.

import os
import jinja2

__version__ = '0.1'

latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%-',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('templates/'))
)

template = latex_jinja_env.get_template('testt.tex')

with open('test.tex', 'w') as f:
	f.write(template.render(name='Bernd Lieferts'))

os.system('pdflatex test.tex -interaction nonstopmode')

def deckblatt():
	# -> deckblatt.tex
	pass

def anschreiben():
	# -> anschreiben.tex
	pass

def lebenslauf():
	# -> lebenslauf.tex
	pass

def main():
	# Person generieren
	# -> bewerbung.tex -> bewerbung.pdf 
	# deckblatt optional
	pass

if __name__ == "__main__":
	main()
