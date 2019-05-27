.PHONY : statement clean

statement : build/statement/statement.pdf

build/statement/statement.pdf : $(shell find contest -type f)
	mkdir -p $(dir $@)
	./pc api.texsyn.contest > build/statement/statement.tex
	xelatex --output-directory=$(dir $@) build/statement/statement.tex
	xelatex --output-directory=$(dir $@) build/statement/statement.tex
	xelatex --output-directory=$(dir $@) build/statement/statement.tex

clean :
	rm -rf build
