.PHONY : statement

statement : build/statement/stat.pdf

build/statement/stat.pdf : build/statement/stat.tex
	xelatex $<
	xelatex $<
	xelatex $<

build/statement/stat.tex : $(
	
