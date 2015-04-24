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
import random
from subprocess import Popen

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

def deckblatt():
	_template = latex_jinja_env.get_template('testt.tex')
	with open('work/deckblatt.tex', 'w') as f:
		f.write(_template.render(name='Bernd Lieferts'))

def anschreiben():
	_template = latex_jinja_env.get_template('testt.tex')
	with open('work/anschreiben.tex', 'w') as f:
		f.write(_template.render(name='Manfred Linz'))

def lebenslauf():
	_template = latex_jinja_env.get_template('testt.tex')
	with open('work/lebenslauf.tex', 'w') as f:
		f.write(_template.render(name='Ferdinand Koff'))

def bewerbung():
	_template = latex_jinja_env.get_template('bewerbung.tex')
	with open('work/bewerbung.tex', 'w') as f:
		f.write(_template.render(deckblatt=mit_deckblatt))

def main():
	# Person generieren
	name = 'Manfred Linz'

	# aufräumen
	Popen('rm -f work/*', shell=True).wait()
	
	mit_deckblatt = random.randint(0,1)
	if mit_deckblatt:
		deckblatt()
		deck_proc = Popen('pdflatex -interaction=nonstopmode -output-directory=work work/deckblatt.tex', shell=True)

	anschreiben()
	ans_proc = Popen('pdflatex -interaction=nonstopmode -output-directory=work work/anschreiben.tex', shell=True)

	lebenslauf()
	leb_proc = Popen('pdflatex -interaction=nonstopmode -output-directory=work work/lebenslauf.tex', shell=True)

	# wait for pdf generation
	if mit_deckblatt:
		deck_proc.wait()
	ans_proc.wait()
	leb_proc.wait()
	
	bewerbung()
	Popen('pdflatex -interaction=nonstopmode -output-directory=work work/bewerbung.tex', shell=True).wait()
	Popen("mv work/bewerbung.pdf 'bewerbungen/Bewerbung {0}.pdf'".format(name), shell=True).wait()

if __name__ == "__main__":
	main()
